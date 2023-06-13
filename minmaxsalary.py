#Average Salary Excluding the Minimum and Maximum Salary

import sys
def average(salary) -> float:
        minimum = salary[0]
        maximum = salary[0]
        sum = 0
        for i in range(1, len(salary)):
            if salary[i] > maximum:
                maximum = salary[i]
            elif salary[i] < minimum:
                minimum = salary[i]
        salary.remove(minimum)
        salary.remove(maximum)
        for sal in salary:
            sum += sal
        averageval = sum/len(salary)
        return averageval
salary = [4000,3000,1000,2000]
print(average(salary))