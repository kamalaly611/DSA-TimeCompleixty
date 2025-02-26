# Define empty dictionary to store word counts
word_counts = {}

# Open the file and iterate through each line
with open("poem.txt", "r") as f: 
    for line in f:
        # Split the line into words
        line_list = line.split()
        
        # Iterate through each word in the line
        for word in line_list:
            # Increment the count of the word if it's already in the dictionary
            if word in word_counts:
                word_counts[word] += 1
            # Otherwise, initialize the count to 1
            else:
                word_counts[word] = 1

# Find the maximum occurrence of each word
for word, count in word_counts.items():
    max_occurrences = max(word_counts.values())
    if count == max_occurrences:
        print(f"The word '{word}' occurs maximum {max_occurrences} times.")
