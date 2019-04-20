
# Python script to calculate spearman's constant and pearson's constant

# imports

import pandas as pd
from scipy.stats import spearmanr
import numpy as np
import matplotlib.pyplot as plt


colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0',
          '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000',
          '#ffd8b1', '#000075', '#808080', '#ffffff', '#000000']




# This function removes  % from a string
def strip_percentage_and_return_num(str):
    return int(str.strip("%"))


# function converts fraction to percentage
def fraction_to_percentage(str):
    return int(str)*100


# This function returns the project rows matched with the string
def dataframe_of_a_specific_project(df, str):
    return df[df['Unnamed: 0'].str.contains(str)]



# file name
file = "data.xlsx"
df = pd.read_excel(file)

print(list(df))
df = df[['Unnamed: 0', 'Statement Coverege', 'Branch Coverage', 'McCabe Complexity', 'Instruction Coverage']]
df = df.dropna()

# List of projects
projects = ["Jfree", "CommonIO", "CommonColle", "File", "SlingApi"]

for project in projects:

    # Getting the branch coverage, instruciton coverage, and McCabe complexity rows corresponding to all the projects.
    df_jfree = dataframe_of_a_specific_project(df, project)
    df_jfree_mccabe_list = df_jfree["McCabe Complexity"].tolist()
    df_jfree_branch_coverage_list = df_jfree['Branch Coverage'].tolist()
    df_jfree_instruction_coverage_list = df_jfree['Instruction Coverage'].tolist()

    if "%" in str(df_jfree_branch_coverage_list[0]):
        df_jfree_branch_coverage_list_without_percentage = list(map(lambda x: strip_percentage_and_return_num(x), df_jfree_branch_coverage_list))
    else:
        df_jfree_branch_coverage_list = list(map(lambda x: fraction_to_percentage(x), df_jfree_branch_coverage_list))

    if "%" in str(df_jfree_instruction_coverage_list[0]):
        df_jfree_instruction_coverage_list_without_percentage = list(map(lambda x: strip_percentage_and_return_num(x), df_jfree_instruction_coverage_list))
    else:
        df_jfree_instruction_coverage_list = list(map(lambda x: fraction_to_percentage(x), df_jfree_instruction_coverage_list))

    # Calculating spearman constant for each of the projects
    print("\n"+project+" Spearman"+"\n")
    print(spearmanr(df_jfree_branch_coverage_list_without_percentage, df_jfree_mccabe_list)[0])
    print(spearmanr(df_jfree_instruction_coverage_list_without_percentage, df_jfree_mccabe_list)[0])


    print("p value branch-complexity" , spearmanr(df_jfree_branch_coverage_list_without_percentage, df_jfree_mccabe_list)[1])
    print("p value statement-complexity", spearmanr(df_jfree_instruction_coverage_list_without_percentage, df_jfree_mccabe_list)[1])

    # Plotting graphs for the data points for each of the projects.
    plt.scatter(df_jfree_branch_coverage_list_without_percentage, df_jfree_mccabe_list, c="#000000")
    plt.title(project+": Branch vs complexity")
    z = np.polyfit(df_jfree_branch_coverage_list_without_percentage, df_jfree_mccabe_list, 1)
    p = np.poly1d(z)
    plt.plot(df_jfree_branch_coverage_list_without_percentage, p(df_jfree_branch_coverage_list_without_percentage), "r--")
    plt.show()

    plt.scatter(df_jfree_instruction_coverage_list_without_percentage, df_jfree_mccabe_list, c="#000000")
    plt.title(project+": instruction vs complexity")
    z = np.polyfit(df_jfree_instruction_coverage_list_without_percentage, df_jfree_mccabe_list, 1)
    p = np.poly1d(z)
    plt.plot(df_jfree_instruction_coverage_list_without_percentage, p(df_jfree_instruction_coverage_list_without_percentage),
             "r--")
    plt.show()











