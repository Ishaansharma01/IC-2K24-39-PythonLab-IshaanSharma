
paragraph = input("Enter a paragraph: ")

# 1. Clean the paragraph: lowercase and remove punctuation
cleaned = ""

for ch in paragraph.lower():
    if ch.isalnum() or ch.isspace():
        cleaned += ch

words = cleaned.split()

if not words:
    print("Please enter a non-empty paragraph.")

else:
    # 2. Count word frequencies using get()
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    print("\nWord Counts:")
    print(frequency)

    # 3. Print top N words, ties broken alphabetically
    n = int(input("\nEnter N for top N words: "))

    sorted_words = sorted(
        frequency.items(),
        key=lambda item: (-item[1], item[0])
    )

    print("\nTop", n, "words:")
    for word, count in sorted_words[:max(0, n)]:
        print(word, "->", count)

    # 4. Words appearing exactly once
    once = sorted([
        word for word, count in frequency.items()
        if count == 1
    ])

    print("\nWords appearing exactly once:")
    print(once)

    # 5. Invert dictionary: frequency -> list of words
    inverted = {}

    for word, count in frequency.items():
        inverted.setdefault(count, []).append(word)

    for count in inverted:
        inverted[count].sort()

    print("\nInverted Dictionary:")
    print(inverted)

    # 6. Group words by length
    length_groups = {}

    for word in frequency:
        length = len(word)
        length_groups.setdefault(length, []).append(word)

    for length in length_groups:
        length_groups[length].sort()

    print("\nWords Grouped by Length:")
    print(length_groups)

    # 7. Search for a word
    search_word = input("\nEnter a word to search: ").lower()

    # Remove punctuation from the searched word too
    cleaned_search = ""
    for ch in search_word:
        if ch.isalnum():
            cleaned_search += ch

    if cleaned_search in frequency:
        print(cleaned_search, "appears",
              frequency[cleaned_search], "time(s).")
    else:
        print("Word not found.")
