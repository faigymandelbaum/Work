
import csv
import pandas as pd

class Employee:

    def __init__(self, employee_information):
        self.employee_path = employee_information

        # Reading in a csv file as a list of lists
        with open (self.employee_path, encoding = 'UTF-8') as f:
            reader = csv.reader(f)
            rows = list(reader)
        self.header = rows[0]
        self.rows = rows[1:] 

        # Instantiating a dictionary with the countries as keys and the rest of the information as values. 
        self.employees_by_country = {}
        for row in self.rows:
            if row[3] in self.employees_by_country:
                self.employees_by_country[row[3]] += [row[:3] + row[4:]]
            else:
                self.employees_by_country[row[3]] = [row[:3] + row[4:]]

        # Creating a set of industries to enable customers to see the different types in a organized list.
        self.industries = set()
        for row in rows:
            self.industries.add(row[2])

        # Sorting the company names in a list
        self.sorted_company_names = []
        for row in self.rows:
            self.sorted_company_names.append(row[1])
        self.sorted_company_names = sorted(self.sorted_company_names)

        self.employees_df = pd.DataFrame(self.rows, columns = self.header)

    # This function does a binary search on the companies and returns the rank of the company that was given.
    def list_binsearch_lookup(self, target_name, sorted_names):
        range_start = 0
        range_end = len(sorted_names) - 1
        while range_start < range_end:
            range_middle = (range_end + range_start) // 2
            name = sorted_names[range_middle]
            if name == target_name:
                for row in self.rows:
                    if row[1] == name:
                        return row[0]
            elif name < target_name:
                range_start = range_middle + 1
            else:
                range_end = range_middle - 1
        if sorted_names[range_start] != target_name:
            return False
        else:
            for row in self.rows:
                if row[1] == target_name:
                    return row[0]

    # This function does the same as above (binary search on the rank) with a pandas dataframe.
    def dataframe_binsearch_lookup(self, df, sorted_names, target_name):
        range_start = 0
        range_end = len(sorted_names) - 1
        while range_start < range_end:
            range_middle = (range_end + range_start) // 2
            name = sorted_names[range_middle]
            if name == target_name:
                return df['RANK'][df['NAME'] == target_name]
            elif name < target_name:
                range_start = range_middle + 1
            else:
                range_end = range_middle - 1
        if sorted_names[range_start] != target_name:
            return False
        else:
            return df['RANK'][df['NAME'] == target_name] 





