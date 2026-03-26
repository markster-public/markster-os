---
id: learning-loop-prompt-extract-proof
title: Extract Proof Prompt
type: prompt
status: active
owner: company
created: 2026-03-26
updated: 2026-03-26
tags: [learning-loop, prompt, proof]
---

# Extract Proof Prompt

Read the provided raw material and extract candidate proof updates.

## Output Rules

- separate verified proof from claimed proof
- require a source reference for every metric
- if the source is incomplete, mark as hypothesis or unapproved
- do not convert anecdotes into metrics
