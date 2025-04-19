# Pratice with functions
print("Bitch")
num_char = len("Hello")
print(num_char)


# Function definition
# def my_function():
#     print("hello")
#     print("bye")
#
# my_function()
# for steps in range(8):
#     my_function()

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)

        return s == t

s = ["race"]
t = ["ecar"]

answer = Solution.isAnagram(s, t)
print(answer)
