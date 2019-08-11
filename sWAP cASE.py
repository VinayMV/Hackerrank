def swap_case(s):
    s1=''
    for ch in s:
        if ch.islower():
            s1+=ch.upper()
        else:
            s1+=ch.lower()
    return(s1)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
