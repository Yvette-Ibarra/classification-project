import os
import pandas as pd

import numpy as np


import env

# train test split from sklearn
from sklearn.model_selection import train_test_split
# imputer from sklearn
# help with missing value by replacing blank with: median, mode, average, calculate using other column
from sklearn.impute import SimpleImputer


def new_telco_data():
    '''
    This function retrieves telco_churn data from codeup database using an 
    sql query, converts telco_churn data into a dataframe and returns 
    telco_churn data as a data frame as df.
    '''
    # create sql query to get telco churn from codeup database
    sql_query = """
                select * from customers
                join contract_types using (contract_type_id)
                join internet_service_types using (internet_service_type_id)
                join payment_types using (payment_type_id)
                """
    
    # Read in DataFrame from Codeup db.
    df = pd.read_sql(sql_query, env.get_connection('telco_churn'))
    
    return df

def get_telco_data():
    '''
    This function checks to see if user has telco.csv, reads telco.csv and c
    converts csv into data frame df. Returns df

    If user does not have telco.csv this function will use new_telco_data() to retrieve
    telco data and convert to data frame df. Returns df
    
    '''
    # obtain csv file
    if os.path.isfile('telco.csv'):
        
        # If csv file exists read in data from csv file.
        df = pd.read_csv('telco.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame
        df = new_telco_data()
        
        # Cache data
        df.to_csv('telco.csv')
        
    return df



def prep_telco(df):
    '''
    This function takes in dataframe and 
    drops columns:'payment_type_id', 'internet_service_type_id', 'contract_type_id''customer_id 
    Removes 11 observations of white space in the total charges and changes
    total charges column to numeric type

    create dummy data for  categorical columns, drop_first set to False: 'senior_citizen'gender',
    'partner','dependents','phone_service','multiple_lines','online_security','online_backup',
    'device_protection', 'tech_support', 'streaming_tv','streaming_movies','paperless_billing', 
    'total_charges', 'churn','contract_type', 'internet_service_type', 'payment_type'
     and Concatenate dummy_df to original data frame
    '''

    # drop columns with redundant information 'payment_type_id', 'internet_service_type_id', 'contract_type_id' 
    # drop columns with unuseful information 'customer_id'

    df = df.drop(columns=['payment_type_id', 'internet_service_type_id', 'contract_type_id','customer_id'])
    

    # remove 11 observations in total_charges that have null values and convert to numeric type
    df = df[df.total_charges != ' ']

    # convert column to numeric type
    df.total_charges = df.total_charges.astype('float')
    
    #convert total_charges to numeric data
    df.total_charges = df.total_charges.replace(' ', np.nan).astype(float)

    # encode categorical drop_first set to False 'senior_citizen'gender','partner','dependents','phone_service','multiple_lines','online_security','online_backup','device_protection', 'tech_support','streaming_tv','streaming_movies','paperless_billing', 'total_charges', 'churn','contract_type','internet_service_type','payment_type'
    dummy_df = pd.get_dummies(df[[
                                    'gender','partner',
                                    'dependents',
                                    'phone_service',
                                    'multiple_lines',
                                    'online_security',
                                    'online_backup',
                                    'device_protection', 
                                    'tech_support',
                                    'streaming_tv',
                                    'streaming_movies',
                                    'paperless_billing',
                                    
                                    'contract_type',
                                    'internet_service_type',
                                    'payment_type']], dummy_na=False)

    
    # Concatenate dummy_df to original data frame
    df = pd.concat([df, dummy_df], axis=1)
    
    return df

def split_telco_data(df):
    '''
    This function split telco data into train , validate, test and  stratifies on churn.
    The split is 20% test 80% train/validate. Then 30% of 80% validate and 70% of 80% train.
    Aproximately (train 56%, validate 24%, test 20%)
    Returns train, validate, and test 
    '''
    # split test data from train/validate
    train_validate, test = train_test_split(df, test_size=.2, 
                                        random_state=123, 
                                        stratify=df.churn)

    # split train from validate
    train, validate = train_test_split(train_validate, test_size=.3, 
                                   random_state=123, 
                                   stratify=train_validate.churn)
                                   
    return train, validate, test




