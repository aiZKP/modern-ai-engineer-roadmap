# 4.3 Generation Controls

## Role at Stage 4: Large Language Models

Control probabilistic text generation and make outputs fit software contracts. This part is one capability inside the stage. It should leave behind an artifact, measurements, and a short explanation of failure modes.

## Explanation

This part has 5 sub-parts because the topic needs that many learning units to feel natural. Some stages have more parts and some have fewer; the structure follows the topic, not a fixed template.

## Generation Control Flow

This diagram shows a beginner-friendly order for applying common generation controls during one next-token step. Stop sequences, max tokens, and structured-output checks sit around the sampling loop because they decide whether to continue, stop, validate, retry, or reject the result.

<div class="roadmap-diagram roadmap-diagram--part" markdown="1">

```mermaid
%%{init: {"flowchart": {"htmlLabels": true, "nodeSpacing": 50, "rankSpacing": 70}, "themeVariables": {"fontSize": "14px"}} }%%
flowchart TD
A["Prompt + text generated so far<br/>+ optional JSON schema or format contract"] --> B["Model outputs raw logits<br/>z_i for every candidate token"]
B --> C["Count token history<br/>count_i and seen_i"]
C --> D["Frequency + presence penalties<br/>z_pen_i = z_i - frequency_penalty * count_i - presence_penalty * seen_i"]
D --> E["Temperature<br/>score_i = z_pen_i / temperature"]
E --> F["Softmax<br/>P_i = exp(score_i) / sum_j exp(score_j)"]
F --> G["Top-k filter<br/>keep the k highest probabilities"]
G --> H["Top-p filter<br/>keep the smallest sorted group whose total probability reaches p"]
H --> I["Structured-output constraint<br/>mask tokens that cannot continue valid JSON or schema<br/>(when constrained decoding is supported)"]
I --> J["Renormalize<br/>remaining probabilities add to 100%"]
J --> K["Sample one token"]
K --> L["Append token to output"]
L --> M{"Stop sequence matched?"}
M -- "yes" --> Z["Stop and return output<br/>usually without the stop sequence"]
M -- "no" --> N{"Max output tokens reached?"}
N -- "yes" --> Y["Stop with length limit<br/>output may be incomplete"]
N -- "no" --> O{"Structured output complete?"}
O -- "no" --> A
O -- "yes" --> P["Validate JSON/schema in code"]
P --> Q{"Valid?"}
Q -- "yes" --> Z
Q -- "no" --> R["Handle failure<br/>retry, repair, or reject"]
```

</div>

Exact order can vary by provider or inference library. Some systems apply top-k before top-p, some expose only a few controls, and some add controls such as repetition penalty or min-p. Structured-output implementations also differ: some constrain token choices during decoding, while others validate or repair after the text is complete.

Beginner model:

1. The model creates raw logits.
2. Frequency and presence penalties adjust logits for tokens already used.
3. Temperature reshapes the logits.
4. Softmax turns logits into probabilities.
5. Top-k and top-p remove candidate tokens.
6. Structured-output constraints can mask tokens that would break valid JSON or the schema.
7. The remaining probabilities are rescaled.
8. The model samples one token.
9. Stop sequences, max tokens, and structured-output completion checks decide whether to stop or continue.
10. Completed structured outputs should still be validated by code.

## Sub-Parts

| Sub-part folder | What it explains |
|---|---|
| [4.3.1 Logits and Softmax](<4.3.1 Logits and Softmax/index.md>) | Logits and Softmax is the working skill inside Generation Controls that helps you build the stage artifact, An LLM fundamentals notebook comparing models, tokenization, structured outputs, embeddings, costs, and failure cases, while collecting enough evidence to trust the result. |
| [4.3.2 Temperature Top-p and Top-k](<4.3.2 Temperature Top-p and Top-k/index.md>) | Temperature Top-p and Top-k is the working skill inside Generation Controls that helps you build the stage artifact, An LLM fundamentals notebook comparing models, tokenization, structured outputs, embeddings, costs, and failure cases, while collecting enough evidence to trust the result. |
| [4.3.3 Stop Sequences and Max Tokens](<4.3.3 Stop Sequences and Max Tokens/index.md>) | Stop Sequences and Max Tokens is the working skill inside Generation Controls that helps you build the stage artifact, An LLM fundamentals notebook comparing models, tokenization, structured outputs, embeddings, costs, and failure cases, while collecting enough evidence to trust the result. |
| [4.3.4 Structured Outputs and JSON Schemas](<4.3.4 Structured Outputs and JSON Schemas/index.md>) | Structured Outputs and JSON Schemas is the working skill inside Generation Controls that helps you build the stage artifact, An LLM fundamentals notebook comparing models, tokenization, structured outputs, embeddings, costs, and failure cases, while collecting enough evidence to trust the result. |
| [4.3.5 Frequency and Presence Penalties](<4.3.5 Frequency and Presence Penalties/index.md>) | Frequency and Presence Penalties is the working skill inside Generation Controls that helps you build the stage artifact, An LLM fundamentals notebook comparing models, tokenization, structured outputs, embeddings, costs, and failure cases, while collecting enough evidence to trust the result. |

## What a Person Who Masters This Part Can Do

- Explain how Generation Controls supports an llm fundamentals notebook comparing models, tokenization, structured outputs, embeddings, costs, and failure cases..
- Build and inspect this artifact: Compare repeated generations across decoding settings.
- Measure progress with: Track variation, validity, latency, and quality.
- Debug at least one failure mode before moving to the next part.

## Build and Measure

**Build:** Compare repeated generations across decoding settings.

**Measure:** Track variation, validity, latency, and quality.

## Tests

Take one 30-question exam after studying this part. It opens in a new browser tab so the study page stays available.

<div class="exam-actions exam-actions--single">
  <a href="test/exam.html" target="_blank" rel="noopener">Open Part Exam</a>
</div>

## Back to Stage

Return to [Stage 4: Large Language Models](<../index.md>).
