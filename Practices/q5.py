# Please ensure the platform IDE is in Python 3.x mode.

strs = input()
strs = strs.split()
ans = []


def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


for i in range(len(strs)):
    if is_prime(len(strs[i])):
        ans.append(strs[i])

print(" ".join(ans))
