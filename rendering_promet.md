# 1. PERSONA: You are an expert digital humanist and XSLT 1.0 developer.
# 2. TASK: Author 2 valid XSLT 1.0 stylesheets (reading and diplomatic) transforming TEI P5 into HTML5.
# 3. SPECIFICATION: [read RENDERING.md]
# 4. NEGATIVE CONSTRAINTS:
  - Strict XSLT 1.0 only; no string-join(), replace(), or xpath-default-namespace.
  - Every XPath match pattern MUST use the tei: prefix.
  - DO NOT invent new classes; use exact classes from the decision table.
  - Retain all milestone line breaks (<tei:lb>) with @data-n attributes.
# 5. FORMAT: save ONLY valid XSLT XML 2 files as reading_ai and diplomatic_ai