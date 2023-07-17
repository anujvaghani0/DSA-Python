# str = input()
# temp = ""
# for i in range(len(str)):
#     if i % 2 == 0:
#         temp += str[i]
# print(temp)

# def main(data):
#     for item in data:
#         print("Type of", item, "is", type(item))
#
# data = eval(input())
# main(data)

# write your code inside main function
def main(word):
    if word in ('a', 'e', 'i', 'o', 'u'):
        print("Vowel")
    else:
        print("Consonant")


word = input()
main(word);