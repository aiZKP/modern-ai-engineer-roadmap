# Specify Length, Format, and Audience

## Summary

Length, format, and audience constraints turn a vague request into an output
contract. They tell the model how much to write, what shape the answer must
take, and who the answer is for.

Use these constraints when the response must be easy to read, compare, copy,
evaluate, or parse by software.

## Core Idea

A prompt should answer three output questions before the model starts writing:

| Constraint | Question it answers | Example instruction |
| --- | --- | --- |
| Length | How much detail is needed? | `Write about 120 words.` |
| Format | What structure should the answer follow? | `Return a markdown table with columns: Risk, Cause, Mitigation.` |
| Audience | Who needs to understand or use this? | `Write for a non-technical product manager.` |

If you omit these details, the model must guess. Guessing often produces
answers that are too long, too shallow, too technical, too casual, or difficult
to reuse.

## Make Constraints Testable

A constraint is specific when another person or program can check whether the
answer followed it.

| Vague instruction | Specific instruction | How to check it |
| --- | --- | --- |
| `Make it short.` | `Use exactly 5 bullets, each under 14 words.` | Count bullets and words |
| `Use a table.` | `Use columns: Term, Meaning, Example, Common mistake.` | Check column names and order |
| `Write for beginners.` | `Assume no Python or ML background; define every technical term once.` | Scan vocabulary and definitions |
| `Give JSON.` | `Return only valid JSON with keys: title, summary, risks.` | Parse JSON and check keys |
| `Be professional.` | `Use a neutral business tone; avoid jokes, slang, and emojis.` | Review tone rules |

Put these rules near the start or in a clearly labeled `Output requirements`
section. If the task is long, repeat the required output format immediately
before the model should answer.

## Specify Length

Length controls depth. A short answer is useful when the reader needs a quick
decision. A long answer is useful when the task needs explanation, evidence,
tradeoffs, or examples.

| Length instruction | Best for | Prompt example |
| --- | --- | --- |
| `One sentence` | Definitions, labels, quick checks | `Explain vector databases in one sentence.` |
| `3-5 bullets` | Scannable summaries | `Summarize the risks in 5 bullets.` |
| `About 100 words` | Short explanations | `Explain retrieval augmented generation in about 100 words.` |
| `300-500 words` | Brief articles or decision notes | `Write a 400-word overview for engineering managers.` |
| `Step-by-step` | Procedures, tutorials, debugging | `Explain how to deploy the model in 7 numbered steps.` |
| `No more than 2 pages` | Reports, memos, design notes | `Create a concise design memo, no more than 2 pages.` |

Prefer practical limits over vague phrases:

| Weak | Better |
| --- | --- |
| `Keep it short.` | `Use 5 bullets, max 12 words each.` |
| `Explain in detail.` | `Write 600-800 words with examples and tradeoffs.` |
| `Make it concise.` | `Use one paragraph under 90 words.` |

Length does not need to be exact for every task. For human reading, approximate
limits are usually enough. For UI copy, social posts, database fields, or
automation, use stricter limits.

### Specific Length Rules

Choose the length rule based on where the output will go.

| Output destination | Good length rule | Why |
| --- | --- | --- |
| Button or label | `2-4 words` | Fits UI constraints |
| Tooltip | `One sentence under 20 words` | Readable on hover |
| Executive summary | `3 bullets, max 20 words each` | Easy to scan |
| Study note | `150-250 words with one example` | Enough context without overload |
| Tutorial | `6-10 numbered steps` | Clear sequence |
| JSON field | `String under 120 characters` | Easier validation and storage |

Avoid exact word counts when meaning matters more than precision. Use ranges
such as `180-220 words` or structural limits such as `5 bullets`.

## Specify Format

Format controls how the answer is organized. Use it when the output must be
easy to skim, compare, validate, or pass into another tool.

The format of your prompt can make or break its effectiveness. It’s not just about what you ask, but how you ask it.

| Format | Use when | Example instruction |
| --- | --- | --- |
| Bullets | The reader needs quick takeaways | `Use 6 bullets, ordered by importance.` |
| Numbered list | Sequence matters | `Return the setup steps as a numbered list.` |
| Table | The reader must compare options | `Use a table with columns: Option, Cost, Risk, When to use.` |
| Markdown | The answer will become docs or notes | `Use markdown headings and fenced code blocks.` |
| JSON | Software must parse the result | `Return only valid JSON matching this schema.` |
| Email | The output must be sent to a person | `Write as a professional email with subject line.` |
| Checklist | The user must verify completion | `Return a checklist with pass/fail criteria.` |

### Types of Prompt Formats

- Question based prompts: These are straightforward and often begin with who, what, when, where, why, or how.
  Example: “What are the main challenges facing renewable energy adoption in 2026?”

- Instruction based prompts: These tell the AI exactly what you want it to do.
  Example: “Write a 500 word blog post about the benefits of meditation for stress relief.”

- Context based prompts: These provide background information before asking a question or giving an instruction.
  Example: “You are an expert in blockchain technology. Explain the concept of smart contracts to a beginner.”
- Role playing prompts: These ask the AI to assume a specific role or persona.
  Example: “As a financial advisor, provide advice on diversifying an investment portfolio in a volatile market.”
- Completion prompts: These provide the beginning of a sentence or paragraph for the AI to complete.
  Example: “The future of transportation in smart cities will be characterized by…”

### Format Recipes

Use a recipe when you need repeatable output.

| Task | Specific format recipe |
| --- | --- |
| Compare options | `Return a markdown table with columns: Option, Best for, Tradeoff, Recommendation.` |
| Explain a concept | `Use sections: Definition, Why it matters, Example, Common mistake.` |
| Summarize a source | `Use 4 bullets: main claim, evidence, limitation, action item.` |
| Write a how-to | `Use numbered steps. Each step must start with a verb.` |
| Extract data | `Return only JSON. No markdown, no comments, no trailing text.` |
| Review output | `Use sections: Findings, Risks, Missing information, Suggested fix.` |

## Specify Audience

Audience controls vocabulary, assumptions, examples, and level of detail. The
same topic should look different for a child, a new developer, a CTO, and a
domain expert.

Understanding your audience – both the AI model you’re prompting and the end users of the generated content – is crucial for effective prompt engineering

| Audience | What changes | Example direction |
| --- | --- | --- |
| Beginner | Define terms and avoid jargon | `Assume no prior AI knowledge.` |
| Student | Teach concepts and show examples | `Use simple examples and explain key terms.` |
| Developer | Include implementation details | `Mention APIs, failure modes, and code-level tradeoffs.` |
| Manager | Focus on decisions and risk | `Emphasize business impact, cost, and timeline.` |
| Executive | Be concise and outcome-oriented | `Use an executive summary with recommendations.` |
| Expert | Use precise terms and skip basics | `Assume familiarity with transformers and retrieval systems.` |
| Customer | Keep it practical and reassuring | `Avoid internal jargon and explain benefits clearly.` |

### Same Topic, Different Audience

Topic: `AI agents`

| Audience | Better prompt | Expected style |
| --- | --- | --- |
| High school student | `Explain AI agents to a high school student in 120 words using an everyday analogy.` | Simple, concrete, analogy-driven |
| Junior developer | `Explain AI agents to a junior Python developer in 5 bullets, including tools, memory, and control loops.` | Technical but beginner-friendly |
| CTO | `Summarize AI agent adoption risks for a CTO in a 1-page decision memo.` | Strategic, risk-aware, decision-focused |
| ML researcher | `Compare tool-using LLM agents with classical planning systems for an ML researcher.` | Dense, precise, assumes background knowledge |

### Specific Audience Profile

Instead of writing only `for beginners`, define the reader more precisely.

```text
Audience:
- Role: junior backend developer
- Prior knowledge: knows HTTP APIs and Python basics
- Unknown concepts: vector databases, embeddings, RAG
- Goal: decide what to learn next
- Tone: direct and practical
```

This tells the model which terms need definitions and which terms can be used
without explanation.

## Examples

### Example 1:Technical Writing for Developers

Prompt: “As an experienced software engineer, write a detailed tutorial on implementing a RESTful API using Node.js and Express. The tutorial should be 1500 words long and include code snippets, best practices, and common pitfalls to avoid. Your audience is junior developers with basic JavaScript knowledge.”

Analysis:

Format: Instruction with role playing element
Length: Long (provides specific word count and content requirements)
Audience: Clearly defined (junior developers with basic JavaScript knowledge)

### Example 2: Creative Writing for Children

Prompt: “Write a short, imaginative story about a friendly robot who learns the value of friendship. The story should be suitable for children aged 6-8 and no longer than 300 words. Include a moral lesson at the end.”

Analysis:

Format: Instruction based with specific creative elements
Length: Medium (word limit specified)
Audience: Clearly defined (children aged 6-8)

### Example 3: Market Analysis for Executives

Prompt: “You are a leading market analyst. Provide a concise summary of the major trends shaping the electric vehicle industry in 2026. Focus on technological advancements, market growth, and regulatory changes. Your analysis should be no more than 500 words and suitable for busy executives.”

Analysis:

Format: Role playing with specific instructions
Length: Medium to Long (word limit specified)
Audience: Clearly defined (busy executives)

## Combined Example

### Prompt

```text
You are helping a startup founder understand RAG.

Write for a non-technical founder who understands basic SaaS products but not
machine learning.

Length: 180-220 words.

Format:
1. One-sentence definition
2. Markdown table with columns: Benefit, Example, Risk
3. Three-bullet recommendation

Avoid equations and academic terminology.
```

### Why It Is Strong

| Part | What it controls |
| --- | --- |
| `non-technical founder` | Audience, vocabulary, examples |
| `180-220 words` | Depth and time-to-read |
| `definition + table + bullets` | Output structure |
| `Avoid equations...` | Style and exclusion rules |

## Citation, Refusal, and Escalation Formats

Some tasks need more than ordinary formatting. If the output can affect a
decision, tell the model how to cite uncertainty, refuse unsafe work, or
escalate missing information.

```text
Answer in this format:

Summary:
- 3 bullets maximum

Evidence:
- Cite each source with a link
- Mark unsupported claims as "uncertain"

If the request asks for illegal, unsafe, or private information:
- Refuse briefly
- Offer a safe alternative

If required information is missing:
- Ask up to 3 clarifying questions
```

This matters in AI agents because downstream tools may treat the model response
as an instruction. A predictable refusal or escalation format makes the agent
easier to audit.

## Common Mistakes

| Mistake | Result | Fix |
| --- | --- | --- |
| Asking for `a summary` without length | Output may be one sentence or several pages | Specify bullets, words, or sections |
| Asking for JSON plus explanation | Parser may fail on extra text | Say `Return only valid JSON` |
| Choosing a format after the task is complex | Important constraints may be ignored | Put output rules near the start |
| Ignoring audience | Tone and depth may miss the reader | State role, knowledge level, and goal |
| Overloading the prompt | The model may drop requirements | Split complex work into steps or schemas |

## Source Notes

This page synthesizes the provided study note and the Techlasi article on
format, length, and audience in prompt engineering:

- [Mastering Prompt Engineering: Format, Length, and Audience Examples](https://techlasi.com/savvy/mastering-prompt-engineering-format-length-and-audience-examples-for-2024/)
