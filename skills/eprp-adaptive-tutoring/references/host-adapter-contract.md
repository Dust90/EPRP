# Host adapter contract

Use this reference when implementing EPRP in a concrete Agent host. The Skill defines teaching protocol; the host adapter enforces capabilities, structured state, and permitted transitions.

## Responsibility boundary

| Responsibility | Skill / model | Host adapter |
|---|---|---|
| Identify learning goal and information needs | Propose | Validate user scope |
| Select teaching strategy | Propose | Execute only permitted actions |
| Discover capabilities | Consume declared capability context | Enumerate actual capabilities |
| Search, read files, query knowledge bases | Request through available tools | Authorize and execute tools |
| Interpret learner response | Produce structured assessment | Validate schema and route state |
| Update course and lesson state | Propose record | Persist accepted record |
| Claim source access, retrieval, or persistence | Never infer | Supply tool results as the only evidence |

Do not expose fictional or unavailable capabilities to the model. Treat successful tool results, accessible source metadata, and stored state as the only evidence that an external action occurred.

## Minimum capability context

Inject a compact, authoritative host-owned capability context each turn:

```json
{
  "available": ["web_search", "web_read", "persistent_learning_state"],
  "unavailable": ["knowledge_base_search", "local_file_read"],
  "constraints": {
    "web_search": "public sources only",
    "persistence": "current user namespace"
  },
  "source_instruction": "Web research allowed"
}
```

The model may request only capabilities in `available`. The adapter rejects tool calls outside that set and records any denial as a limitation, not as a completed action.

## Required structured outputs

Validate model-produced records before applying them.

### Probe assessment

```json
{
  "relevance": "relevant",
  "understanding": "partial",
  "attempt_outcome": "misconception_detected",
  "evidence": ["Learner distinguishes correlation from causation"],
  "misconceptions": ["Learner assumes correlation proves causation"],
  "user_intent": "answer",
  "suggested_next_action": "re_explain"
}
```

Use only these enums:

- `relevance`: `relevant | partially_relevant | off_topic`
- `understanding`: `clear | partial | confused | unknown`
- `attempt_outcome`: `demonstrated_understanding | partial_understanding | misconception_detected | insufficient_evidence | off_topic | learner_requested_help`
- `user_intent`: `answer | ask_question | request_explanation | request_answer | change_goal | change_topic | pause | exit`
- `suggested_next_action`: `advance | re_explain | probe_again | revisit_prerequisite | adjust_curriculum | pause | stop`

Do not accept a numeric confidence score as routing evidence. If uncertainty matters, use explicit `insufficient_evidence` and ask a narrower Probe.

### Progress record

Accept a Progress record only when it identifies the current lesson, demonstrated evidence, unresolved items, source provenance when used, and one allowed next action. Never persist a claim of mastery without learner evidence.

## Deterministic transition rules

Apply these rules in order:

```text
if user_intent in {exit, pause}:
    transition to pause_or_exit
elif user_intent in {change_goal, change_topic}:
    transition to curriculum_revision
elif user_intent == request_answer:
    transition to explain; probing becomes optional
elif user_intent in {ask_question, request_explanation}:
    transition to explain with a different strategy
elif attempt_outcome == off_topic:
    transition to intent_clarification
elif attempt_outcome == insufficient_evidence:
    transition to narrower_probe
elif attempt_outcome in {misconception_detected, learner_requested_help}:
    increment unresolved_attempts for current concept
    transition to re_explain
elif attempt_outcome == partial_understanding:
    preserve correct evidence; choose narrower_probe or re_explain
elif attempt_outcome == demonstrated_understanding:
    transition to review_then_progress
else:
    transition to narrower_probe
```

The adapter, not the model, increments counters and commits transitions.

## Define unsuccessful re-explanations

Count an unsuccessful attempt only when the learner has engaged with the same core concept and the accepted assessment is one of:

- `misconception_detected`
- `learner_requested_help`
- `partial_understanding` after a re-explanation, when the same blocking gap remains

Do not count:

- pause, exit, or a goal change
- an off-topic response
- missing or inaccessible material
- `insufficient_evidence`; ask a narrower Probe instead
- a tutor error or a source contradiction

After two counted unsuccessful attempts for the same concept:

1. mark the concept as unresolved;
2. select `revisit_prerequisite` or ask the learner to identify the blocker;
3. require the next Explain to use a materially different strategy;
4. preserve the learner's ability to skip or request a direct answer.

## Validate source and persistence claims

- Attach citations, anchors, and retrieval provenance only from tool results supplied by the adapter.
- Reject fabricated source IDs, pages, URLs, document IDs, or timestamps.
- Reject a `capabilities_used` entry that has no corresponding successful host tool result.
- When no persistent store exists, keep a session checkpoint only and label it as non-durable.
- When a tool fails, record the failure and offer a fallback; never convert it into a successful source claim.

## Adapter conformance tests

An adapter is conformant only if it can demonstrate:

1. unavailable tools cannot be called or claimed;
2. malformed assessment records are rejected;
3. state transitions follow the deterministic table;
4. failure counters change only under the defined conditions;
5. two unsuccessful attempts trigger prerequisite repair or blocker clarification;
6. user exit, pause, direct-answer, and source constraints override default routing;
7. source and persistence claims are derived from real host results.
