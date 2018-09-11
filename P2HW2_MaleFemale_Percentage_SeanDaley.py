#Chapter 2 Exercise #11 Male and Female Percentages page 78
#09/11/2018
#CTI-110 P2HW2 - Male Female Percentage
#Sean Daley
#

males=int(input("Enter number of males:"))
females=int(input("Enter number of females:"))

total=males+females

percentmale= males/total
percentfemale= females/total

print("Percent males:", end="")
print(format(percentmale,'.0%'))
print("Percent females:", end="")
print(format(percentfemale,'.0%'))
