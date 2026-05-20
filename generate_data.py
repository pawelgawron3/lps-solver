half = 249_999
text = ("a" * half) + "b" + ("a" * half)

with open("input.txt", "w") as f:
    f.write(text)

print(f'The data has been generated and saved in input.txt file. The size of a word is {len(text)} chars')