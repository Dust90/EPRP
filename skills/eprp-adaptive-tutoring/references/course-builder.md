# Course builder

Use this reference when converting a learning goal and available sources into a curriculum or when Progress requires curriculum revision.

## Define the course brief

Capture only information that changes the course:

```json
{
  "subject": "psychology",
  "learning_goal": "Build a broad foundation for informed self-study",
  "starting_level": "beginner",
  "desired_depth": "undergraduate overview",
  "constraints": {
    "time": "30 minutes per day",
    "source_instruction": "Web research allowed"
  }
}
```

Infer fields from the request when possible. Ask one question at a time only for material ambiguity. Do not require all fields before beginning.

## Research the curriculum backbone

Use capability routing to collect enough evidence for a coherent course:

- authoritative taxonomies, standards, or curricula
- primary sources when the learning goal requires them
- reputable textbooks, open courses, official documentation, or review material
- current sources for changing subjects
- user-designated local or knowledge-base material

Do not confuse search-result popularity with authority. Prefer a small, diverse, relevant source set over a long uncurated bibliography.

## Build a proportional course

Create modules and lessons that:

- lead from prerequisites to the learner's outcome
- define a demonstrable outcome for each lesson
- contain one concept or tightly related concept cluster per EPRP unit
- identify source requirements without loading all sources every turn
- fit the user's time and depth
- avoid redundant “introduction” modules with no knowledge gain

Example:

```json
{
  "course_id": "psychology-foundations-v1",
  "title": "Foundations of Psychology",
  "learning_goal": "Understand how psychology studies behavior and mind",
  "modules": [
    {
      "id": "m1",
      "title": "Evidence and explanation",
      "lessons": [
        {
          "id": "m1-l1",
          "title": "What psychology explains",
          "concepts": ["behavior", "cognition", "emotion"],
          "outcome": "Distinguish observable behavior from inferred mental processes",
          "source_requirements": ["authoritative introductory overview"]
        }
      ]
    }
  ],
  "next_lesson_id": "m1-l1"
}
```

Do not generate an exhaustive course when a shorter first path can be adapted later.

## Present the course

Show enough structure for informed consent:

- goal and assumed starting level
- module sequence
- approximate lesson count or time when known
- source approach and important limitations
- where the learner will begin

Allow the learner to modify scope, order, depth, pace, or source constraints.

## Prepare each lesson

Before Explain:

1. select the current lesson outcome
2. retrieve the minimum relevant source material
3. resolve required prerequisites
4. carry forward relevant misconceptions and evidence
5. select a suitable initial teaching strategy
6. bind source anchors when available

## Adapt the curriculum from Progress

Progress may issue one curriculum action:

- `advance`
- `repeat_with_new_strategy`
- `insert_remedial_lesson`
- `skip_mastered_lesson`
- `deepen_current_topic`
- `reorder_lessons`
- `revise_goal`
- `pause`
- `complete_course`

Example:

```json
{
  "lesson_id": "m1-l2",
  "demonstrated_understanding": ["Distinguishes correlation from causation"],
  "unresolved": ["Confounding variables"],
  "curriculum_action": {
    "type": "insert_remedial_lesson",
    "before": "m1-l3",
    "topic": "Confounding variables and experimental control",
    "reason": "Current lesson evidence shows a prerequisite gap"
  }
}
```

Base adaptation on evidence, not engagement signals alone. Preserve the learner's ability to reject a route change.

## Handle course continuity

With persistence, save:

- course brief and current curriculum version
- source route and important provenance
- completed lessons
- demonstrated evidence and unresolved misconceptions
- curriculum changes and reasons
- next lesson

Without persistence, maintain a compact checkpoint in the conversation and avoid claiming durable storage.
