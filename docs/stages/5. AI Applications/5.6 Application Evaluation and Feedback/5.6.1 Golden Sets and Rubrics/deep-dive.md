# Deep Dive: Golden Sets and Rubrics

## Mental Model

Golden Sets and Rubrics is the working skill inside Application Evaluation and Feedback that helps you build the stage artifact, An evaluated RAG or AI workflow application with documents, prompts, tests, logs, latency, cost, and failure analysis, while collecting enough evidence to trust the result. Treat it as a small engineering contract: what enters, what changes, what leaves, how you know it worked, and how it can fail.

## Key Mechanisms

- Input: identify what raw information, code, data, prompt, model output, trace, or user signal Golden Sets and Rubrics consumes.
- Transformation: describe what changes between input and output in Application Evaluation and Feedback.
- Contract: write the expected shape, constraints, and success criteria so another engineer can check it.
- Measurement: use pass rate, judge agreement, human review notes, and feedback categories as the first observable proof.
- Failure mode: record how Golden Sets and Rubrics can fail specifically in AI Applications, not only in theory.

## Domain Details

- Evaluation starts by defining what good output means for the user and the workflow.
- Use exact checks whenever possible, rubrics when judgment is needed, and AI judges only with calibration examples and spot checks.
- Slice failures by source, task type, input length, user group, difficulty, or tool path to find actionable patterns.
- Regression tests protect existing behavior when prompts, models, data, or tools change.
- A metric should drive a decision: keep, roll back, investigate, route, retrain, or redesign.

## Detailed Explanation

Start with the user or engineering problem. In AI Applications, the learner is trying to produce this artifact: An evaluated RAG or AI workflow application with documents, prompts, tests, logs, latency, cost, and failure analysis. Golden Sets and Rubrics is one piece of that artifact. It should not be studied as an isolated vocabulary item; it should be tied to code, data, diagrams, tests, metrics, or operational behavior.

A useful way to reason about Golden Sets and Rubrics is to ask four questions. First, what does it receive as input? Second, what assumptions does it make? Third, what output or decision does it create? Fourth, what would make that output untrustworthy? These questions keep the topic practical even when the surrounding AI field feels noisy.

The implementation should begin small. If Golden Sets and Rubrics involves code, write the smallest script, notebook cell, route, prompt, schema, or benchmark that exposes the behavior. If it involves design, write a one-page plan with a diagram and at least one measurable acceptance criterion. If it involves security or evaluation, write a test case before building the mitigation.

The measurement is the part that turns learning into engineering. For this part, use: pass rate, judge agreement, human review notes, and feedback categories. The exact number does not need to be perfect at first. It needs to be honest, repeatable, and connected to a decision you would make next.

## Worked Example

Imagine you are building the stage artifact: An evaluated RAG or AI workflow application with documents, prompts, tests, logs, latency, cost, and failure analysis. For Golden Sets and Rubrics, start with the smallest useful slice. Write the input, the expected output, the boundary conditions, and one case that should fail. Then implement only enough to observe the behavior. If the result works once, do not move on yet. Run it against a slightly different input, measure it with pass rate, judge agreement, human review notes, and feedback categories, and add the result to your notes.

## Common Failure Modes

- The concept is described correctly, but no artifact proves it.
- The learner changes models, tools, or frameworks before measuring the current failure.
- The implementation works only on the happy path.
- The measurement is not connected to a decision.
- The failure mode is too vague to debug.

## What Good Looks Like

A strong learner can point to a small artifact, explain the tradeoff, show a measurement, and name the next improvement. For Golden Sets and Rubrics, that means the explanation is grounded in Application Evaluation and Feedback and the stage artifact rather than floating as general AI vocabulary.

Return to [5.6.1 Golden Sets and Rubrics](<index.md>).
