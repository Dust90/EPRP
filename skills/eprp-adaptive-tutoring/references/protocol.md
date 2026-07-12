# EPRP protocol reference

Use this reference when implementing structured state, routing, persistence, or host adapters.

## Phase contract

| Phase | Required input | Responsibility | Completion evidence |
|---|---|---|---|
| Explain | Goal, concept, learner context | Build an accurate initial representation | A bounded explanation is delivered |
| Probe | Concept and prior explanation | Collect evidence of understanding | One learner response is available |
| Review | Probe and learner response | Diagnose reasoning and correct errors | Actionable feedback is delivered |
| Progress | Review and accumulated evidence | Update learning state and select next action | A progress record or summary exists |

## Minimal session state

```json
{
  "phase": "probe",
  "topic": "CAP theorem",
  "learning_goal": "Explain the consistency and availability trade-off during a partition",
  "current_concepts": ["network partition"],
  "attempt": 1,
  "last_probe": "What choices remain when two nodes cannot communicate?",
  "next_action": "await_learner"
}
```

Use this shape when the host can preserve only session-local state.

## Probe assessment

```json
{
  "relevance": "relevant",
  "understanding": "partial",
  "evidence": ["Learner recognizes that nodes cannot coordinate"],
  "misconceptions": ["Learner assumes CAP requires choosing one property permanently"],
  "user_intent": "answer",
  "confidence": 0.82,
  "suggested_next_action": "re_explain"
}
```

Recommended enums:

- `relevance`: `relevant | partially_relevant | off_topic`
- `understanding`: `clear | partial | confused | unknown`
- `user_intent`: `answer | ask_question | request_explanation | request_answer | change_topic | pause | exit`
- `suggested_next_action`: `advance | re_explain | probe_again | revisit_prerequisite | pause | stop`

Do not treat `confidence` as proof. It expresses the assessor's uncertainty and should trigger clarification when low.

## Progress record

```json
{
  "unit_id": "distributed-systems.cap.partition",
  "concepts_exposed": ["network partition", "consistency", "availability"],
  "evidence": [
    {
      "concept": "network partition",
      "understanding": "clear",
      "basis": "Learner correctly predicted that isolated nodes cannot coordinate writes"
    }
  ],
  "misconceptions": [],
  "support_used": ["concrete_example"],
  "next_action": "advance"
}
```

Keep preferences separate from learning evidence:

```json
{
  "learner_preferences": {
    "language": "zh-CN",
    "desired_depth": "undergraduate",
    "tone": "direct"
  },
  "learning_state": {
    "evidence": [],
    "misconceptions": [],
    "completed_units": []
  }
}
```

## Deterministic routing

Apply host safety and user-control rules first, then route:

```text
if intent is exit or pause:
    stop or persist checkpoint
else if intent is request_answer:
    provide answer, then offer an optional probe
else if intent is request_explanation:
    explain with a different strategy
else if understanding is confused:
    re-explain or revisit a prerequisite
else if enough evidence exists:
    review, then update progress
else:
    ask one narrower probe
```

The model may propose a transition. The host should validate that it is permitted and that required data exists.

## Re-explanation strategies

Select a strategy different from the failed one:

- concrete example
- counterexample
- analogy with stated limits
- visual representation
- worked example
- decomposition into smaller steps
- prerequisite repair
- compare-and-contrast
- learner-generated explanation followed by correction

Record the strategy when possible so repeated attempts do not cycle through equivalent wording.
