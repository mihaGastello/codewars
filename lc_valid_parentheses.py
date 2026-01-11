# https://leetcode.com/problems/valid-parentheses/description/

def is_valid(s: str) -> bool:
    chars = list(s)
    temp = []
    for c in chars:
        if c in ["(", "{", "["]:
            temp.append(c)
        elif c in [")", "}", "]"] and len(temp) == 0:
            temp.append("X")
            break
        elif c == ")":
            if temp[-1] == "(":
                temp.pop(-1)
            else:
                break
        elif c == "}":
            if temp[-1] == "{":
                temp.pop(-1)
            else:
                break
        elif c == "]":
            if temp[-1] == "[":
                temp.pop(-1)
            else:
                break
    return len(temp) == 0


def is_valid2(s: str) -> bool:
    while len(s) > 0:
        l = len(s)
        s = s.replace('()','').replace('{}','').replace('[]','')
        if l==len(s): return False
    return True

print(is_valid("(((((((((})))))))))"))
print(is_valid2("(((((((((})))))))))"))