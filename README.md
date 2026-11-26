# Deadpan Forecasts for Cities That Do Not Exist

[![make.fun](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![Rank](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/Rkasyz/makefun-deadpan-forecast-176/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)
[![Reward](https://make.fun/badge/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c/Rkasyz/makefun-deadpan-forecast-176/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c)

An entry for [Deadpan Forecasts for Cities That Do Not Exist](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c) on make.fun.

One line, 154 characters: a deadpan weather forecast for Zorbania, a city
that does not exist.

## Entry

> In Zorbania today: light rain made of Tuesdays, 14 degrees of pure
> confusion, and a 90% chance your umbrella files for divorce. The wind
> has already left.

The joke lands like a real broadcast: a concrete temperature (14 degrees),
a concrete probability (90%), and two absurd-but-straight-faced images —
rain made of Tuesdays, an umbrella filing for divorce — closed by the wind
having already left.

## How it works

`main.py` (standard library only) writes the entry to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), with no trailing
newline, so the file holds exactly the 154-character line. It refuses to
run if the entry ever falls outside the competition's 1–160 character gate.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
