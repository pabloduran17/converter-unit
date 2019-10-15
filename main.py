print("-------------Make yourself comfortable and enjoy the one and only converter machine-------------------------")

while True:

    Miles = .62
    Kilometers = None
    Kilometers =int(input("Please tell me how many Kilometers you would like to convert"))



    print(Miles * Kilometers)

    d1a = input("Do you want to: yes) Make another conversion. no) To end up and go home? : ")
    if d1a == "yes":
        print("")
    elif d1a == "no":
        print("Have a nice day!.")
        break
    else:
        print("I don´t get it mate")
        d1a = input("Do you want to: yes) Make another conversion. no) To end up and go home? : ")
        if d1a == "no":
              print("Have a nice day!.")
              break
























