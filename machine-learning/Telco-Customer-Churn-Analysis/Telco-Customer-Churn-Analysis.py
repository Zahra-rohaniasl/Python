#Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


#1. Data prepration
#Load the dataset
file_path = '.../Telco-Customer-Churn-dataset.csv'
data = pd.read_csv(file_path)

#Info
print(data.head(10), data.info())

#missing values
print(data.isnull().sum())

#Changing nature of 'Total Charges' from object to numeric
data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')

#Fill NaN values in TotalCharges with median
data['TotalCharges'] = data['TotalCharges'].fillna(data['TotalCharges'].median())


# 2. Data analyzing

#Summarize the data
print(data.describe())


#Distribution of numerics
numerical_features = ['tenure', 'MonthlyCharges', 'TotalCharges']
for feature in numerical_features:
    sns.histplot(data[feature], kde=True, bins=30)
    plt.title(f'Distribution of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Frequency')
    plt.grid(True, axis='y', linestyle='--', alpha=0.7) 
    plt.show()

#Boxplots to identify outliers
for feature in numerical_features:
    sns.boxplot(x=data[feature])
    plt.title(f'Boxplot of {feature}')
    plt.xlabel(feature)
    plt.grid(True, axis='x', linestyle='--', alpha=0.7)
    plt.show()

#Distribution of categories
categorical_features = ['gender', 'Partner', 'Dependents', 'InternetService', 'Contract', 'PaymentMethod', 'Churn']
for feature in categorical_features:
    sns.countplot(data=data, x=feature, hue='Churn')
    plt.title(f'{feature} Distribution with Churn')
    plt.xlabel(feature)
    plt.ylabel('Count')
    plt.xticks(rotation=45, fontsize=7)
    plt.legend(title='Churn', loc='upper right')
    plt.show()

#Churn rate
churn_rate = data['Churn'].value_counts(normalize=True)
print('Churn rate:\n', churn_rate)

#Analyze churn by contact
contract_churn = data.groupby('Contract')['Churn'].value_counts(normalize=True).unstack()
print('Churn by contract: \n', contract_churn)


#Correlation
numeric_data = data.select_dtypes(include=['number'])
correlation_matrix = numeric_data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# 3. Predictive modeling
X = data.drop(columns=['Churn', 'customerID'])  # Exclude non-feature columns  
y = data['Churn'].map({'Yes': 1, 'No': 0})  # Binary encode Churn
X = pd.get_dummies(X, drop_first=True) 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))
