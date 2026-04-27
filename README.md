# Password Strength Checker

A command-line Python project that evaluates password quality using length, character variety, and entropy estimation.

## Features

- Strength score from 0 to 100
- Entropy estimation in bits
- Rating label: Weak / Medium / Strong
- Actionable improvement suggestions

## Project Structure

```
password-strength-checker/
  main.py
  requirements.txt
  README.md
```

## Requirements

- Python 3.10+

## Usage

```bash
python main.py
```

## Example Output

- Score: `74/100`
- Strength: `Medium`
- Estimated entropy: `52.10 bits`

## Learning Outcomes

- Regex-based validation
- Entropy fundamentals for passwords
- Scoring logic design
