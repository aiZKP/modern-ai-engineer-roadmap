# Deep Dive: Zero Knowledge Fundamentals

## Mental Model

Zero Knowledge Fundamentals is the working skill inside ZK and Verifiable AI that helps you build the stage artifact, A threat model, red-team report, smart contract security lab, and tiny ZKML or verifiable computation demo, while collecting enough evidence to trust the result. Treat it as a small engineering contract: what enters, what changes, what leaves, how you know it worked, and how it can fail.

## Key Mechanisms

- Input: identify what raw information, code, data, prompt, model output, trace, or user signal Zero Knowledge Fundamentals consumes.
- Transformation: describe what changes between input and output in ZK and Verifiable AI.
- Contract: write the expected shape, constraints, and success criteria so another engineer can check it.
- Measurement: use circuit size, proving time, verification time, precision loss, and model limits as the first observable proof.
- Failure mode: record how Zero Knowledge Fundamentals can fail specifically in Security, Blockchain, ZKML, not only in theory.

## Domain Details

- Inference optimization starts with TTFT, TPOT, throughput, memory, and quality regression measurements.
- Prefill processes the input context; decode generates tokens autoregressively and is often memory-bandwidth sensitive.
- KV cache size grows with layers, hidden dimensions, context length, batch size, and precision.
- Quantization reduces memory and bandwidth but must be checked against task quality and structured-output validity.
- Hardware choices should follow a workload contract: context length, output length, concurrency, latency target, memory budget, and power limit.

## Detailed Explanation

Start with the user or engineering problem. In Security, Blockchain, ZKML, the learner is trying to produce this artifact: A threat model, red-team report, smart contract security lab, and tiny ZKML or verifiable computation demo. Zero Knowledge Fundamentals is one piece of that artifact. It should not be studied as an isolated vocabulary item; it should be tied to code, data, diagrams, tests, metrics, or operational behavior.

A useful way to reason about Zero Knowledge Fundamentals is to ask four questions. First, what does it receive as input? Second, what assumptions does it make? Third, what output or decision does it create? Fourth, what would make that output untrustworthy? These questions keep the topic practical even when the surrounding AI field feels noisy.

The implementation should begin small. If Zero Knowledge Fundamentals involves code, write the smallest script, notebook cell, route, prompt, schema, or benchmark that exposes the behavior. If it involves design, write a one-page plan with a diagram and at least one measurable acceptance criterion. If it involves security or evaluation, write a test case before building the mitigation.

The measurement is the part that turns learning into engineering. For this part, use: circuit size, proving time, verification time, precision loss, and model limits. The exact number does not need to be perfect at first. It needs to be honest, repeatable, and connected to a decision you would make next.

## Worked Example

Imagine you are building the stage artifact: A threat model, red-team report, smart contract security lab, and tiny ZKML or verifiable computation demo. For Zero Knowledge Fundamentals, start with the smallest useful slice. Write the input, the expected output, the boundary conditions, and one case that should fail. Then implement only enough to observe the behavior. If the result works once, do not move on yet. Run it against a slightly different input, measure it with circuit size, proving time, verification time, precision loss, and model limits, and add the result to your notes.

## Common Failure Modes

- The concept is described correctly, but no artifact proves it.
- The learner changes models, tools, or frameworks before measuring the current failure.
- The implementation works only on the happy path.
- The measurement is not connected to a decision.
- The failure mode is too vague to debug.

## What Good Looks Like

A strong learner can point to a small artifact, explain the tradeoff, show a measurement, and name the next improvement. For Zero Knowledge Fundamentals, that means the explanation is grounded in ZK and Verifiable AI and the stage artifact rather than floating as general AI vocabulary.

Return to [9.6.1 Zero Knowledge Fundamentals](<index.md>).
