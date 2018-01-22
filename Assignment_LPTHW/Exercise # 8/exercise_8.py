formatter = " {} {} {} {} {} {} {} "
print(formatter.format(1, 2, 3, 4, 5, 6, 7))
print(formatter.format("one", "two", "three", "four", "five", "six", "seven"))
print(formatter.format(True, False, False, True, True, True, False))
print(formatter.format(formatter, formatter, formatter, formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear",
    "Or a gothic fiction book",
    "Silly song lyrics here",
    "Maybe a quote you love"
    ))
