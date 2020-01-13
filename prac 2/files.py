MIN_LENGTH = 10
def main():
    password = int(input("please enter"))
    if password !=  (MIN_LENGTH):
        print ("enter valid input")
        password = int(input("please enter"))
    else:
        print(stars)
        def stars():
            stars = '*'*len(password)
            stars()
main()