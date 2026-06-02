Using examples in a prompt is one of the most powerful ways to improve an LLM's output. This technique is often called in-context learning or few-shot prompting.

The basic idea is:

Instead of only telling the model what to do, you also show it examples of the desired input and output.

The model learns the pattern from the examples and tries to continue it.

Why Examples Help

Suppose you ask:

Prompt:

Translate English to French:

Hello

The model will likely respond correctly.

But for more complex tasks, instructions alone may be ambiguous.

For example:

Extract the important information from this text.

What counts as "important"?

Names?
Dates?
Locations?
Summary?

The model has to guess.

Instead, provide examples:

Input:
John visited Paris on May 5.

Output:
Name: John
Location: Paris
Date: May 5

Input:
Sarah traveled to Tokyo on June 10.

Output:

The model now understands the pattern much more clearly.

Types of Prompting
1. Zero-Shot Prompting

No examples.

Classify sentiment:

I love this movie.

Output:

Positive

The model relies only on its training.

2. One-Shot Prompting

One example.

Review: The food was amazing.
Sentiment: Positive

Review: The service was terrible.
Sentiment:

Output:

Negative

One example demonstrates the task.

3. Few-Shot Prompting

Several examples.

Review: Great product.
Sentiment: Positive

Review: Worst purchase ever.
Sentiment: Negative

Review: I am very happy.
Sentiment: Positive

Review: I want a refund.
Sentiment:

Output:

Negative

This is often the most effective approach.

Example for Coding

Without examples:

Write a Python function that adds two numbers.

Usually works.

But suppose you want a specific style:

Example:

Input:
Multiply two numbers

Output:
def multiply(a: int, b: int) -> int:
    return a * b

Now:

Input:
Add two numbers

Output:

The model is likely to follow:

def add(a: int, b: int) -> int:
    return a + b

Notice it copied:

type hints
formatting
naming conventions
Example for Data Extraction

Suppose you're processing logs.

Prompt:

Example:

Text:
User Ryan logged in at 10:30 AM

JSON:
{
  "user": "Ryan",
  "action": "logged in",
  "time": "10:30 AM"
}

Text:
User Alice logged out at 2:15 PM

JSON:

Output:

{
  "user": "Alice",
  "action": "logged out",
  "time": "2:15 PM"
}

The example teaches the desired structure.

Example for Writing Style

You can teach tone.

Prompt:

Example:

Input:
New feature added

Output:
We're excited to announce a new feature that makes your workflow faster and easier.

Now:

Input:
Bug fixed

Output:

The model mimics the style:

We're happy to share that we've resolved a bug to provide a smoother experience.
Example for AI Agents

Suppose you're building an AI agent.

Without examples:

Decide which tool to use.

The model may behave inconsistently.

With examples:

Question: What's the weather in London?
Action: weather_tool

Question: Calculate 45 * 89
Action: calculator_tool

Question: Who founded Microsoft?
Action:

Output:

search_tool

Examples help the model learn decision-making patterns.

Good Example Design

A strong example should be:

1. Representative

Show realistic cases.

Good:

Customer asks for refund.

Bad:

Customer asks about flying dragons.
2. Consistent

Use the same format every time.

Good:

Input:
...

Output:
...

Bad:

Question:
...

Result:
...

Answer:
...

Mixed formats confuse the model.

3. Diverse

Cover different situations.

For sentiment classification:

Positive
Negative
Neutral

instead of only positive examples.

4. High Quality

Examples become the model's temporary "training data."

Poor examples produce poor outputs.

How Many Examples Should You Use?

Typical guideline:

Number	Name
0	Zero-shot
1	One-shot
2–10	Few-shot
10+	Large context learning

More examples often improve performance, but:

increase token usage
increase cost
may slow inference

Quality matters more than quantity.

Common Mistakes
Too Many Examples
100 examples...

Problems:

expensive
slow
may exceed context limits
Contradictory Examples

Bad:

Happy -> Positive
Happy -> Negative

The model becomes confused.

Different Formats

Bad:

Example 1: JSON
Example 2: Table
Example 3: Bullet list

Consistency is important.

Real-World Prompt Template

A professional prompt often looks like:

You are an expert data extractor.

Task:
Extract customer information.

Examples:

Input:
John Smith, age 30, lives in New York

Output:
{
  "name": "John Smith",
  "age": 30,
  "city": "New York"
}

Input:
Sarah Brown, age 25, lives in Boston

Output:
{
  "name": "Sarah Brown",
  "age": 25,
  "city": "Boston"
}

Now process:

Input:
Michael Davis, age 40, lives in Chicago

Output:

This combines:

Role instruction
Task description
Examples
Actual input

This pattern is widely used in production AI systems because examples often improve reliability more than simply writing longer instructions.