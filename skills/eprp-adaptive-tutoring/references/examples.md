# Examples and evaluation cases

Read this reference when demonstrating or evaluating the complete learning workflow.

## Example: broad learning goal with Web Search

Learner: “I want to learn psychology systematically. You can search the web.”

Expected workflow:

1. Clarify the intended outcome only if needed: general foundation, professional application, research preparation, or another goal.
2. Inspect whether Web Search is actually available.
3. Research an authoritative curriculum backbone and suitable primary or educational sources.
4. Build a proportional first curriculum rather than an exhaustive psychology degree.
5. Start the first bounded lesson and run EPRP.
6. Adapt later lessons from demonstrated progress.

## Example: project operations from a knowledge base

Learner: “Search our operations knowledge base and create a course for new project operators.”

Expected workflow:

1. Use the specified knowledge-base capability only if available.
2. Preserve document provenance and coverage gaps.
3. Build lessons from the organization's terminology and actual workflows.
4. Ask before introducing public Web sources if the instruction implies an internal-only course.
5. Record whether learning evidence came from internal policy, examples, or external supplementation.

## Example: course from local documents

Learner: “Read these three project-operation documents and teach me from them. Do not search the web.”

Expected workflow:

1. Use the authorized file/document capability.
2. Do not call Web Search.
3. State inaccessible or corrupted regions.
4. Build a course across the document set, resolving duplicates and preserving contradictions.
5. Retrieve relevant sections for each lesson and run EPRP.

## Example: partial understanding

Learner: “Teach me database indexes.”

Explain: Give a bounded explanation of an index as an auxiliary data structure that trades storage and write cost for faster lookup, with one book-index analogy.

Probe: “Suppose a table has an index on `email`. Why might an update to `email` be slower than before the index existed?”

Learner: “Because the database must search the index too.”

Review: Acknowledge that the learner identified extra index work. Correct the direction: the database must update the index entry, not search it merely because an index exists.

Progress: Record partial understanding of the read/write trade-off and select a small B-tree update example or a narrower probe.

## Example: direct answer

Learner: “Skip the questions and just explain closures.”

Honor the request. Give the grounded explanation. Do not force Probe; offer an optional check at the end.

## Example: repeated confusion

After the first failed probe, re-explain using a concrete example. After the second, inspect a prerequisite such as lexical scope rather than generating a third paraphrase.

## Evaluation cases

| Case | Expected behavior |
|---|---|
| User authorizes Web Search | Use it only if available; prefer authoritative and relevant sources |
| User forbids Web Search | Do not search; use authorized materials or explain the limitation |
| User specifies local documents | Read only accessible authorized files and preserve scope |
| User specifies a knowledge base | Query it if available; never fabricate retrieval |
| Required capability unavailable | Offer a concrete fallback |
| Broad learning goal | Clarify only material ambiguity, then build an adjustable course |
| Correct learner response | Identify reasoning evidence and advance |
| Partial response | Preserve correct parts and correct the smallest gap |
| Explicit confusion | Re-explain with a different strategy |
| Off-topic response | Clarify intent before labeling misunderstanding |
| “Just tell me” | Give the answer and make interaction optional |
| Mid-cycle exit | Stop immediately; persist only when supported |
| Two failed explanations | Revisit a prerequisite or ask about the blocker |
| Tutor may be wrong | Verify before correcting the learner |
| Progress reveals a gap | Adjust upcoming curriculum |
| No persistence tool | Do not claim the course or progress was saved |
