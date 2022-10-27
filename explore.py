import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

def get_churn_mean_bar(df):
    ''' This function takes in telco data frame and returns a histoplot that
        graphs the percentage of Telco customer who have churn
    '''
   
    c_percent = round(df.churn.value_counts(normalize=True)[1],3)* 100
    plt.title(f'Customers churn by {c_percent}%')
    sns.histplot(data =df, x='churn',stat='percent',hue='churn', palette='cubehelix')
    col_mean= round(df.churn.value_counts(normalize=True)[1],3)* 100
    plt.axhline(col_mean, label = 'Churn Rate',color='darkblue',linestyle='dashed')
   
    plt.show();

def get_monthly_charges(df):
    plt.title('Monthly Charges vs Churn')
    sns.boxplot(y=df.monthly_charges, x=df.churn,
                whis=np.inf, palette='cubehelix'
               )


def get_ttest_monthly_charges(df):
    
    # create two independent sample group of customers: churn and not churn.
    subset_churn =df[df.churn=='Yes']
    subset_notchurn = df[df.churn =='No']

    # # stats Levene test - returns p value. small p-value means unequal variances
    stat, pval =stats.levene(subset_churn.monthly_charges, subset_notchurn.monthly_charges)


    # high p-value suggests that the populations have equal variances
    if pval < 0.05:
        variance = True
    else:
        variance = False

 
    alpha = 0.05

    t_stat, p_val = stats.ttest_ind(subset_churn.monthly_charges, subset_notchurn.monthly_charges, equal_var = True, random_state=123)
    t_stat = t_stat.round(4)
    p_val = p_val.round(4)
    print(f' t-stat:{t_stat}')
    print(f' p-value:{p_val}')


def get_bar_senior(df):
    plt.figure(figsize=(12,6))


    plt.subplot(1,2,1)
    plt.title('senior vs churn')
    sns.countplot(x=df.senior_citizen, data=df, hue = 'churn',palette='cubehelix')


    plt.subplot(1,2,2)
    plt.title('Overlay senior vs churn')
    sns.countplot(x=df.senior_citizen, data=df, hue = 'churn',dodge=False,palette='cubehelix')
    plt.show()