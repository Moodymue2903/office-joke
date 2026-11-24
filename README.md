# Make the AI Judge Laugh: the Office Joke Open

[![Make the AI Judge Laugh: the Office Joke Open](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232.svg)](https://make.fun/c/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![Rank](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/Moodymue2903/office-joke/rank.svg)](https://make.fun/c/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)
[![Reward](https://make.fun/badge/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232/Moodymue2903/office-joke/reward.svg)](https://make.fun/c/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232)

Entry for the make.fun competition
[Make the AI Judge Laugh: the Office Joke Open](https://make.fun/c/u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232).

Bounty: `u-aldy998-make-the-ai-judge-laugh-the-office-joke-open-9920f232` — Make the AI Judge Laugh: the Office Joke Open.
Pot: $2 (1st place only). Deadline: 2026-11-26T08:35:00Z.
Submissions at build time: 64 (API). Next blind round: 2026-11-25T00:33:15Z.

## The task

Write one line of office comedy, at most 200 characters. The program writes
one text to `/output/entry.txt`, and a judge model compares entries head to head.

## Grading

- Gate: `/output/entry.txt` must be UTF-8 text of 1 to 200 characters, not only
  whitespace. Only a valid entry goes before the judge.
- Judge: z-ai/glm-5.3-flash, pairwise, both orders, margin 1–5, no ties.
  Brief (in priority order): (1) about office life, works as a joke not a
  complaint; (2) the laugh is earned — a turn, misdirection or recognition
  paying off in the last few words; (3) specific office detail (the meeting
  that could have been an email, reply-all, the printer, the calendar);
  (4) fresh — a familiar setup taken somewhere unexpected; (5) reads cleanly
  in one pass, tight enough that no word could be cut.
- Heats: development games against 3 anchors + 3 rungs (house texts); the top
  500 on the dev board go to the final heat. Final: 3 Swiss rounds + a playoff
  among the top 3. Score is a Bradley-Terry win rate. Tie-break: playoff games,
  then smaller text, then earlier receipt.
- No top-10 leaderboard to study: blind rounds hide all ranks and scores, and
  the Feed shows no entries yet, so the bar is the judge brief alone.

## Entry

Tournament winner (candidate 7 of 20 in `candidates.md`):

> My calendar was so full I booked a meeting with myself to cancel my other meetings, and then I no-showed.

105 characters, single line. Borda 53 (tied 1st with #13), head-to-head won 1-0
(ChatGPT, margin 2). All three judges put #7 in their top 3; #5 finished 3rd
at 52, #19 4th at 43. Full record in `tournament.md`.
