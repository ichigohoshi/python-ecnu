def is_rotation(str1: str, str2: str) -> bool:
    if str1 == str2:
        return True
    len1 = len(str1)
    len2 = len(str2)
    if len1 != len2:
        return False
    str1_char_count = [0 for _ in range(128)]
    str2_char_count = [0 for _ in range(128)]
    for i in range(len1):
        str1_char_count[ord(str1[i])] += 1
        str2_char_count[ord(str2[i])] += 1
    for i in range(128):
        if str1_char_count[i] != str2_char_count[i]:
            return False
    for i in range(len1):
        str2 = str2[1:] + str2[0]
        if str1 == str2:
            return True
    return False


s, t = map(str, input().split())
print("\"{}\" is {}a rotation of \"{}\"".format(s, "" if is_rotation(s, t) else "NOT " ,t))
