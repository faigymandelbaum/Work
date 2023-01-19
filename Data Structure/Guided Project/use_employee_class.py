from  guided_project_class import Employee
import time

def main():
    print ('"Worlds Best Employers"')
    print ("Faigy MAndelbaum 1/19/2023")
    print('''My goals for this project are the following:
- Write efficient code to help users access the data easily.
- Save time and space while running the code.

Specific goals for the "Worlds Best Employers" dataset:
- Give the user information about employers in each country in an optimized way.
- Organize the different industries.
- Look up the ranks for the companies in the quickest way.''')
    
    my_employee = Employee("Worlds Best Employers.csv")

    print("Employees headers:")
    print(my_employee.header)

    print("Employees first three rows:")
    print(my_employee.rows[:3])

    print("We used a for loop in order to create a dictionary with the countries as keys, the values are lists of all the information of the companies in that country. This for loop saves time for all lookups from now on. Now we can find all the information by country just with calling the key.")
    print("An example of using the dictionary in order to get information about the United Kingdom:")
    print(my_employee.employees_by_country['United Kingdom'])

    print("We created a set of all industries to make it easier to check up all the different types and that way save time and space.")
    print("The set of industries:")
    print(my_employee.industries)

    print("First five sorted company names are:")
    print(my_employee.sorted_company_names[:5])

    print("2 examples of looking up a company with binary search:")
    print(my_employee.list_binsearch_lookup( 'Apple', my_employee.sorted_company_names) )
    print(my_employee.list_binsearch_lookup('Microsoft', my_employee.sorted_company_names,))

    print("Checking if the data frame was actually created. ")
    print(my_employee.employees_df.head())

    print("Using the binary search with a data frame.")
    print(my_employee.dataframe_binsearch_lookup(my_employee.employees_df, my_employee.sorted_company_names, 'IBM'))

    start=time.time()
    my_employee.dataframe_binsearch_lookup(my_employee.employees_df,my_employee.sorted_company_names, 'IBM')
    end=time.time()
    dataframe_time=end-start

    start=time.time()
    my_employee.list_binsearch_lookup('IBM', my_employee.sorted_company_names)
    end=time.time()
    list_time=end-start

    print("The time run with the data frame: " + str(dataframe_time))
    print("The time run with the list: " + str(list_time))
    print("After running the above codes and timing them, we find that looping through a list is faster than a data frame.(Even though the data frame function is shorter.)")
    print('''In conclusion:
Now the user could easily get information about employers in his country by just typing in the country name.
He can also find out the rank for a company by specifying the one he wants to know about.
There is a clear list of all industries.''')

main()    