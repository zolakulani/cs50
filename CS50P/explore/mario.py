def main():
    h = int(input("Height: "))
    pyramid(h)

def pyramid(n):
    for i in range (1, n + 1):
        print("#" * i)

main()