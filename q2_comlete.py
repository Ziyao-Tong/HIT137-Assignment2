"""
Question 2: Expression Evaluator
Student Name: Saima Akter
Student ID: S394703
"""

import os


def tokenize(expression):
    tokens = []
    i = 0
    length = len(expression)

    while i < length:
        ch = expression[i]

        if ch.isspace():
            i += 1
            continue

        if ch.isdigit() or (ch == '.' and i + 1 < length and expression[i + 1].isdigit()):
            num_str = ""
            while i < length and (expression[i].isdigit() or expression[i] == '.'):
                num_str += expression[i]
                i += 1
            tokens.append(("NUM", num_str))
            continue

        if ch in "+-*/":
            tokens.append(("OP", ch))
            i += 1
            continue

        if ch == '(':
            tokens.append(("LPAREN", "("))
            i += 1
            continue

        if ch == ')':
            tokens.append(("RPAREN", ")"))
            i += 1
            continue

        return None

    tokens.append(("END", "END"))
    return tokens


def format_tokens(tokens):
    parts = []
    for tok_type, tok_value in tokens:
        if tok_type == "END":
            parts.append("[END]")
        else:
            parts.append(f"[{tok_type}:{tok_value}]")
    return " ".join(parts)


def parse(tokens):

    pos = [0]

    def current():
        return tokens[pos[0]]

    def advance():
        tok = tokens[pos[0]]
        pos[0] += 1
        return tok

    def parse_expression():
        left = parse_term()
        if left is None:
            return None

        while current()[0] == "OP" and current()[1] in ('+', '-'):
            op = advance()[1]
            right = parse_term()
            if right is None:
                return None
            left = ("binop", op, left, right)

        return left

    def parse_term():
        left = parse_unary()
        if left is None:
            return None

        while True:
            if current()[0] == "OP" and current()[1] in ('*', '/'):
                op = advance()[1]
                right = parse_unary()
                if right is None:
                    return None
                left = ("binop", op, left, right)

            elif current()[0] in ("NUM", "LPAREN") or \
                 (current()[0] == "OP" and current()[1] == '-'):

                if current()[0] in ("NUM", "LPAREN"):
                    right = parse_unary()
                    if right is None:
                        return None
                    left = ("binop", "*", left, right)
                else:
                    break
            else:
                break

        return left

    def parse_unary():
        if current()[0] == "OP" and current()[1] == '-':
            advance()
            operand = parse_unary()
            if operand is None:
                return None
            return ("neg", operand)

        if current()[0] == "OP" and current()[1] == '+':
            return None

        return parse_atom()

    def parse_atom():
        tok = current()

        if tok[0] == "NUM":
            advance()
            value = float(tok[1])
            return ("num", value)

        if tok[0] == "LPAREN":
            advance()
            expr = parse_expression()
            if expr is None:
                return None
            if current()[0] != "RPAREN":
                return None
            advance()
            return expr


        return None

    tree = parse_expression()


    if tree is None or current()[0] != "END":
        return None

    return tree


# =============================================================================
# Tree Formatting
# =============================================================================

def format_number(value):
    if value == int(value):
        return str(int(value))
    return str(value)


def format_tree(tree):
    if tree[0] == "num":
        return format_number(tree[1])

    if tree[0] == "binop":
        _, op, left, right = tree
        return f"({op} {format_tree(left)} {format_tree(right)})"

    if tree[0] == "neg":
        return f"(neg {format_tree(tree[1])})"

    return "ERROR"

def evaluate_tree(tree):
    if tree[0] == "num":
        return tree[1]

    if tree[0] == "neg":
        operand = evaluate_tree(tree[1])
        if operand is None:
            return None
        return -operand

    if tree[0] == "binop":
        _, op, left, right = tree
        left_val = evaluate_tree(left)
        right_val = evaluate_tree(right)

        if left_val is None or right_val is None:
            return None

        if op == '+':
            return left_val + right_val
        elif op == '-':
            return left_val - right_val
        elif op == '*':
            return left_val * right_val
        elif op == '/':
            if right_val == 0:
                return None  # Division by zero
            return left_val / right_val

    return None


def format_result(value):

    if value is None:
        return "ERROR"
    if value == int(value):
        return str(int(value))
    return f"{value:.4f}"


def evaluate_file(input_path: str) -> list:
    # Read input file
    with open(input_path, 'r') as f:
        lines = f.readlines()

    results = []

    for line in lines:
        expression = line.rstrip('\n').rstrip('\r')

        # Skip blank lines
        if expression.strip() == "":
            continue

        entry = {"input": expression}

        # Tokenize
        tokens = tokenize(expression)

        if tokens is None:
            # Invalid character found — everything is ERROR
            entry["tree"] = "ERROR"
            entry["tokens"] = "ERROR"
            entry["result"] = "ERROR"
            results.append(entry)
            continue

        # Format tokens string
        entry["tokens"] = format_tokens(tokens)

        # Parse into expression tree
        tree = parse(tokens)

        if tree is None:
            entry["tree"] = "ERROR"
            entry["result"] = "ERROR"
            results.append(entry)
            continue

        # Format tree string
        entry["tree"] = format_tree(tree)

        # Evaluate
        value = evaluate_tree(tree)
        if value is None:
            entry["result"] = "ERROR"
        else:
            entry["result"] = value

        results.append(entry)

    output_dir = os.path.dirname(input_path)
    if output_dir == "":
        output_dir = "."
    output_path = os.path.join(output_dir, "output.txt")

    with open(output_path, 'w') as f:
        for i, entry in enumerate(results):
            f.write(f"Input: {entry['input']}\n")
            f.write(f"Tree: {entry['tree']}\n")
            f.write(f"Tokens: {entry['tokens']}\n")

            if entry['result'] == "ERROR":
                f.write("Result: ERROR\n")
            else:
                f.write(f"Result: {format_result(entry['result'])}\n")

            if i < len(results) - 1:
                f.write("\n")

    return results

# Entry Point — Run directly for testing
if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "sample_input.txt"

    results = evaluate_file(path)

    for entry in results:
        print(f"Input: {entry['input']}")
        print(f"Tree: {entry['tree']}")
        print(f"Tokens: {entry['tokens']}")
        if entry['result'] == "ERROR":
            print("Result: ERROR")
        else:
            print(f"Result: {format_result(entry['result'])}")
        print()
