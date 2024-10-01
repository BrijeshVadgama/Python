# 2. WAP to reverse the words in given string.

str = input("Enter a string: ")
word = str.split()
rev = word[::-1]
ans = " ".join(word)

print(f"Original string {str}")
print(f"Reversed string {rev}")
