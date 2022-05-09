import pandas as pd
import numpy as np
import glob

# set path and file name so we can pull all the csvs in the folder
path = 'Data/Testimonies/'
filenames = glob.glob(path + "/*.csv")

# read them all and assign them to their own dataframes
df_list = []
for f in filenames:
    f = pd.read_csv(f)
    df_list.append(f)

# make sure SV is specially broken out because its format is a little different
SV, testimonies_1, testimonies_2, testimonies_3, testimonies_4, testimonies_5, testimonies_6, testimonies_7,\
testimonies_8, testimonies_9, testimonies_10, testimonies_11, testimonies_12 = df_list

# keep just the testimonies of SV
SV_text = pd.DataFrame(SV['أقوال بالتعرض للتعذيب'])

# string together the texts of each dataframe into a single text series
text_1 = testimonies_1['الحبس الانفرادى'].str.cat(testimonies_1['الإضراب'], sep=' ', na_rep="")\
.str.cat(testimonies_1['التريض'], sep=' ', na_rep="")\
.str.cat(testimonies_1['الزيارات'], sep=' ', na_rep="")\
.str.cat(testimonies_1['الأكل'], sep=' ', na_rep="")\
.str.cat(testimonies_1['التهوية'], sep=' ', na_rep="")\
.str.cat(testimonies_1['سوء المعاملة'], sep=' ', na_rep="")\
.str.cat(testimonies_1['التكدس'], sep=' ', na_rep="")\
.str.cat(testimonies_1['الوضع الصحى'], sep=' ', na_rep="")

text_2 = testimonies_2['الوضع اصحي'].str.cat(testimonies_2['أقوال أخري عن الوضع الصحي '], sep=' ', na_rep="")\
.str.cat(testimonies_2['الحبس الإنفرادى'], sep=' ', na_rep="")\
.str.cat(testimonies_2['التريض'], sep=' ', na_rep="")\
.str.cat(testimonies_2['الزيارات'], sep=' ', na_rep="")\
.str.cat(testimonies_2['الأكل'], sep=' ', na_rep="")\
.str.cat(testimonies_2['التهوية'], sep=' ', na_rep="")\
.str.cat(testimonies_2['سوء المعاملة'], sep=' ', na_rep="")\
.str.cat(testimonies_2['التكدس'], sep=' ', na_rep="")\
.str.cat(testimonies_2['شكاوي أخري'], sep=' ', na_rep="")

text_3 = testimonies_3['تفريغ أقوالهم بالتعرض للتعذيب'].str.cat(testimonies_3['أقوال أخرى عن التعذيب'], sep=' ', na_rep="")\
.str.cat(testimonies_3['الكهرباء'], sep=' ', na_rep="")\
.str.cat(testimonies_3['التعليق'], sep=' ', na_rep="")\
.str.cat(testimonies_3['التهديد بالتعذيب وبالأهل'], sep=' ', na_rep="")

text_4 = testimonies_4['تفريغ أقوالهم بالتعرض للتعذيب'].str.cat(testimonies_4['مناظرة المتهم'], sep=' ', na_rep="")

text_5 = testimonies_5['الوضع اصحي'].str.cat(testimonies_5['الحبس الانفرادى'], sep=' ', na_rep="")\
.str.cat(testimonies_5['التريض'], sep=' ', na_rep="")\
.str.cat(testimonies_5['الزيارات'], sep=' ', na_rep="")\
.str.cat(testimonies_5['الأكل'], sep=' ', na_rep="")\
.str.cat(testimonies_5['التهوية'], sep=' ', na_rep="")\
.str.cat(testimonies_5['سوء المعاملة'], sep=' ', na_rep="")\
.str.cat(testimonies_5['التكدس'], sep=' ', na_rep="")\
.str.cat(testimonies_5['شكاوي اخري'], sep=' ', na_rep="")

text_6 = testimonies_6['الوضع الصحى'].str.cat(testimonies_6['الحبس الانفرادى'], sep=' ', na_rep="")\
.str.cat(testimonies_6['الحبس الانفرادى'], sep=' ', na_rep="")\
.str.cat(testimonies_6['التريض'], sep=' ', na_rep="")\
.str.cat(testimonies_6['الزيارات'], sep=' ', na_rep="")\
.str.cat(testimonies_6['الأكل'], sep=' ', na_rep="")\
.str.cat(testimonies_6['التهوية'], sep=' ', na_rep="")\
.str.cat(testimonies_6['سوء المعاملة'], sep=' ', na_rep="")\
.str.cat(testimonies_6['التكدس'], sep=' ', na_rep="")

text_7 = testimonies_7['تفريغ أقوالهم بالتعرض للتعذيب'].str.cat(testimonies_7['مناظرة المتهم'], sep=' ', na_rep="")\
.str.cat(testimonies_7['أقوال أخرى عن التعذيب'], sep=' ', na_rep="")\
.str.cat(testimonies_7['ملاحظات'], sep=' ', na_rep="")

text_8 = testimonies_8['تفريغ أقوالهم بالتعرض للتعذيب'].str.cat(testimonies_8['مناظرة المتهم'], sep=' ', na_rep="")\
.str.cat(testimonies_8['أقوال ٢'], sep=' ', na_rep="")

text_9 = testimonies_9['الوضع اصحي'].str.cat(testimonies_9['الحبس الإنفرادى'], sep=' ', na_rep="")\
.str.cat(testimonies_9['التريض'], sep=' ', na_rep="")\
.str.cat(testimonies_9['الزيارات'], sep=' ', na_rep="")\
.str.cat(testimonies_9['الأكل'], sep=' ', na_rep="")\
.str.cat(testimonies_9['التهوية'], sep=' ', na_rep="")\
.str.cat(testimonies_9['سوء المعاملة'], sep=' ', na_rep="")\
.str.cat(testimonies_9['التكدس'], sep=' ', na_rep="")\
.str.cat(testimonies_9['شكاوي اخري'], sep=' ', na_rep="")

text_10 = testimonies_10['تفريغ أقوالهم بالتعرض للتعذيب'].str.cat(testimonies_10['مناظرة المتهم'], sep=' ', na_rep="")\
.str.cat(testimonies_10['أقوال أخرى عن التعذيب'], sep=' ', na_rep="")

text_11 = testimonies_11['تفريغ أقوالهم بالتعرض للتعذيب'].str.cat(testimonies_11['مناظرة المتهم'], sep=' ', na_rep="")\
.str.cat(testimonies_11['أقوال أخرى عن التعذيب'], sep=' ', na_rep="")

text_12 = testimonies_12['الوضع الصحى'].str.cat(testimonies_12['الحبس الانفرادى'], sep=' ', na_rep="")\
.str.cat(testimonies_12['الحبس الانفرادى'], sep=' ', na_rep="")\
.str.cat(testimonies_12['التريض'], sep=' ', na_rep="")\
.str.cat(testimonies_12['الزيارات'], sep=' ', na_rep="")\
.str.cat(testimonies_12['الأكل'], sep=' ', na_rep="")\
.str.cat(testimonies_12['التهوية'], sep=' ', na_rep="")\
.str.cat(testimonies_12['سوء المعاملة'], sep=' ', na_rep="")\
.str.cat(testimonies_12['التكدس'], sep=' ', na_rep="")

# remove empty strings
texts = [text_1, text_2, text_3, text_4, text_5, text_6, text_7, text_8, text_9, text_10, text_11, text_12]

for i in texts:
    i.replace('^[ \t\r\n\s]*$', np.nan, regex=True, inplace=True)
    i.dropna(inplace=True)

#iterate through the texts list and stack them vertically
texts_stacked = pd.DataFrame(np.concatenate(texts), columns=["أقوال بالتعرض للتعذيب"])

testimonies = pd.concat([texts_stacked, SV_text], ignore_index=True)

testimonies.to_csv("testimonies.csv", index=False)