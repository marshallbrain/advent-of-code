low = 168630
high = 718098


def incressing_digits(num):
    s_num = str(num)
    last = 0
    for s in s_num:
        if int(s) < last:
            return False
        last = int(s)
    return True


def has_pair(num):
    s_num = str(num)
    for i in range(0, len(s_num)-1):
        if s_num[i] == s_num[i+1]:
            return True
    return False


match = []
for n in range(low, high+1):
    if not incressing_digits(n):
        continue
    if not has_pair(n):
        continue
    match.append(n)

print(len(match))
