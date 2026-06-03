# 4.3.5 Frequency and Presence Penalties

## Why This Sub-Part Matters

Frequency and Presence Penalties is the working skill inside Generation Controls that helps you build the stage artifact, An LLM fundamentals notebook comparing models, tokenization, structured outputs, embeddings, costs, and failure cases, while collecting enough evidence to trust the result. A sub-part is now a folder so longer topics can grow without forcing everything into one huge page.

## Study Pages

| Page | Purpose |
|---|---|
| [Deep Dive](<deep-dive.md>) | Full explanation, mechanisms, examples, and failure modes. |
| [Examples and Practice](<examples-and-practice.md>) | Worked exercises, project drills, and self-check prompts. |

## Core Ideas

- Frequency penalty discourages tokens more strongly each time they repeat.
- Presence penalty nudges the model away from tokens that have already appeared at least once.
- Both penalties adjust logits before sampling, so they interact with temperature, top-p, and top-k.
- Use penalties to reduce loops or repetitive phrasing, not to guarantee factuality or structure.
- Measure repetition, validity, latency, and quality before deciding a penalty helped.

## How to Study It

1. Read this overview and write the concept in your own words.
2. Read the deep dive and identify the input, transformation, output, and failure mode.
3. Complete the examples and practice page.
4. Add one measurement using: Track variation, validity, latency, and quality.

## Completion Standard

- I can explain Frequency and Presence Penalties without naming a tool first.
- I can connect it to the stage artifact.
- I can show a small artifact, measurement, or test.
- I know how it fails and what I would inspect first.

Return to [4.3 Generation Controls](<../index.md>).
