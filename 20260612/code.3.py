#PROGRAM TO CALCULATE SALARY OF AN EMPLOYEE
workHour=int(input("Enter the total work hours"))
overDuty = workHour-176
if (overDuty > 0):
    salaryAmount=(overDuty*200)+10000
    print(overDuty," RS")
else:
    print("6,000 RS")    