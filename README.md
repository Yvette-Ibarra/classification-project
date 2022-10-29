# Telco classification project

# Project Description:
Telco is a company that provides communication and media services to customers that include phone services, multiple phone lines, online security, online_backup, device protection, tech support services, streaming tv services, and streaming movies services. Within codeup database we have collected telco customer account information and customers demographics. I would like to look into drivers of customer churn and what actions can be put in place to prevent customer churn.

# Project Goal:
* Discover drivers of Telco customer churn
* Use drivers to develop a machine learning model to predict weather or not a Telco customer will churn.

# Initial Thoughts:
My initial hypothesis is that high monthly charges cause for a Telco customer to churn.

# The Plan
* Aquire data from codeup database

* Prepare data

* Explore data in search of drivers of upsets

  * Answer the following initial questions
    * How often does churn occur?
    * Do customer who churn have higher monthly charges?
    * Is the mean tenure of customers who churn lower?
    * Does having Senior Citizen status affect churn?
    * Does contract type affect churn?
    * Does having a partner affect churn?
    * Does gender affect churn?
   
  
    
* Develop a Model to predict if a chess game will end in an upset

    * Use drivers identified in explore to build predictive models of different types
    * Evaluate models on train and validate data
    * Select the best model based on highest accuracy
    * Evaluate the best model on test data
    
* Draw conclusions



# Data Dictionary

| Feature | Definition |
| --- | --- |
| Gender | Whether a customer is male or female |
| Senior Citizen | Whether a customer is Senior Citizen (1) or not (0) |
| Partner | Whether the customer has a partner or not |
| Dependents | Whether the customer has dependents or not |
| Tenure | Number of months the customer has stayed with the company |
| PhoneService | Whether the customer has a phone service or not |
| MultipleLines | Whether the customer has multiple lines or not (Yes, No, No phone service)|
| InternetService | Customer’s internet service provider (DSL, Fiber optic, No internet srvice)|
| OnlineSecurity | Whether the customer has online security or not (Yes, No, No internet service) |
| Additional Features | Encoded and values for categorical data and scaled versions continuous data|




# Steps to Reproduce
1. Clone this repository
2. Get Telco Churn data from Codeup Database:
  * Must have acess to Codeup Database 
  * Save a copy env.py file containing codeups: hostname, username and password
  * Save file in cloned repository
3. Run notebook

# Takeaways and Conclusions
* About 26.5% of Telco customers churn.
* Customers who churn tend to:
    * have a higher a monthly charge
    * lower tenure mean
* Contract type, partner status and senior status have an association with churn
* Gender has no influence on churn


# Recommendations
* Have appealing incentives for customers to sign a two-year contract.
* Run a promotion to lower monthly charges for new customers.
* Give discounts to senior citizens