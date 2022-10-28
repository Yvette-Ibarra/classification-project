from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def model_prep(train,validate,test):
    
    ''' This function takes in data that has been split into train, validate and test and prepares for modeling 
        by removing features not used for modeling and seperating the target variable into its own dataframe.
        The following features are keept for modeling: 'monthly_charges','senior_citizen','tenure', 'partner_No',
        'partner_Yes','churn','contract_type_Month-to-month','contract_type_One year','contract_type_Two year', 
        Six data frames seperating the target variale from the selected features per train, validate and test 
        are returned
    '''
    
    # drop unused columns 
    features = ['monthly_charges','senior_citizen','tenure','partner_No','partner_Yes','churn','contract_type_Month-to-month','contract_type_One year','contract_type_Two year']


    train = train[features]
    validate = validate[features]
    test = test[features]
        
    #seperate target
    x_train = train.drop(columns=['churn'])
    y_train = train.churn

    x_validate = validate.drop(columns=['churn'])
    y_validate = validate.churn

    x_test = test.drop(columns=['churn'])
    y_test = test.churn
        
    # Convert binary categorical targer variable to numeric
    y_train.churn= train.churn.map({'Yes': 1, 'No': 0})
    y_validate.churn = validate.churn.map({'Yes': 1, 'No': 0})
    y_test.churn = test.churn.map({'Yes': 1, 'No': 0})
        
    return x_train,y_train,x_validate,y_validate, x_test, y_test

def get_tree_model(x_train,y_train,x_validate,y_validate):
    ''' This function takes in train data and validate data and returns models accuracy score.
        Train data  is used tofit Decision Tree Model. Both train and validate data is used
        to return the accuracy score of the Decision Tree Model
    '''
    
    # Set Decision tree parameters
    tree = DecisionTreeClassifier(max_depth=3, random_state=123)

    # Use train data to fit model
    tree = tree.fit(x_train, y_train)

    # Print accuracy score for train and validate data
    print(f'Accuracy of Decision Tree on train data is {tree.score(x_train, y_train)} about {round(tree.score(x_train, y_train)*100,2)}%')
    print(f'Accuracy of Decision Tree on validate data is {tree.score(x_validate, y_validate)}about {round(tree.score(x_validate, y_validate)*100,2)}%')

def get_random_forest_model(x_train,y_train,x_validate,y_validate):
    ''' This function takes in train data and validate data and returns models accuracy score.
        Train data  is used to fit Random Forest Model. Both train and validate data is used
        to return the accuracy score of the Random Forest Model
    '''
    
    # Set Random Forest Model parameters
    random_forest = RandomForestClassifier(max_depth=8, min_samples_leaf = 9 , random_state=123)
   
    # Use train data to fit Random Forest model
    random_forest = random_forest.fit(x_train, y_train)
    
    print(f'Accuracy of Random Forest on train data is {random_forest.score(x_train, y_train)} about {round(random_forest.score(x_train, y_train)*100,2)}%')
    print(f'Accuracy of Random Forest on validate data is {random_forest.score(x_validate, y_validate)} about {round(random_forest.score(x_validate, y_validate)*100,2)}%')
