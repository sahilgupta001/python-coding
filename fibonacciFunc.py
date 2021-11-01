# Ab ye program me purane vaale se sirf 2 changes hai
# pehla ki ye function se solve hoga
# dusra ye ki isme hum puri series ki jagah sirf ek position vaala number print karege


def printFibonacci(pos):
    if pos == 1:
        print("0")
        return #isko samajhio ki ye kya kar rha hai ...jese continue samajh rha tha
    if pos == 2:
        print("1")
        return

    num1 = 0
    num2 = 1

    # isko initial value awai di hai no meaning
    sum = 0
    
    for i in range(2, pos):
        sum = num1 + num2
        num1 = num2
        num2 = sum
    # ab ye sum me final answer kese store hua ye tujhe samajh ni ayega I know
    # me to aapko samjhauga hi but agar tune khud se isss loop ka har step likh lia pen paper pe
    # to tu sirf ye ques ni samjhega balki logic building me ek acha improvement layega
    # aur yahi tareeka best hai

    # uske baad bhi samajh ni ayega to bhi koi tension ni but try karna is imp
    # jitni der tak haar ni maanega utna jaldi job payega
    # fir me bhi samjhauga and tu apne dimaag me match karega ki kya me sai sochra tha.. jisse confidence ayega
    return sum

pos = int(input("Enter the position of the number that you want from the series "))
ans = printFibonacci(pos)
print("Fibonaccu number at position ", pos, " is ", ans)