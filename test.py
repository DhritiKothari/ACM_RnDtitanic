import pandas as pd

# Load the tested.csv file
df = pd.read_csv("tested.csv")

# Display the first few rows
print(df.head())
# Get basic info
print(df.info())

# Show summary statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())
df = df[['PassengerId', 'Pclass', 'Sex', 'Age', 'Fare', 'Embarked']]
print(df.head())
first_class = df[df['Pclass'] == 1]
print(first_class.head())
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df.dropna(inplace=True)
