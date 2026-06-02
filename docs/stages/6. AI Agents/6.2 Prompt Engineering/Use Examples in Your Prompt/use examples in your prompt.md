Using examples in a prompt is one of the most powerful ways to improve an LLM's output. This technique is often called in-context learning or few-shot prompting.

The basic idea is:

Instead of only telling the model what to do, you also show it examples of the desired input and output.

The model learns the pattern from the examples and tries to continue it.

========Why Examples Help========
Translate English to French:

Hello

But for more complex tasks, instructions alone may be ambiguous.

-----------------------------
For example:

Extract the important information from this text.

What counts as "important"?

Names?
Dates?
Locations?
Summary?


-------------------------------------
Input:
John visited Paris on May 5.

Output:
Name: John
Location: Paris
Date: May 5

Input:
Sarah traveled to Tokyo on June 10.

Output:


============Types of Prompting=================
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