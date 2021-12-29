absent = [2,3,5,7]
stop = [6]
for students in range(1,10+1) :
    if students in absent :
        continue
    elif students in stop :
        print(f"{students} 멈춰")
        break
    print(f"{students}, 소리질러")
