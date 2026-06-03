# Examples and Practice: Frequency and Presence Penalties

## Worked Practice

1. Write one paragraph explaining the difference between frequency penalty and presence penalty.
2. Draw a small diagram that shows token history, logit adjustment, sampling, and output.
3. Run or outline three generations for the same prompt: no penalties, modest frequency penalty, and modest presence penalty.
4. Measure it with: Track variation, validity, latency, and quality.
5. Add one failure case where a penalty makes the answer worse.

## Mini Project Drill

Create a file named `notes/frequency-and-presence-penalties.md` in your project workspace. Include:

- the prompt you tested
- the generation settings that stayed fixed
- the frequency penalty and presence penalty values you compared
- one example output for each setting
- duplicate phrase or n-gram observations
- schema validity or format validity, if relevant
- one decision you would make from the result

## Check Your Understanding

| Question | What a strong answer includes |
|---|---|
| What does frequency penalty do? | It penalizes repeated tokens more as they appear more often, which can reduce loops and repeated wording. |
| What does presence penalty do? | It penalizes tokens after they have appeared once, which can push the model toward new tokens or ideas. |
| When can penalties hurt? | They can avoid required terms, damage exact formats, weaken code, or make structured output less valid. |
| How would you test them? | Keep the prompt and other decoding settings fixed, compare repeated runs, and measure repetition, validity, latency, and quality. |

## Stretch Exercise

Repeat the drill on a structured-output prompt. Record whether penalties improve variety or damage contract validity.

Return to [4.3.5 Frequency and Presence Penalties](<index.md>).
