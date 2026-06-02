# Temperature, Top-p, Top-k

## Purpose

Sampling controls decide how an LLM chooses the next token. They do not change
what the model knows. They change how risky, focused, repetitive, creative, or
stable the model's next-token choices become.

For AI agents, this matters because every token can affect a plan, a tool call,
a JSON field, a memory update, or a final answer. A creative setting can help
with brainstorming, but the same setting can break a tool call.

## The Simple Mental Model

An LLM writes text one token at a time. At each step, it first gives every
possible next token a raw score called a logit. A logit is not a probability
yet. It is just the model's internal score for "how well this token fits here."

Imagine the prompt is:

```text
I want to eat a slice of
```

The model might create a tiny version of this logit list:

| Candidate token | Example logit | Beginner meaning |
|---|---:|---|
| pizza | 3.3 | strongest raw score |
| cake | 2.8 | also likely |
| apple | 1.7 | possible, but weaker |
| paper | 1.3 | strange, but not impossible |
| shampoo | 0.5 | very unlikely |

Then softmax turns those logits into probabilities:

| Candidate token | Logit | Probability after softmax | Visual |
|---|---:|---:|---|
| pizza | 3.3 | about 50% | ########## |
| cake | 2.8 | about 30% | ###### |
| apple | 1.7 | about 10% | ## |
| paper | 1.3 | about 7% | # |
| shampoo | 0.5 | about 3% | # |

The actual model has a huge vocabulary, not just five tokens, but this tiny
table shows the core idea: logits become probabilities, and then the model
samples from those probabilities.

Sampling controls edit the logits and probability list before the model chooses
one token.

<div class="sampling-flow" role="img" aria-label="How sampling controls edit the next-token candidate list before the model chooses one token.">
  <div class="sampling-flow__step">
    <span class="sampling-flow__number">1</span>
    <strong class="sampling-flow__title">Prompt text</strong>
    <span class="sampling-flow__text">The model reads the current conversation and the unfinished answer.</span>
  </div>
  <div class="sampling-flow__arrow" aria-hidden="true">&darr;</div>
  <div class="sampling-flow__step">
    <span class="sampling-flow__number">2</span>
    <strong class="sampling-flow__title">Neural network</strong>
    <span class="sampling-flow__text">The model processes the text through its learned weights.</span>
  </div>
  <div class="sampling-flow__arrow" aria-hidden="true">&darr;</div>
  <div class="sampling-flow__step">
    <span class="sampling-flow__number">3</span>
    <strong class="sampling-flow__title">Raw scores, called logits</strong>
    <span class="sampling-flow__text">Every possible next token gets a raw score before it becomes a probability.</span>
  </div>
  <div class="sampling-flow__arrow" aria-hidden="true">&darr;</div>
  <div class="sampling-flow__step sampling-flow__step--highlight">
    <span class="sampling-flow__number">4</span>
    <strong class="sampling-flow__title">Temperature reshapes scores</strong>
    <span class="sampling-flow__text">Low temperature sharpens the list. High temperature flattens it.</span>
  </div>
  <div class="sampling-flow__arrow" aria-hidden="true">&darr;</div>
  <div class="sampling-flow__step">
    <span class="sampling-flow__number">5</span>
    <strong class="sampling-flow__title">Softmax makes probabilities</strong>
    <span class="sampling-flow__text">Scores become percentages that add up to 100%.</span>
  </div>
  <div class="sampling-flow__arrow" aria-hidden="true">&darr;</div>
  <div class="sampling-flow__step sampling-flow__step--highlight">
    <span class="sampling-flow__number">6</span>
    <strong class="sampling-flow__title">Top-p and top-k filter choices</strong>
    <span class="sampling-flow__text">Top-p cuts by total probability. Top-k cuts by number of candidates.</span>
  </div>
  <div class="sampling-flow__arrow" aria-hidden="true">&darr;</div>
  <div class="sampling-flow__step">
    <span class="sampling-flow__number">7</span>
    <strong class="sampling-flow__title">Rescale remaining probabilities</strong>
    <span class="sampling-flow__text">The kept candidates are stretched back to a 100% total.</span>
  </div>
  <div class="sampling-flow__arrow" aria-hidden="true">&darr;</div>
  <div class="sampling-flow__step">
    <span class="sampling-flow__number">8</span>
    <strong class="sampling-flow__title">Sample one token, then repeat</strong>
    <span class="sampling-flow__text">The selected token is added to the answer, and the process starts again.</span>
  </div>
</div>

Exact order can vary by provider or library, but this diagram is a useful
beginner model: temperature reshapes logits before softmax, while top-p and
top-k cut the probability list after softmax.

## Quick Comparison

| Control | Question it answers | What lower values do | What higher values do |
|---|---|---|---|
| `temperature` | How strongly should high logits win? | More predictable, focused, repetitive | More varied, creative, risky |
| `top_p` | How much total probability mass should stay available? | Keeps only the safest high-probability group | Allows a wider group of choices |
| `top_k` | How many candidate tokens should stay available? | Keeps only a small fixed number of choices | Allows more ranked choices |

## Temperature

Temperature changes how strongly the model prefers the most likely token.

Think of it like a creativity slider:

- `temperature = 0` or near `0`: the model strongly prefers the most likely
  token. This is useful for tool calls, structured output, math, code, and
  factual tasks.
- `temperature = 0.3` to `0.7`: the model can vary its wording while usually
  staying on track.
- `temperature = 0.8` to `1.0+`: the model explores less likely tokens. This
  can help creative writing and brainstorming, but it can also increase errors,
  strange wording, or format drift.

### How Temperature Changes Scores

The model first produces raw scores called logits. Temperature divides those
raw scores before probabilities are calculated:

```text
adjusted_score = logit / temperature
```

At exactly `temperature = 0`, providers usually use greedy decoding or a
near-greedy mode instead of literally dividing by zero.

Low temperature makes the biggest scores dominate. High temperature makes the
scores closer together.

Using the earlier logits:

| Candidate token | Original logit | Adjusted logit at `temperature = 0.2` | Adjusted logit at `temperature = 2.0` |
|---|---:|---:|---:|
| pizza | 3.3 | 16.5 | 1.65 |
| cake | 2.8 | 14.0 | 1.40 |
| apple | 1.7 | 8.5 | 0.85 |
| paper | 1.3 | 6.5 | 0.65 |
| shampoo | 0.5 | 2.5 | 0.25 |

After softmax, those adjusted logits become probabilities:

| Candidate token | Normal, `temperature = 1.0` | Low, `temperature = 0.2` | High, `temperature = 2.0` |
|---|---:|---:|---:|
| pizza | about 50% | about 92% | about 35% |
| cake | about 30% | about 8% | about 27% |
| apple | about 10% | near 0% | about 16% |
| paper | about 7% | near 0% | about 13% |
| shampoo | about 3% | near 0% | about 9% |

Low temperature is like telling the model: "Pick the obvious answer." High
temperature is like telling it: "Let unusual options compete."

### Same Prompt, Different Temperature

Prompt:

```text
Write the first sentence of a story about a dragon.
```

| Setting | Example output | Why it happens |
|---|---|---|
| Low, `0.2` | "Once upon a time, a large green dragon lived in a dark cave on top of a mountain." | Safe, common, predictable story words win. |
| Medium, `0.5` | "Deep inside the Whispering Mountains, an ancient dragon guarded a treasure made of glowing blue crystals." | The model still stays normal, but adds more color. |
| High, `1.0` | "Barnaby was a terrible dragon because he sneezed soap bubbles instead of fire." | Less likely ideas get a real chance, so the result becomes surprising. |

## Top-p

Top-p is also called nucleus sampling. It keeps the smallest group of likely
tokens whose total probability reaches the chosen `p` value.

If `top_p = 0.80`, the model starts from the most likely token, adds
probabilities from top to bottom, and stops when the running total reaches
`80%`.

Using the same list:

| Candidate token | Probability | Running total | Keep with `top_p = 0.80`? |
|---|---:|---:|---|
| pizza | 50% | 50% | yes |
| cake | 30% | 80% | yes |
| apple | 10% | 90% | no |
| paper | 7% | 97% | no |
| shampoo | 3% | 100% | no |

Now the model can only choose between `pizza` and `cake`. The other tokens are
removed for this step.

### Rescaling After Top-p

After filtering, the kept probabilities must add back up to `100%`.

| Candidate token | Before top-p | After `top_p = 0.80` |
|---|---:|---:|
| pizza | 50% | 62.5% |
| cake | 30% | 37.5% |
| apple | 10% | 0% |
| paper | 7% | 0% |
| shampoo | 3% | 0% |

The model then samples from only the remaining candidates.

### Why Top-p Is Dynamic

Top-p adapts to the model's confidence.

If the model is very sure:

| Candidate token | Probability |
|---|---:|
| spell | 97% |
| wand | 1% |
| potion | 1% |
| table | 1% |

A `top_p` value like `0.90` keeps only `spell`.

If the model is unsure:

| Candidate token | Probability |
|---|---:|
| book | 12% |
| shirt | 11% |
| game | 10% |
| apple | 10% |
| bag | 9% |
| many others | 48% |

The same `top_p = 0.90` keeps many more options. This is why top-p can feel
more natural than a fixed cutoff.

## Top-k

Top-k keeps only the top `k` candidate tokens by rank. It does not care how
much probability they contain.

If `top_k = 3`, the model keeps exactly the three highest-ranked candidates:

| Candidate token | Probability | Rank | Keep with `top_k = 3`? |
|---|---:|---:|---|
| pizza | 50% | 1 | yes |
| cake | 30% | 2 | yes |
| apple | 12% | 3 | yes |
| burger | 5% | 4 | no |
| socks | 3% | 5 | no |

After filtering, the probabilities are rescaled:

| Candidate token | Before top-k | After `top_k = 3` |
|---|---:|---:|
| pizza | 50% | 54.3% |
| cake | 30% | 32.6% |
| apple | 12% | 13.1% |
| burger | 5% | 0% |
| socks | 3% | 0% |

### The Top-k Weakness

Top-k is simple, but it is blind to confidence.

If the model is very sure, `top_k = 3` is usually fine:

| Candidate token | Probability |
|---|---:|
| spell | 99% |
| wand | 0.5% |
| potion | 0.3% |
| table | 0.2% |

But if the model is confused, a fixed `top_k = 3` can cut away options that are
almost equally good:

| Candidate token | Probability |
|---|---:|
| car | 3% |
| book | 3% |
| shirt | 3% |
| dog | 3% |
| apple | 3% |
| game | 3% |

Here, keeping only three candidates is arbitrary. Top-p often handles this
kind of uncertainty better because it expands the candidate set when many
tokens have similar probability.

## Should You Change Them Together?

For beginners, change one control at a time. Otherwise, you will not know which
control caused the behavior change.

A practical rule:

- If you are experimenting with `temperature`, keep `top_p` high, such as
  `1.0`, and avoid changing `top_k`.
- If you are experimenting with `top_p`, keep `temperature` moderate, such as
  `0.7` to `1.0`.
- If you use a local model that exposes `top_k`, start with a common value such
  as `40` or `50`, then test the result.

Some APIs expose only temperature and top-p. Some local inference engines expose
temperature, top-p, top-k, min-p, repetition penalty, and more. Treat every
setting as something to test, not something to trust blindly.

## Agent Settings Guide

| Agent job | Suggested starting point | Why |
|---|---|---|
| Tool call arguments | `temperature: 0` to `0.2`, `top_p: 1.0` | Tool calls need stable, parseable fields. |
| JSON or structured output | `temperature: 0` to `0.2` | Creativity can break schemas. |
| Math or code reasoning | `temperature: 0` to `0.3` | You want fewer surprising word choices. |
| Customer support | `temperature: 0.2` to `0.5` | Polite and consistent, but not robotic. |
| Search query rewriting | `temperature: 0` to `0.4` | Query expansion needs focus. |
| Brainstorming | `temperature: 0.7` to `1.0`, `top_p: 0.9` | More variety is useful. |
| Story writing | `temperature: 0.8+`, `top_p: 0.9` to `1.0` | Unusual wording can be a feature. |

In agent systems, the safest pattern is often to use different settings for
different steps:

```text
planner step:      low or medium temperature
tool-call step:    low temperature
creative draft:    higher temperature
final answer:      medium temperature
```

## Example: Same Question, Different Settings

Prompt:

```text
Do you know who the best football player is?
```

| Style | Settings | Example behavior |
|---|---|---|
| Fact checker | `temperature = 0.1`, `top_p = 0.20` | Gives a safe answer naming widely discussed players such as Lionel Messi, Cristiano Ronaldo, Pele, and Diego Maradona. |
| Sports fan | `temperature = 0.7`, `top_p = 0.85` | Gives a more conversational answer and may compare playing styles or eras. |
| Broken radio | `temperature = 1.8`, `top_p = 1.0` | May drift into strange or useless text because almost everything is allowed and the model is encouraged to take risks. |

The key idea: top-p decides which choices are allowed, and temperature changes
how strongly the model prefers the safest choices among the allowed candidates.

## Common Mistakes

| Mistake | Why it hurts |
|---|---|
| Using high temperature for tool calls | The model may invent fields, change formats, or choose the wrong tool. |
| Lowering every setting at once | You cannot tell which setting fixed or harmed the output. |
| Treating `temperature = 0` as perfectly deterministic | Some systems can still vary because of infrastructure, model routing, floating-point behavior, or provider settings. |
| Using one setting for the whole agent | Planning, tool use, writing, and summarizing often need different behavior. |
| Ignoring evaluation | A setting that feels good on one prompt may fail on edge cases. |

## Mini Lab

Use one prompt and run it several times with different settings.

Prompt:

```text
Write a short answer explaining why an AI agent should validate tool results.
```

Test these settings:

| Run | Temperature | Top-p | Top-k | What to observe |
|---|---:|---:|---:|---|
| A | 0.1 | 1.0 | off | Is it stable and precise? |
| B | 0.7 | 0.9 | off | Is it still accurate but more natural? |
| C | 1.0 | 1.0 | off | Does it become more creative or less focused? |
| D | 0.7 | 0.9 | 40 | Does top-k make the style more controlled? |

Record:

- Did the answer stay correct?
- Did the answer keep the requested format?
- Did the wording become more helpful or just more random?
- Would this setting be safe for tool calls?

## What to Remember

- Temperature changes the shape of the probability distribution.
- Top-p cuts by total probability mass.
- Top-k cuts by a fixed number of candidates.
- Lower settings are usually better for correctness, tools, schemas, and
  repeatability.
- Higher settings are usually better for brainstorming, creative writing, and
  exploration.
- AI agents often need multiple sampling profiles, not one global setting.

## Study Sources

- [Hands-On Large Language Models](https://github.com/HandsOnLLM/Hands-On-Large-Language-Models):
  Chapter 3 explains token sampling/decoding, and Chapter 6 shows prompt
  engineering examples with `temperature` and `top_p`.
- [LLM Engineers Handbook](https://github.com/PacktPublishing/LLM-Engineers-Handbook):
  model evaluation and inference examples use sampling parameters such as
  `temperature` and `top_p`.
- [Building LLM Applications](https://github.com/roberto-inf/building-llm-applications):
  agent/tool examples use low temperature for stable tool-aware behavior.
- [AI Engineering](https://github.com/chiphuyen/aie-book):
  sampling is treated as the reason generative models are powerful for creative
  work but also inconsistent, which is why evaluation matters.
