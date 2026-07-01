# Python Fundamentals Tracker

A single-file, terminal-styled learning tracker for going through Python fundamentals in 10 weeks — built for a 1 hour/day, Monday–Friday study schedule, with a habit-tracker calendar and daily coding challenges instead of multiple-choice quizzes.

![status](https://img.shields.io/badge/status-personal%20project-informational)
![type](https://img.shields.io/badge/type-single--file%20HTML-blue)

## What it is

`python-fundamentals-tracker.html` is a self-contained dashboard (HTML/CSS/JS, no build step, no dependencies) that walks through 50 daily lessons — 10 weeks × 5 weekdays — covering Python fundamentals from variables through basic OOP, file I/O, error handling, and a final week on calling APIs with `requests` and `boto3`.

Each day includes:
- A short **lesson summary**
- A **coding challenge** you write and run yourself as a real `.py` script (not multiple choice) — many challenges are framed around AWS/infra scenarios (EC2 instances, S3 buckets, CPU/log parsing) to match cloud/DevOps-track learning
- A **notes field** for what tripped you up
- A **mark-complete** toggle

A git-contribution-style **habit tracker grid** shows weekday completion history and current streak, and summary stats (days completed, streak, projected finish date) sit at the top.

## Curriculum overview

| Week | Topic |
|---|---|
| 1 | Variables, data types, operators, input/output |
| 2 | Control flow — if/else, loops, break/continue |
| 3 | Data structures — lists, tuples, dicts, sets |
| 4 | Functions — args, return values, scope, lambdas |
| 5 | String manipulation & formatting |
| 6 | File I/O — text files, CSV, JSON |
| 7 | Error handling — try/except, custom exceptions |
| 8 | Modules, packages, virtual environments |
| 9 | OOP basics — classes, objects, inheritance |
| 10 | Working with APIs, intro to boto3, final project |

## Usage

Open `python-fundamentals-tracker.html` directly in any browser — no server, no build step, no dependencies. Progress (completed days, notes, streaks) is saved automatically to your browser's local storage, so it persists between visits on the same browser/device.

Note: progress is stored per-browser. Opening the file in a different browser or clearing site data will reset it.

## Tech

- Plain HTML/CSS/JS — no frameworks, no build tools, no npm install
- Single file, opens directly in a browser
- All 50 lessons/challenges are hardcoded in a `CURRICULUM` array near the top of the `<script>` block — easy to edit, reorder, or extend

## Customizing

- **Add/edit challenges:** edit the `CURRICULUM` array — each entry is `{ id, week, weekTopic, title, lesson, challenge }`
- **Change pace:** the habit grid and streak logic assume Mon–Fri; adjust the weekday checks in `computeStats()` and `renderHabitGrid()` if your schedule differs
- **Restyle:** all design tokens (colors, fonts) are CSS custom properties at the top of the `<style>` block under `:root`

## Reference

- [W3Schools Programming](https://www.w3schools.com/programming/index.php) — general reference for looking up Python (and other language) syntax alongside the daily lessons

## License

Personal project — use, fork, or adapt freely.