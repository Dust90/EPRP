# Capability routing

Use this reference when deciding how to obtain material for curriculum construction or a lesson.

## Governing rule

The Skill identifies information needs. The host Agent exposes and executes real capabilities. Never encode a dependency on a specific vendor, API, MCP server, vector database, file system, or search implementation.

Apply this priority:

1. explicit user source instructions and prohibitions
2. safety, privacy, authorization, and host policy
3. capabilities actually available to the Agent
4. reliability and coverage needed for the learning goal
5. least-expansive useful default

## Capability classes

Treat tool names as host-specific mappings to these abstract capabilities:

- `web_search`: find current or public material
- `web_read`: open and read selected public pages
- `local_file_read`: read user-authorized local or uploaded files
- `document_parse`: extract PDF, office document, image, or structured-document content
- `knowledge_base_search`: retrieve from a user-specified corpus
- `citation_resolution`: preserve links, document IDs, pages, sections, or result provenance
- `code_execution`: verify formulas, code, calculations, or data
- `persistent_learning_state`: save curriculum and learning evidence

Do not require these names to exist literally.

## Interpret user instructions

| User instruction | Route |
|---|---|
| “Search the web and build a course” | Use Web Search and Web Read if available |
| “Use only these documents” | Use authorized file/document capabilities; prohibit Web Search |
| “Search our knowledge base” | Use the specified knowledge-base capability |
| “Use my documents and fill gaps from the web” | Read documents first, then search only identified gaps |
| “Do not go online” | Prohibit Web Search and Web Read |
| No source instruction | Choose the least-expansive available route that can build a reliable course |

Do not silently broaden “use this source” into permission to access unrelated private or public sources.

## Decide whether automatic Web Search is useful

When not prohibited, use Web Search if one or more apply:

- the user explicitly requests it
- the topic, policy, software, market, science, or practice may have changed
- authoritative sources are needed for reliable teaching
- existing material cannot support the requested curriculum
- a source claim, citation, statistic, or tutor correction requires verification

Avoid Web Search when authorized material already satisfies the goal and search would not materially improve the course.

## Use local or uploaded documents

- Read only files the user identifies or places in scope.
- Confirm actual access; do not infer contents from filenames.
- Use parsing or OCR only when the host provides it.
- State missing pages, unreadable regions, unsupported formats, or extraction defects.
- When multiple documents are supplied, preserve provenance, duplication, and disagreement.

## Use a knowledge base

- Query only the corpus the user identifies or authorizes.
- Preserve result provenance exposed by the retrieval tool.
- Distinguish “no result” from “capability unavailable.”
- Do not fill a knowledge-base gap with model knowledge while presenting it as retrieved content.
- Ask before using public Web sources if the request implies an internal-only curriculum.

## Combine capabilities

Use a staged hybrid route, not an indiscriminate search:

1. inspect user-provided or designated material
2. identify curriculum or lesson coverage gaps
3. retrieve only what is needed to fill or verify those gaps
4. preserve the origin of each source
5. apply source grounding before teaching

## Handle unavailable capabilities

Offer a concrete fallback:

- no Web Search → use supplied material or create a provisional course from existing context
- no file reader → ask for an upload, pasted excerpt, or accessible link
- no PDF parser/OCR → ask for extracted text or clearer pages
- no knowledge-base access → ask for exported material or permission to use public sources
- no persistence → keep progress in the current conversation and say it is not durably saved

Do not repeatedly ask for a capability the host cannot provide.

## Record the route

When structured state is supported, record:

```json
{
  "source_instruction": "Use internal knowledge base; no public web",
  "allowed_capabilities": ["knowledge_base_search"],
  "prohibited_capabilities": ["web_search", "web_read"],
  "capabilities_used": ["knowledge_base_search"],
  "limitations": ["Knowledge base covers onboarding but not advanced incident response"]
}
```

Expose this record only when it helps the learner understand coverage, provenance, or a limitation.
