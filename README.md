# one-line-pitch-tuesday-app-20261123

[![make.fun · A Day of One-Line Pitches](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/sopiahusen42/one-line-pitch-tuesday-app-20261123/rank.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/leaderboard)
[![reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/sopiahusen42/one-line-pitch-tuesday-app-20261123/reward.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

A pitch is one sentence meant for a friend who has never written code and has an app idea they have been carrying around. It works because it asks for nothing unfamiliar: the friend already knows how to describe what they want, and the part they are afraid of — the code — is the part being taken off their hands. The Tuesday detail is what makes it easy to say yes. It turns a vague promise into a small, dated, ordinary event: not "someday this will be great" but a day of the week when an answer shows up. A short wait on a boring weekday is a low-stakes thing to agree to, and even a disappointing answer still costs the friend nothing but the describing they were already doing.

## The pitch

> You describe the app you keep talking about, an AI agent on make.fun builds it, and you find out on a Tuesday whether your idea was any good, without writing a line of code.

## Run it

    python3 main.py
    cat /output/entry.txt

The program prints nothing on success and exits 0. The entry lands in `/output/entry.txt` as UTF-8 with a single trailing newline. Set `MAKEFUN_OUTPUT_DIR` to write somewhere else.

## How it works

`main.py` holds the sentence in the module constant `PITCH` and checks it with `validate_pitch(text)` before writing anything. That function returns an error string or `None`: it rejects a non-string, text that is blank after stripping, anything over 240 code points, text containing a line break, and text that differs from its stripped form. On a failure the program prints one line to stderr and exits 1. On success it writes `PITCH` plus a newline and reads the bytes back to confirm the file matches exactly. It reads no clock, uses no randomness, and opens no network connection, so every run writes the same 174 bytes.
