print("=" * 10, "While", "=" * 10)
i = 0
index = True
while index:
    print("Text")
    i += 1
    if i == 4:
        index = False
print("=" * 10, "For", "=" * 10)
for i in range(10):
    print(i, end=" ")
print()
for i in range(1, 10, 2):
    print(i, end=" ")
print()
for i, element in enumerate([1, "two", "three"]):
    print(i, element)
for element in [1, 2, 5, "three", "four"]:
    print(element)
for key, value in {"first": 1, "second": 2, "three": 3}.items():
    print(f"The key {key} contains value {value}")
