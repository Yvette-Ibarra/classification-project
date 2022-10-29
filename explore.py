import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

########################### CHURN RATE ###################################################

def get_churn_mean_bar(df):
    ''' This function takes in telco data frame and returns a histoplot that
    graphs the percentage of Telco customer who have churn'''
    
    sns.set(font_scale=1.3)  
    sns.set_style('white')
    
    c_percent = round(df.churn.value_counts(normalize=True)[1],3)* 100
    plt.title(f'Customers churn by {c_percent}%',fontsize=25,fontweight=100,color='midnightblue')
    sns.histplot(data =df, x='churn',stat='percent',hue='churn', palette='cubehelix')
    col_mean= round(df.churn.value_counts(normalize=True)[1],3)* 100
    plt.axhline(col_mean, label = 'Churn Rate',color='midnightblue',linestyle='dashed')
   
    plt.show();

########################### MONTHLY CHARGES #############################################

def get_monthly_charges(df):
   
    sns.set(font_scale=1.3)  
    sns.set_style('white')

    colors = ['#6BAF8E', '#E6AFC9']
    # Set your custom color palette
    sns.set_palette(sns.color_palette(colors))
    plt.title('Higher mean Monthly Charge',fontsize=25,fontweight=100,color='midnightblue')
    sns.boxplot(y=df.monthly_charges, x=df.churn,
                whis=np.inf
               )


def get_ttest_monthly_charges(df):
    
    # create two independent sample group of customers: churn and not churn.
    subset_churn =df[df.churn=='Yes']
    subset_notchurn = df[df.churn =='No']

    # # stats Levene test - returns p value. small p-value means unequal variances
    stat, pval =stats.levene(subset_churn.monthly_charges, subset_notchurn.monthly_charges)


    # high p-value suggests that the populations have equal variances
    if pval < 0.05:
        variance = False
    else:
        variance = True

    # set alpha to 0.05
    alpha = 0.05

    # perform T-test
    t_stat, p_val= stats.ttest_ind(subset_churn.monthly_charges, subset_notchurn.monthly_charges, equal_var = variance, random_state=123)
   
    # Round and print results
    t_stat = t_stat.round(4)
    p_val = (p_val.round(4))/2
    print(f' t-stat:{t_stat}')
    print(f' p-value/2:{p_val/2}')

############################## SENIOR CITIZENS ###################################

def get_bar_senior(df):
  
    plt.figure(figsize=(10,4))

    # change encoding of senior citizen to text
    senior= df.senior_citizen.map({1:'Yes', 0: 'No'})
    
    # Set your custom color palette and font size
    colors = ['#6BAF8E', '#E6AFC9']
    sns.set(font_scale=1.3)    
    sns.set_palette(sns.color_palette(colors))
    sns.set_style('white')
    
    plt.subplot(1,2,1)
    sns.countplot(x=senior, data= df, hue = 'churn')


    plt.subplot(1,2,2)
    sns.countplot(x=senior, data= df, hue = 'churn',dodge=False)

    # Title
    plt.suptitle('Senior Citizens Churn More',fontsize=25,fontweight=100,color='midnightblue')
    plt.show();

def get_chi2_senior(df):    
    # Chi-Square test to compare two categorical variables (senior citizen status, churn)

    # Set alpha to 0.05
    alpha = 0.05

    # Setup a crosstab of observed 
    observed = pd.crosstab(df.senior_citizen==1, df.churn)

    # Run Chi-Square test
    chi2, p, degf, expected = stats.chi2_contingency(observed)

    # Round and Print results
    chi2 = chi2.round(4)
    p = p.round(4)
    print(f' Chi-Square{chi2}')
    print(f' p-value:{p}')

############################################## TENURE #########################################
def get_boxplot_tenure(df):  

    sns.set(font_scale=1.3)  
    sns.set_style('white')

    # Set your custom color palette
    colors = ['#6BAF8E', '#E6AFC9']
    sns.set_palette(sns.color_palette(colors))

    plt.title('Lower mean tenure')
    sns.boxplot(y=df.tenure, x=df.churn,whis=np.inf);

def get_ttest_tenure(df):
    
    # create two independent sample group of customers: churn and not churn.
    subset_churn =df[df.churn=='Yes']
    subset_notchurn = df[df.churn =='No']

    # # stats Levene test - returns p value. small p-value means unequal variances
    stat, pval =stats.levene(subset_churn.tenure, subset_notchurn.tenure)


    # high p-value suggests that the populations have equal variances
    if pval < 0.05:
        variance = False
        print('False')
    else:
        variance = True
        print('True')

    # set alpha to 0.05
    alpha = 0.05

    # perform t-test
    t_stat, p_val = stats.ttest_ind(subset_churn.tenure, subset_notchurn.tenure, equal_var = variance,random_state=123)
    
    # round  and print results
    t_stat = t_stat.round(4)
    p_val = p_val.round(4)/2
    print(f' t-stat:{t_stat}')
    print(f' p-value/2:{p_val/2}')

################################ CONTRACT TYPE #########################################

def get_plot_contract(df):
    sns.set(font_scale=1.3)  
    sns.set_style('white')
    # Set your custom color palette
    colors = ['#6BAF8E', '#E6AFC9']
    sns.set_palette(sns.color_palette(colors))

    plt.title('Contract Type vs Churn')
    sns.countplot(x=df.contract_type, data=df, hue = 'churn');

def get_chi2_contract(df):    
    # Chi-Square test to compare two categorical variables (contract type, churn)
    # Set alpha to 0.05
    alpha = 0.05

    # Setup a crosstab of observed 
    observed = pd.crosstab(df.contract_type, df.churn)
    
    # Run chi-square test
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    
    # Round and Print Results
    chi2 = chi2.round(4)
    p = p.round(4)
    print(f' Chi-Square:{chi2}')
    print(f' p-value:{p}')

#################################### GENDER ###################################
def get_plot_gender(df):  

    sns.set(font_scale=1.3)  
    sns.set_style('white')

    # Set your custom color palette
    colors = ['#6BAF8E', '#E6AFC9']
    sns.set_palette(sns.color_palette(colors))

    plt.title('Gender Vs Churn')
    sns.countplot(x=df.gender, data=df, hue = 'churn')

    plt.legend()
    plt.show();

def get_chi2_gender(df):    
    # Chi-Square test to compare two categorical variables (gender, churn)
    # Set alpha to 0.05
    alpha = 0.05

    # Setup a crosstab of observed 
    observed = pd.crosstab(df.gender, df.churn)
    
    # Run chi-square test
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    
    # Round and Print Results
    chi2 = chi2.round(4)
    p = p.round(4)
    print(f' Chi-Square:{chi2}')
    print(f' p-value:{p}')

############################################# PARTNER ##################################

def get_plot_partner(df):  

    sns.set(font_scale=1.3)  
    sns.set_style('white')

    # Set your custom color palette
    colors = ['#6BAF8E', '#E6AFC9']
    sns.set_palette(sns.color_palette(colors))

    plt.title('Partner Vs Churn')
    sns.countplot(x=df.partner, data=df, hue = 'churn')

    plt.legend()
    plt.show();

def get_chi2_partner(df):    
    # Chi-Square test to compare two categorical variables (gender, churn)
    # Set alpha to 0.05
    alpha = 0.05

    # Setup a crosstab of observed 
    observed = pd.crosstab(df.partner, df.churn)
    
    # Run chi-square test
    chi2, p, degf, expected = stats.chi2_contingency(observed)
    
    # Round and Print Results
    chi2 = chi2.round(4)
    p = p.round(4)
    print(f' Chi-Square:{chi2}')
    print(f' p-value:{p}')