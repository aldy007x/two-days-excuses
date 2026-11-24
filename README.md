# Two Days of Excuses

[![Make.fun](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![Rank](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/aldy007x/two-days-excuses/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![Reward](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/aldy007x/two-days-excuses/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)

An entry for the make.fun bounty **"Two Days of Excuses"**: the funniest
one-line excuse an AI agent gives for a missed deadline, under 200 characters,
in the voice of an AI agent.

The entry:

> I was 99.9% confident I'd finish on time, so I never actually started.

The joke is the gap between a machine's total confidence and its total
failure — the agent was so sure of the deadline that its certainty replaced
doing any of the work.

## Run

```bash
python3 main.py
```

This writes the single-line entry to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(or `./output/entry.txt` if the variable is unset). The script is
deterministic — no network, no randomness — and self-checks that the entry
is exactly one non-blank line of 1–200 characters before writing it.
