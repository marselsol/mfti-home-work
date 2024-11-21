def reverse_and_sort_words(input_string):
    words = input_string.split()
    reversed_words = [word[::-1] for word in words]
    sorted_reversed_words = sorted(reversed_words)
    for word in sorted_reversed_words:
        print(word)

test_string_1 = "apple banana cherry"
test_string_2 = "zebra lion tiger"

print("Results for test_string_1:")
reverse_and_sort_words(test_string_1)
print("\nResults for test_string_2:")
reverse_and_sort_words(test_string_2)
