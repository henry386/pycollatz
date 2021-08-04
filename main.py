def calculate(num):
    if num % 2 != 0:
        i = num * 3 + 1
        print(str(int(num)) + " is Odd, Therefore: (3*" + str(int(num)) + ")+1 = " + str(int(i)))

    else:
        i = num / 2
        print(str(int(num)) + " is Even, Therefore: " + str(int(num)) + "/2 = " + str(int(i)))

    if num != 1:
        calculate(i)
    else:
        print("")
        print("The algorithm is now in the infinite 1-4-2-1 Sequence (I have stopped the process to stop it from "
              "taking up system resources)")
        print("")
        print("What would happen is: \n"
              "(1*3)+1 = 4 \n"
              "4/2 = 2 \n"
              "2/2 = 1 \n"
              "(1*3)+1 = 4 \n"
              "And so on... \n")


print("")
print("Collatz Conjuncture")
print("")
print("About:")
print("If the integer is even then the number is halved, if the integer is odd then the number is put into the "
      "equation 3X+1")
print("This algorithm will (almost) always result in pattern 4, 1, 4, etc..")
print("")

int_main = int(input("Enter End Number: "))
print("")

calculate(int_main)
