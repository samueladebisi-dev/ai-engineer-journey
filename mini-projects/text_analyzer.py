words_list = text.lower().split()

word_counts = {}

for word in words_list:
    word_counts[word] = word_counts.get(word, 0) + 1

most_common = max(word_counts, key=word_counts.get)

print("Most Common Word:", most_common)

reading_time = round(words / 200, 2)

print("Estimated Reading Time:", reading_time, "minutes")
