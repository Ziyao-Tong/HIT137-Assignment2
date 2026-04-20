# HIT137 Assignment 2 — Question 2: Expression Evaluator

**Student:** Saima Akter (S394703)

## Overview

A recursive descent parser that reads mathematical expressions from a text file, tokenizes them, builds expression trees, evaluates the results, and writes structured output to `output.txt`.

The entire solution uses plain functions — no classes.

## How to Run

```bash
python evaluator.py sample_input.txt
```

This reads expressions from `sample_input.txt` (one per line) and produces `output.txt` in the same directory.

You can also import the function directly:

```python
from evaluator import evaluate_file

results = evaluate_file("sample_input.txt")
```

## Features

- **Operator precedence:** `*` and `/` bind tighter than `+` and `-`
- **Parentheses:** nested to any depth
- **Unary negation:** `-5`, `--5`, `-(3+4)`, `3 * -2`
- **Implicit multiplication:** `2(3)` and `(2)(3)` are treated as `2 * 3`
- **Error handling:** invalid characters (e.g. `@`) and division by zero produce `ERROR`
- **Unary `+`:** not supported — produces an error as required

## Output Format

Each expression produces a four-line block separated by blank lines:

```
Input: 2 + 3 * 4
Tree: (+ 2 (* 3 4))
Tokens: [NUM:2] [OP:+] [NUM:3] [OP:*] [NUM:4] [END]
Result: 14
```

Whole-number results display without a decimal point. Non-whole results are rounded to 4 decimal places.

## Files

| File | Description |
|---|---|
| `q2_evaluator.py` | Main program |
| `sample_input.txt` | Provided sample expressions |
| `sample_output.txt` | Expected output for verification |
| `output.txt` | Generated output (after running) |
