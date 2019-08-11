def print_formatted(number):
    for i in range(1,number+1):
        if i != 1:
            print(end='\n')
        print(i,end=" ")
        print(oct(i).replace("0o",""),end=" ")
        print(hex(i).replace("0x",""),end=" ")
        print(bin(i).replace("0b",""),end="")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
