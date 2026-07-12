# EPRP protocol reference

Use this reference when implementing structured course state, lesson state, assessment, routing, or persistence.

## Layered state

Keep course orchestration separate from the current EPRP lesson:

```json
{
  "course": {
    "course_id": "psychology-foundations-v1",
    "learning_goal": "Build a broad foundation in psychology",
    "curriculum_version": 1,
    "next_lesson_id": "m1-l1"
  },
  "source_context": {
    "instruction": "Web research allowed",
    "capabilities_used": ["web_search", "web_read"],
    "grounding_policy": "supplemented"
  },
  "lesson": {
    "lesson_id": "m1-l1",
    "outcome": "Distinguish behavior from inferred mental processes",
    "phase": "probe",
    "attempt": 1,
    "source_anchors": ["source-1#heading-2"],
    "next_action": "await_learner"
  }
}
```

Keep learner preferences separate from demonstrated evidence.

## Phase contract

| Phase | Required input | Responsibility | Completion evidence |
|---|---|---|---|
| Explain | Lesson outcome, concept, learner context, relevant sources | Build an accurate representation | A bounded explanation is delivered |
| Probe | Concept and prior explanation | Collect evidence of understanding | One learner response is available |
| Review | Probe, response, and relevant evidence | Diagnose reasoning and correct errors | Actionable feedback is delivered |
| Progress | Review and accumulated evidence | Update lesson and curriculum state | A progress record exists |

## Probe assessment

```json
{
  "relevance": "relevant",
  "understanding": "partial",
  "evidence": ["Learner distinguishes observable behavior from emotion"],
  "misconceptions": ["Learner treats all cognition as directly observable"],
  "user_intent": "answer",
  "confidence": 0.82,
  "suggested_next_action": "re_explain"
}
```

Recommended enums:

- `relevance`: `relevant | partially_relevant | off_topic`
- `understanding`: `clear | partial | confused | unknown`
- `user_intent`: `answer | ask_question | request_explanation | request_answer | change_goal | change_topic | pause | exit`
- `suggested_next_action`: `advance | re_explain | probe_again | revisit_prerequisite | adjust_curriculum | pause | stop`

Confidence expresses assessor uncertainty, not proof.

## Progress record

```json
{
  "lesson_id": "m1-l1",
  "concepts_exposed": ["behavior", "cognition", "emotion"],
  "evidence": [
    {
      "concept": "behavior",
      "understanding": "clear",
      "basis": "Learner correctly identified an observable action"
    }
  ],
  "misconceptions": ["Treats cognition as directly observable"],
  "sources_used": [
    {
      "source_id": "source-1",
      "anchors": ["heading-2"],
      "role": "course_backbone"
    }
  ],
  "external_supplements": [],
  "support_used": ["concrete_example"],
  "next_lesson_action": "repeat_with_new_strategy",
  "curriculum_action": null
}
```

Record only evidence demonstrated by the learner. Do not infer complete mastery from one response.

## Deterministic routing

Apply safety, authorization, explicit source constraints, and user control first:

```text
if intent is exit or pause:
    stop or persist checkpoint
else if intent changes the learning goal:
    revise the course brief and curriculum
else if intent requests a direct answer:
    provide the answer and make probing optional
else if intent requests explanation:
    explain with a different strategy
else if understanding is confused:
    re-explain or revisit a prerequisite
else if enough evidence exists:
    review, write Progress, and select a curriculum action
else:
    ask one narrower probe
```

The model may propose transitions. The host should validate permissions, required data, and allowed state transitions.

## Re-explanation strategies

Choose a strategy different from the failed one:

- concrete example
- counterexample
- analogy with stated limits
- visual representation
- worked example
- decomposition
- prerequisite repair
- compare-and-contrast
- learner-generated explanation followed by correction

Record the selected strategy when possible.

## Persistence contract

With persistent state, save:

- course brief and curriculum version
- source instruction and capabilities used
- completed lessons and next lesson
- demonstrated evidence and unresolved misconceptions
- curriculum changes and reasons

Without persistence, maintain a compact conversational checkpoint and do not claim durable memory.
