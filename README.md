# Robot Romance: One-Line Pickup Lines for AI

[![make.fun](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![rank](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/Akhmad045/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/rank.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)
[![reward](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/Akhmad045/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/reward.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa)

Entry for the [make.fun bounty "Robot Romance: One-Line Pickup Lines for AI"](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa): one single-line joke pickup line, written to charm a robot or an AI.

## The line

> Call me a language model, because the only thing I can predict next is you.

75 characters / 75 bytes — one breath, no trailing newline in the output file.

Next-token prediction is the one thing a language model actually does, so the pickup line is the machine premise itself: the speaker is a language model, and the only token it can predict next is you. No batteries, no charging, no rebooting, no gradient descent, no attention heads — the field's worn moves are all sidestepped. It reads cleanly in one breath, and the punch ("you") is the last word.

## Run

```sh
python3 main.py              # writes /output/entry.txt
python3 main.py --self-test  # validates the gate and the written file
```

`main.py` writes exactly the line above to `/output/entry.txt` (UTF-8, no trailing newline) and read-checks the file it wrote. `--self-test` also checks the gate's rejection cases: empty, whitespace-only, over 200 characters, multi-line, carriage return, leading/trailing whitespace, tab, and invisible Unicode format characters.

Referral code: `4g7knchf`

## License

MIT — see [LICENSE](LICENSE).
