print("=== 1. Counting with while ===")

count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

print()
print("=== 2. Counting down ===")

remaining = 3
while remaining > 0:
    print(remaining)
    remaining -= 1
print("Go!")

print()
print("=== 3. Leaving a loop with break ===")

candidate = 1
target = 4
while candidate <= 10:
    if candidate == target:
        print("Found the target.")
        break

    print(f"Checked: {candidate}")
    candidate += 1

print()
print("=== 4. Skipping an iteration with continue ===")

number = 0
while number < 6:
    number += 1

    if number % 2 == 0:
        continue

    print(f"Odd number: {number}")

print()
print("End of examples.")
