# anonymize and select sheets
# the original dataframes are no longer accessible as I've removed them for obvcious anonymity reasons but the anonymized dataframes are still accessible
# versions are

import pandas as pd
import numpy as np

# ALREADY anonymized
pd.read_csv("Data/Testimonies/SV_Feb. 14_for review.xlsx - Arabic.csv").head(5)

# still need to anonymize
# read the workbooks
x_79 = pd.ExcelFile("Data/Testimonies/ القضية  79 .xlsx")
x_81 = pd.ExcelFile("Data/Testimonies/Case_81.xlsx")
x_123 = pd.ExcelFile("Data/Testimonies/Case_123.xlsx")
x_165 = pd.ExcelFile("Data/Testimonies/Case_165.xlsx")
x_16850 = pd.ExcelFile("Data/Testimonies/Case_16850.xlsx")
x_helwan = pd.ExcelFile("Data/Testimonies/كتائب حلوان.xlsx")

# sheet names- we need torture and detention conditions because that's where the testimonies are
x_79.sheet_names

torture_79 = x_79.parse("التعذيب")
torture_81 = x_81.parse("التعذيب")
torture_123 = x_123.parse("التعذيب")
torture_165 = x_165.parse("التعذيب")
torture_16850 = x_16850.parse("التعذيب")
torture_helwan = x_79.parse("التعذيب")

x_helwan.sheet_names

# this was a pain because some have a hamza and some don't
# dacritics make working with Arabic text way more difficult
detention_79 = x_79.parse('اوضاع اماكن الأحتجاز')
detention_81 = x_81.parse('أوضاع أماكن الاحتجاز')
detention_123 = x_123.parse('أوضاع اماكن الأحتجاز')
detention_165 = x_165.parse('أوضاع أماكن الاحتجاز')
detention_16850 = x_16850.parse('أوضاع أماكن الاحتجاز')
detention_helwan = x_helwan.parse('أوضاع اماكن الأحتجاز')

# add all dataframes to one list
group_df = [torture_79, torture_81, torture_123, torture_165, torture_16850, torture_helwan,\
     detention_79, detention_81, detention_123, detention_165, detention_16850, detention_helwan]

# remove names
for i in group_df:
    if 'الإسم' in i.columns:
        i.drop('الإسم', axis=1, inplace=True)
    elif 'الاسم' in i.columns:
        i.drop('الاسم', axis=1, inplace=True)

# make csvs

for i, _df in enumerate(group_df):
    print(i)
    filename = 'Data/Testimonies/testimonies_' + str(i) + '.csv'
    _df.to_csv(filename)