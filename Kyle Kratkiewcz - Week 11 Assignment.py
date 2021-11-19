#Create a single list that contains the following collection of data in the order provided
listA = [1121, "Jackie Grainger", 22.22,
 1122, "Jignesh Thrakkar", 25.25,
 1127, "Dion Green", 28.75, False,
 24.32, 1132, "Jacob Gerber",
 "Sarah Sanderson", 23.45, 1137, True,
 "Brandon Heck", 1138, 25.84, True,
 1152, "David Toma", 22.65,
 23.75, 1157, "Charles King", False,
 "Jackie Grainger", 1121, 22.22, False,
 22.65, 1152, "David Toma"]

listB = []
dict1 = {'Name':'', 'Information':int, 'Wage':float, 'Total_Hourly_Rate':float}
dict2 = {'Name':'', 'Raise':float}
underpaid_salaries = []
company_raises = []
i = 0

#Assume that the above information is a small sample of the company's data. Programmatically sort the information into a list of dictionary items. Each dictionary must be in a database-like format.
while i < len(listA):

    for j in range(3):

        if type(listA[j+i]) == int:
           dict1['Information'] = listA[j+i]
        if type(listA[j+i]) == str:
           dict1['Name'] = listA[j+i]
        if type(listA[j+i]) == float:
           dict1['Wage'] = listA[j+i]

    #No duplicate data should make its way into the list of dictionary items.
    if dict1 not in listB:
    
        dict1_copy = dict1.copy()
        
        listB.append(dict1_copy)

    if i+3 < len(listA):
        if type(listA[i+3]) == bool:
            i = i + 1

    i = i + 3

#For each value in the list multiply the current hourly wage value by 1.3 (since benefits are about 30% of a person's salary) and add a key to each dictionary item called total_hourly_rate. Under that key, store the value you just calculated.
for i in range(len(listB)):
    listB[i]['Total_Hourly_Rate'] = round(listB[i]['Wage'] * 1.3, 2)

#Determine if anyone's total hourly rate is between 28.15 and 30.65. If they are, add stored dictionary information on the person to a new list called underpaid_salaries.
for i in range(len(listB)):
    if listB[i]['Total_Hourly_Rate'] > 28.15 and listB[i]['Total_Hourly_Rate'] < 30.65:
        underpaid_salaries.append(listB[i])

#For each value in the dictionary, calculate a raise in dollars
for i in range(len(listB)):
    dict2['Name'] = listB[i]['Name']
    if listB[i]['Wage'] > 22 and listB[i]['Wage'] < 24:
        dict2['Raise'] = round(listB[i]['Wage'] * 1.05, 2)
    elif listB[i]['Wage'] > 24 and listB[i]['Wage'] < 26:
        dict2['Raise'] = round(listB[i]['Wage'] * 1.04, 2)
    elif listB[i]['Wage'] > 26 and listB[i]['Wage'] < 28:
        dict2['Raise'] = round(listB[i]['Wage'] * 1.03, 2)
    else:
        dict2['Raise'] = round(listB[i]['Wage'] * 1.02, 2)
    
    #Add to a new list called company_raises the name of the employee and the raise you calculated for each person. This information will be stored as a dictionary in database-like format. 
    dict2_copy = dict2.copy()
    company_raises.append(dict2_copy)

#Print out the data in all three lists you generated for this assignment.
print("Organized Data:", listB)
print()
print("Underpaid Salaries:", underpaid_salaries)
print()
print("Company Raises", company_raises)