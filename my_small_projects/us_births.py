"""The dataset contains the following columns:

year: Year (1994 to 2003).
month: Month (1 to 12).
date_of_month: Day number of the month (1 to 31).
day_of_week: Day of week (1 to 7).
births: Number of births that day.


A program that produces the results of Births in US form 1999 to 2003. data is taken from a csv file 'US_births_1994-2003_CDC_NCHS.csv'"""


#introduction to dataset
csv_list = open("US_births_1994-2003_CDC_NCHS.csv").read().split("\n")

def read_csv(filename):                         #converting to list of lists
    string_data = open(filename).read()
    string_list = string_data.split("\n")[1:]
    final_list = []

    for row in string_list:
        string_fields = row.split(",")
        int_fields = []
        for value in string_fields:
            int_fields.append(int(value))
        final_list.append(int_fields)
    return final_list

cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")             #returns list of lists


def calc_counts(data, column):          #function which provides the result
    sums_dict = {}

    for row in data:
        col_value = row[column]
        births = row[4]
        if col_value in sums_dict:
            sums_dict[col_value] = sums_dict[col_value] + births
        else:
            sums_dict[col_value] = births
    return sums_dict

cdc_year_births = calc_counts(cdc_list, 0)          #returns result in a dictionary, total no.of births in year
cdc_month_births = calc_counts(cdc_list, 1)         #returns result in a dictionary, total no.of births in months
cdc_dom_births = calc_counts(cdc_list, 2)           #returns result in a dictionary, total no.of births in date of month(1.....31)
cdc_dow_births = calc_counts(cdc_list, 3)           #returns result in a dictionary, total no.of births in date of day(1...7)


