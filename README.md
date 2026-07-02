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

### Week 1 — Variables, Data Types & I/O
| Day | Topic |
|---|---|
| 1 | Variables & print/input |
| 2 | Numbers & arithmetic |
| 3 | Strings & f-strings |
| 4 | Booleans & comparisons |
| 5 | Type conversion — review |
 
### Week 2 — Control Flow
| Day | Topic |
|---|---|
| 1 | if / elif / else |
| 2 | while loops |
| 3 | for loops & range() |
| 4 | break, continue, pass |
| 5 | Nested loops — review |
 
### Week 3 — Data Structures
| Day | Topic |
|---|---|
| 1 | Lists |
| 2 | List methods & slicing |
| 3 | Tuples |
| 4 | Dictionaries |
| 5 | Sets — review |
 
### Week 4 — Functions
| Day | Topic |
|---|---|
| 1 | Defining functions |
| 2 | Default & keyword arguments |
| 3 | *args and **kwargs |
| 4 | Scope |
| 5 | Lambda functions — review |
 
### Week 5 — String Manipulation
| Day | Topic |
|---|---|
| 1 | String methods |
| 2 | Formatting deep dive |
| 3 | Intro to regex (re module) |
| 4 | Practical parsing |
| 5 | Review project |
 
### Week 6 — File I/O
| Day | Topic |
|---|---|
| 1 | Reading & writing text files |
| 2 | CSV module |
| 3 | JSON module |
| 4 | Context managers (with) |
| 5 | Review — parse a log file |
 
### Week 7 — Error Handling
| Day | Topic |
|---|---|
| 1 | try / except basics |
| 2 | else, finally & multiple excepts |
| 3 | Raising exceptions |
| 4 | Custom exceptions |
| 5 | Review — robust script |
 
### Week 8 — Modules & Environments
| Day | Topic |
|---|---|
| 1 | import & the standard library |
| 2 | Writing your own modules |
| 3 | pip & third-party packages |
| 4 | Virtual environments |
| 5 | Review — organize a project |
 
### Week 9 — Object-Oriented Programming
| Day | Topic |
|---|---|
| 1 | Classes & objects |
| 2 | __init__ and attributes |
| 3 | Methods |
| 4 | Inheritance |
| 5 | Review — class hierarchy |
 
### Week 10 — APIs, boto3 & Final Project
| Day | Topic |
|---|---|
| 1 | requests & calling a REST API |
| 2 | Parsing JSON API responses |
| 3 | Intro to boto3 — S3 |
| 4 | boto3 — EC2 instances |
| 5 | Final project |

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
- [W3Schools Python](https://www.w3schools.com/python/default.asp) — Python-specific reference and tutorial

## License

Personal project — use, fork, or adapt freely.