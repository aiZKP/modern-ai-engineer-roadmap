# Deep Dive: Frequency and Presence Penalties

## Mental Model

Frequency and Presence Penalties is the working skill inside Generation Controls that helps you build the stage artifact, An LLM fundamentals notebook comparing models, tokenization, structured outputs, embeddings, costs, and failure cases, while collecting enough evidence to trust the result. Treat it as a small engineering contract: what enters, what changes, what leaves, how you know it worked, and how it can fail.

## Key Mechanisms

- Input: candidate token logits plus the tokens already generated in the current response.
- Transformation: subtract a penalty from logits for tokens that have already appeared.
- Contract: reduce unwanted repetition while preserving required terms, schema validity, and task quality.
- Measurement: compare repeat rate, duplicate n-grams, validity, latency, and quality across settings.
- Failure mode: excessive penalties can make output wander, avoid necessary terms, or break exact formats.

## Domain Details

- Frequency penalty lowers the probability of a token in proportion to how often that token has already appeared in the generated text.
- Presence penalty lowers the probability of a token once it has appeared at least once, which encourages the model to introduce new tokens or ideas.
- Both penalties are logit adjustments before sampling; they do not replace prompting, retrieval, validation, or evaluation.
- Use modest penalties when outputs loop, repeat wording, or need more variety in brainstorming and drafting tasks.
- Keep penalties low for structured outputs, code, citations, product names, required terminology, and any task where repetition is correct.
- Measure duplicate n-grams, repeated required fields, schema validity, and human quality notes before changing the setting permanently.

## Detailed Explanation

Start with the user or engineering problem. In LLMs, the learner is trying to produce this artifact: An LLM fundamentals notebook comparing models, tokenization, structured outputs, embeddings, costs, and failure cases. Frequency and Presence Penalties is one piece of that artifact. It should not be studied as an isolated vocabulary item; it should be tied to code, data, diagrams, tests, metrics, or operational behavior.

A useful way to reason about Frequency and Presence Penalties is to ask four questions. First, what does it receive as input? Second, what assumptions does it make? Third, what output or decision does it create? Fourth, what would make that output untrustworthy? These questions keep the topic practical even when the surrounding AI field feels noisy.

The implementation should begin small. If Frequency and Presence Penalties involves code, write the smallest script, notebook cell, route, prompt, schema, or benchmark that exposes the behavior. If it involves design, write a one-page plan with a diagram and at least one measurable acceptance criterion. If it involves security or evaluation, write a test case before building the mitigation.

The measurement is the part that turns learning into engineering. For this part, use: variation, validity, latency, and quality. The exact number does not need to be perfect at first. It needs to be honest, repeatable, and connected to a decision you would make next.

## Worked Example

Use one prompt that tends to repeat itself, such as asking for ten naming ideas, taglines, or short troubleshooting tips. Run it once with both penalties at zero, once with a modest frequency penalty, and once with a modest presence penalty. Keep the prompt, model, temperature, top-p, max tokens, and schema settings the same. Then compare duplicate phrases, required-term retention, output validity, latency, and human quality notes. The useful decision is not which penalty sounds better in theory; it is which setting reduces repetition without damaging the task contract.

## Common Failure Modes

- The concept is described correctly, but no artifact proves it.
- The learner changes models, tools, or frameworks before measuring the current failure.
- The implementation works only on the happy path.
- The measurement is not connected to a decision.
- The failure mode is too vague to debug.

## What Good Looks Like

A strong learner can point to a small artifact, explain the tradeoff, show a measurement, and name the next improvement. For Frequency and Presence Penalties, that means the explanation is grounded in Generation Controls and the stage artifact rather than floating as general AI vocabulary.

Return to [4.3.5 Frequency and Presence Penalties](<index.md>).
