# Write your code here

strng = "Google.com"
strng = strng.lower()
dic = {}

for str in range(len(strng)):
    if strng[str] not in dic:
        dic[strng[str]] = 1
    else:
        dic[strng[str]] += 1

print(dic)
