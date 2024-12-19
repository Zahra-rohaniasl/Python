# Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import numpy as np
from imblearn.over_sampling import SMOTE
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# Load dataset
file_path = ".../heart-stroke-prediction-dataset.csv"
data = pd.read_csv(file_path)

### 1. Data Cleaning
# Null values
data = data.drop_duplicates()
data = data.dropna(subset=['bmi'])
data = data[data['smoking_status'] != 'Unknown']

# Map categorical columns to numeric for modeling
data['smoking_status'] = data['smoking_status'].map({'formerly smoked': 1, 'smokes': 1, 'never smoked': 0})


# Keep 'gender' as categorical for visualization
# Drop unnecessary columns
data.drop(columns=['id', 'work_type', 'Residence_type'], inplace=True)

# Print data headers
print(data.head(10))

### 2. Categorization
def categorize_glucose(glucose):
    if glucose < 80:
        return 'Below Normal'
    elif 80 <= glucose <= 100:
        return 'Normal'
    elif 101 <= glucose <= 125:
        return 'Impaired Glucose'
    else:
        return 'Diabetic'

def categorize_bmi(bmi):
    if bmi < 16:
        return 'Severe Thinness'
    elif 16 <= bmi < 17:
        return 'Moderate Thinness'
    elif 17 <= bmi < 18.5:
        return 'Mild Thinness'
    elif 18.5 <= bmi < 25:
        return 'Normal'
    elif 25 <= bmi < 30:
        return 'Overweight'
    elif 30 <= bmi < 35:
        return 'Obese Class I'
    elif 35 <= bmi < 40:
        return 'Obese Class II'
    else:
        return 'Obese Class III'

data['glucose_category'] = data['avg_glucose_level'].apply(categorize_glucose)
data['bmi_category'] = data['bmi'].apply(categorize_bmi)

# Convert smoking_status to integer type
data['smoking_status'] = data['smoking_status'].astype(int)

# Define features (X) and target (y)
X = data.drop(columns=['stroke'])
y = data['stroke']

# One-hot encode categorical variables
X = pd.get_dummies(X, drop_first=True)

### 3. Model Training
# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Oversampling to handle imbalance
smote = SMOTE(random_state=42)
X_train_sm, y_train_sm = smote.fit_resample(X_train, y_train)

# Train Decision Tree model
dt_model = DecisionTreeClassifier(max_depth=6, random_state=42)
dt_model.fit(X_train_sm, y_train_sm)

# Model Evaluation
y_pred = dt_model.predict(X_test)
print('Accuracy:', accuracy_score(y_test, y_pred))
print('\nClassification Report:\n', classification_report(y_test, y_pred))

### 4. Visualization
# Decision Tree Visualization
plt.figure(figsize=(10,10))
plot_tree(
    dt_model, feature_names=X.columns, class_names=['No Stroke', 'Stroke'], 
    filled=True, rounded=True, fontsize=5
)
plt.title('Decision Tree for Heart Stroke Prediction', fontsize=12)
plt.show()

# Age-Stroke Plot
sns.histplot(data, x='age', hue='stroke', kde=True, bins=20)
plt.title('Age Distribution by Stroke Occurrence')
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend(title='Stroke', labels=['No Stroke (0)', 'Stroke (1)'])
plt.show()

# BMI-Stroke Plot
sns.countplot(data=data, x='bmi_category', hue='stroke')
plt.title('Stroke by BMI Categories')
plt.xlabel('BMI Category')
plt.ylabel('Count')
plt.xticks(rotation=45, fontsize=8)
plt.legend(title='Stroke', labels=['No Stroke (0)', 'Stroke (1)'])
plt.show()

# Glucose-Stroke Plot
sns.countplot(data=data, x='glucose_category', hue='stroke')
plt.title('Stroke by Glucose Categories')
plt.xlabel('Glucose Category')
plt.ylabel('Count')
plt.legend(title='Stroke', labels=['No Stroke (0)', 'Stroke (1)'])
plt.show()

# Gender-Stroke Plot
sns.countplot(data=data, x='gender', hue='stroke')
plt.title('Stroke Distribution by Gender')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.legend(title='Stroke', labels=['No Stroke (0)', 'Stroke (1)'])
plt.show()


# Marriage-Stroke Plot
sns.countplot(data=data, x='ever_married', hue='stroke')
plt.title('Stroke Distribution by Marriage Status')
plt.xlabel('Marriage Status')
plt.ylabel('Count')
plt.legend(title='Stroke', labels=['No Stroke (0)', 'Stroke (1)'])
plt.show()
