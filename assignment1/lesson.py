snack_box1 = {"Chips", "Cookies", "Juice", "Biscuits"}
snack_box2 = {"Juice", "Popcorn", "Chips", "Chocolate"}

snack_box1.add("Apples")

print("Snack Box 1:", snack_box1)
print("Snack Box 2:", snack_box2)

shared_snacks = snack_box1.intersection(snack_box2)
print("Shared snacks:", shared_snacks)

snack_counts = [10, 15, 8, 12, 20]

snack_counts.append(25)
print("Snack counts:", snack_counts)

print("Count of 10:", snack_counts.count(10))

snack_counts.reverse()
print("Reversed snack counts:", snack_counts)