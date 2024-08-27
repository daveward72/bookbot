def count_words(s):
    return len(s.split())

def count_characters(s):
    charDict = {}
    for c in s.lower():
        if not c.isalpha():
            continue

        if not c in charDict:
            charDict[c] = 0

        charDict[c] += 1

    listCharCounts = []
    for c in charDict:
        listCharCounts.append({"char": c, "count": charDict[c]})

    listCharCounts.sort(reverse=True, key=lambda x:x["count"])

    return listCharCounts

def get_file_contents(path):
    with open(path) as f:
        return f.read()

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
        print(file_contents)

        word_count = count_words(file_contents)
        print(f'There are {word_count} words')

        char_counts = count_characters(file_contents)
        for listEntry in char_counts:
            c = listEntry["char"]
            count = listEntry["count"]
            print(f"The '{c}' character was found {count} times")
        print("--- End report ---")

main()