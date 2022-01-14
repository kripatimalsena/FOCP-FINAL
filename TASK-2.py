a = []  # it is a empty list 
print("Swallow speed Analysis: version 1.0")
while True:
    name = input("Enter the next reading: ")
    if name == "": #check whether the data entere is 
        break
    elif name[0]== "U" or name[0]=="u":
        a.append(float(name[1:]))
        print("reading saved")
    elif name[0] =="E" or name[0] == "e":
        a.append(float(name[1:])/1.61)
        print("reading saved")
if len(a) > 0:   
    max_miles = max(a)
    max_km = max_miles * 1.61
    min_miles = min(a)
    min_km = min_miles *1.61

    sum = 0
    for i in range(len(a)):
        sum += a[i]
    avg_miles = sum/ len(a)
    avg_km = avg_miles*1.61
    print("\nReading summary\n")
    
    if len(a) == 1: #length of list = 1
        print( len(a) ," Reading analysed\n")
    else:
        print(len(a)," Readings analysed\n")    
    
    print("Max is %.1f KMP  %.1f MPH"%(max_km,max_miles))
    print("Min is %.1f KMP %.1f MPH"%(min_km,min_miles))
    print("Avg is %.1f KMP %.1f MPH"%(avg_km,avg_miles))
else:
    print("No reading entered, Nothing to do.") 

 
    

