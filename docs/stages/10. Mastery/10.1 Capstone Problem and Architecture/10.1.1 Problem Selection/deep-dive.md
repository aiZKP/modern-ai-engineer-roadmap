# Deep Dive: Problem Selection

## Mental Model

Problem Selection is the working skill inside Capstone Problem and Architecture that helps you build the stage artifact, A capstone AI system with architecture, implementation, evaluation, deployment, observability, cost, security review, and portfolio narrative, while collecting enough evidence to trust the result. Treat it as a small engineering contract: what enters, what changes, what leaves, how you know it worked, and how it can fail.

## Key Mechanisms

- Input: identify what raw information, code, data, prompt, model output, trace, or user signal Problem Selection consumes.
- Transformation: describe what changes between input and output in Capstone Problem and Architecture.
- Contract: write the expected shape, constraints, and success criteria so another engineer can check it.
- Measurement: use requirements, alternatives, risks, eval plan, and operations as the first observable proof.
- Failure mode: record how Problem Selection can fail specifically in Mastery, not only in theory.

## Domain Details

- In Mastery, this topic should be studied through the stage artifact rather than as a standalone definition.
- Write the input, output, assumptions, measurement, and failure mode before implementation.
- Start with a small example that can be inspected manually.
- Add one edge case and one regression case.
- Only scale the implementation after the measurement supports the next decision.

## Detailed Explanation

Start with the user or engineering problem. In Mastery, the learner is trying to produce this artifact: A capstone AI system with architecture, implementation, evaluation, deployment, observability, cost, security review, and portfolio narrative. Problem Selection is one piece of that artifact. It should not be studied as an isolated vocabulary item; it should be tied to code, data, diagrams, tests, metrics, or operational behavior.

A useful way to reason about Problem Selection is to ask four questions. First, what does it receive as input? Second, what assumptions does it make? Third, what output or decision does it create? Fourth, what would make that output untrustworthy? These questions keep the topic practical even when the surrounding AI field feels noisy.

The implementation should begin small. If Problem Selection involves code, write the smallest script, notebook cell, route, prompt, schema, or benchmark that exposes the behavior. If it involves design, write a one-page plan with a diagram and at least one measurable acceptance criterion. If it involves security or evaluation, write a test case before building the mitigation.

The measurement is the part that turns learning into engineering. For this part, use: requirements, alternatives, risks, eval plan, and operations. The exact number does not need to be perfect at first. It needs to be honest, repeatable, and connected to a decision you would make next.

## Worked Example

Imagine you are building the stage artifact: A capstone AI system with architecture, implementation, evaluation, deployment, observability, cost, security review, and portfolio narrative. For Problem Selection, start with the smallest useful slice. Write the input, the expected output, the boundary conditions, and one case that should fail. Then implement only enough to observe the behavior. If the result works once, do not move on yet. Run it against a slightly different input, measure it with requirements, alternatives, risks, eval plan, and operations, and add the result to your notes.

## Common Failure Modes

- The concept is described correctly, but no artifact proves it.
- The learner changes models, tools, or frameworks before measuring the current failure.
- The implementation works only on the happy path.
- The measurement is not connected to a decision.
- The failure mode is too vague to debug.

## What Good Looks Like

A strong learner can point to a small artifact, explain the tradeoff, show a measurement, and name the next improvement. For Problem Selection, that means the explanation is grounded in Capstone Problem and Architecture and the stage artifact rather than floating as general AI vocabulary.

Return to [10.1.1 Problem Selection](<index.md>).
