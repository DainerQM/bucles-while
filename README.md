# Python `while` Loops: Conditions, `break`, and `continue`

A `while` loop repeats a block of code as long as its condition is true. It is
useful when the number of repetitions depends on a condition rather than a
fixed sequence.

This lesson explains how a `while` loop works, how to update state safely,
when to use `break` to leave a loop, and how `continue` skips the rest of the
current iteration.

The runnable companion file is
[`while_examples.py`](./while_examples.py). It contains short, deterministic
examples and uses only Python's built-in features.

## Requirements

- Python 3
- No third-party packages

## Run the examples

Open a terminal in this repository directory and run:

```bash
python while_examples.py
```

On some systems, the Python command is `python3`:

```bash
python3 while_examples.py
```

## 1. How a `while` loop works

Python checks the condition before every iteration:

1. If the condition is `True`, Python runs the indented loop body.
2. Python reaches the end of the body and checks the condition again.
3. If the condition is `False`, Python skips the body and continues after the
   loop.

The basic structure is:

```python
while condition:
    statements
```

For example:

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

This prints `1`, `2`, and `3`. After printing `3`, the increment changes
`count` to `4`; the next condition check (`4 <= 3`) is false, so the loop ends.

If the condition is false before the first check, the body runs zero times.
Unlike a `do while` loop in some other languages, Python's `while` condition
is checked before the body.

## 2. Loop state and termination

A loop often uses a variable to track its progress. In the counting example,
`count` is the loop state:

- It starts at `1`.
- The condition allows values through `3`.
- The loop body changes it by adding `1`.

The update is essential. If `count` never changed, `count <= 3` would remain
true and the loop would never finish. Such a loop is called an **infinite
loop**.

Make sure each loop has a clear path to termination. Common patterns include:

- Move a counter closer to a limit.
- Remove or process an item until none remain.
- Stop when a sentinel value or other state is reached.
- Use `break` when a specific event means the loop should end.

## 3. Counting down

A loop can update state in the opposite direction too:

```python
remaining = 3

while remaining > 0:
    print(remaining)
    remaining -= 1

print("Go!")
```

The `-=` operator subtracts from and reassigns the variable. The condition
becomes false when `remaining` reaches `0`.

## 4. `break`: exit a loop early

`break` immediately ends the **innermost loop** that contains it. Execution
continues with the first statement after that loop:

```python
candidate = 1
target = 4

while candidate <= 10:
    if candidate == target:
        print("Found the target.")
        break

    print("Checked:", candidate)
    candidate += 1
```

When `candidate` reaches `4`, the message is printed and `break` exits the
loop. The loop does not continue to `5`.

`break` is useful when continuing would do no more useful work, such as when
searching for a match or responding to a stop condition.

## 5. `continue`: skip to the next iteration

`continue` skips the rest of the current loop body. Python then checks the
loop condition again and, if it is still true, starts the next iteration:

```python
number = 0

while number < 6:
    number += 1

    if number % 2 == 0:
        continue

    print("Odd number:", number)
```

The remainder operator (`%`) gives the remainder after division. Even numbers
have a remainder of `0` when divided by `2`, so `continue` skips their
`print()` statement. The output contains only `1`, `3`, and `5`.

Update the loop state before `continue` when the update is needed to make
progress. If `number += 1` came after the `if`, an even number would trigger
`continue` before the increment; the same even number would be checked forever.

## 6. `break` and `continue` compared

| Statement | Effect | What happens next |
|---|---|---|
| `break` | Ends the innermost loop immediately | Execution continues after that loop |
| `continue` | Skips the rest of this iteration | The loop condition is checked again |

Both statements affect only the innermost loop in which they appear. In nested
loops, a `break` in the inner loop does not automatically end the outer loop.

## 7. Common mistakes

### Forgetting to update the loop state

If the condition remains true and nothing changes the values it depends on,
the loop may never stop:

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

### Using the wrong comparison

Check whether the boundary should be included. `count < 3` stops before `3`;
`count <= 3` includes `3`.

### Placing `continue` before required progress

If every path through the body must update the counter, do that update before
a `continue` can skip it, or structure the loop so progress is guaranteed.

### Misunderstanding indentation

Only indented statements belong to the loop. A statement aligned with `while`
runs after the loop finishes:

```python
while condition:
    print("Repeated")

print("After the loop")
```

### Using a `while` loop for a fixed number of repetitions

When you are iterating over a known sequence or a fixed range, a `for` loop is
often clearer. Use `while` when repeating depends on a condition that can
change as the program runs.

## 8. Expected output

Running `python while_examples.py` prints:

```text
=== 1. Counting with while ===
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5

=== 2. Counting down ===
3
2
1
Go!

=== 3. Leaving a loop with break ===
Checked: 1
Checked: 2
Checked: 3
Found the target.

=== 4. Skipping an iteration with continue ===
Odd number: 1
Odd number: 3
Odd number: 5

End of examples.
```

## 9. Practice

1. Change the first counter's starting value and limit. Predict how many
   numbers will print, then run the program to check.
2. Change the countdown's starting value to `5`. What is the last number
   printed before `"Go!"`?
3. Change `target` in the `break` example to `1`, then to `10`. How many
   `"Checked"` lines appear in each case?
4. Change the condition in the `continue` example to skip odd numbers instead
   of even numbers.
5. Write a loop that adds the numbers from `1` through `5` and prints the
   final total. Make sure the loop state changes on each iteration.

## Quick reference

```python
while condition:
    if stop_now:
        break

    update_state()

    if skip_this_iteration:
        continue

    do_remaining_work()
```

- A `while` loop checks its condition before each iteration.
- Its body repeats while the condition is true.
- Update loop state so the loop can eventually end.
- `break` exits the innermost loop immediately.
- `continue` skips the rest of the current iteration.
- Indentation determines which statements belong to the loop.
