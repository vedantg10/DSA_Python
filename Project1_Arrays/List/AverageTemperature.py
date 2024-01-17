## Calculate average temperature
i = 1
numDays = int(input("How many days temperature : "))
temp_list = []

while(i<=(numDays)):
    nextDay = int(input(f" Day{i}'s high temp : "))
    temp_list.append(nextDay)
    average = sum(temp_list)/len(temp_list)
    i += 1
print('Average', average)

above = 0
for i in temp_list:
    if i>average:
        above +=1

print(str(above) + "day(s) above average") 