# HIT137 — Group Assignment 2

## Group Members & Contributions

| Member | GitHub | Contribution |
|---|---|---|
| Mitch | [Mitch3512](https://github.com/Mitch3512) | Question 1 — Encryption logic, file handling, main program structure|
| Ziyao Tong | [Ziyao-Tong](https://github.com/Ziyao-Tong) | Question 1 — Decryption logic, verfication |
| Saima Akter | [saimaaaaaaaa](https://github.com/saimaaaaaaaa) | Question 2 — Expression evaluator (tokenizer, parser, evaluator) |

---

## Project Structure

```
.
├── member1_encryption.py      # Q1: Encryption functions
├── q1_complete.py             # Q1: Main program (encrypt → decrypt → verify)
├── member2_evaluation.py      # Q2: Expression evaluator (alternate entry point)
├── q2_evaluator.py            # Q2: Expression evaluator (main module)
├── raw_text.txt               # Q1: Input text file
├── sample_input.txt           # Q2: Sample mathematical expressions
├── sample_output.txt          # Q2: Expected output for verification
├── output.txt                 # Q2: Generated output (after running)
├── readmeQ2.md                # Q2: Standalone readme
└── README.md                  # This file
```

---

## Question 1: Encryption & Decryption

### Overview

A custom cipher that reads `raw_text.txt`, encrypts it using two user-provided shift values, then decrypts and verifies the result matches the original.

### Encryption Rules

Given two integer inputs `shift1` and `shift2`:

**Lowercase letters:**
- `a`–`m` → shift forward by `shift1 × shift2`
- `n`–`z` → shift backward by `shift1 + shift2`

**Uppercase letters:**
- `A`–`M` → shift backward by `shift1`
- `N`–`Z` → shift forward by `shift2²`

**Other characters** (spaces, digits, punctuation, newlines) remain unchanged.

### Decryption Approach

The decryption uses a brute-force reverse lookup — for each encrypted character, it tests every possible letter of the same case through the encryption function and returns the one that produces a match. This guarantees correct reversal regardless of shift values.

### How to Run

```bash
python q1_complete.py
```

The program will:
1. Prompt for `shift1` and `shift2` values
2. Encrypt `raw_text.txt` → `encrypted_text.txt`
3. Decrypt `encrypted_text.txt` → `decrypted_text.txt`
4. Compare the decrypted output against the original and print the verification result

### Files

| File | Role |
|---|---|
| `member1_encryption.py` | Core encryption logic: `encrypt_char()`, `encrypt_file()`, `read_file()`, `write_file()`, `get_integer_input()` |
| `q1_complete.py` | Main entry point — runs the full encrypt → decrypt → verify pipeline |

---

## Question 2: Mathematical Expression Evaluator

### Overview

A recursive descent parser built entirely from plain functions (no classes) that reads mathematical expressions from a text file, tokenizes them, builds expression trees, evaluates the results, and writes structured output to `output.txt`.

### How to Run

```bash
python q2_evaluator.py sample_input.txt
```

Or import the function directly:

```python
from q2_evaluator import evaluate_file

results = evaluate_file("sample_input.txt")
```

This produces `output.txt` in the same directory as the input file.

### Features

- **Operator precedence:** `*` and `/` bind tighter than `+` and `-`
- **Parentheses:** nested to any depth
- **Unary negation:** `-5`, `--5`, `-(3+4)`, `3 * -2`
- **Implicit multiplication:** `2(3)` and `(2)(3)` are treated as multiplication
- **Error handling:** invalid characters (e.g. `@`) and division by zero produce `ERROR`
- **Unary `+`:** not supported — correctly produces an error as specified

### Output Format

Each expression produces a four-line block separated by blank lines:

```
Input: (10 - 2) * 3 + -4 / 2
Tree: (+ (* (- 10 2) 3) (/ (neg 4) 2))
Tokens: [LPAREN:(] [NUM:10] [OP:-] [NUM:2] [RPAREN:)] [OP:*] [NUM:3] [OP:+] [OP:-] [NUM:4] [OP:/] [NUM:2] [END]
Result: 22
```

- Whole-number results display without a decimal point (e.g. `8` not `8.0`)
- Non-whole results are rounded to 4 decimal places

### Token Types

| Type | Description |
|---|---|
| `NUM` | Numeric literal (integer or decimal) |
| `OP` | Operator: `+`, `-`, `*`, `/` |
| `LPAREN` | Opening parenthesis `(` |
| `RPAREN` | Closing parenthesis `)` |
| `END` | End of token stream |

### Tree Notation

- **Number:** displayed as its value — `3`, `4.5`
- **Binary operation:** `(op left right)` — `(+ 3 5)`, `(* 2 (+ 1 3))`
- **Unary negation:** `(neg operand)` — `(neg 5)`
- **Implicit multiplication:** appears as `*` in the tree

### Files

| File | Role |
|---|---|
| `q2_evaluator.py` | Main evaluator module with `evaluate_file()` interface |
| `sample_input.txt` | Provided sample expressions for testing |
| `sample_output.txt` | Expected output to verify correctness |
| `output.txt` | Generated output after running the program |

---

## Requirements

- Python 3.6 or higher
- No external libraries required (standard library only)
