import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
import io

file_path = "517174.csv"

# Create a DataFrame from the data
df = pd.read_csv(file_path)

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Convert the 'Date' column to a datetime object
df['Date'] = pd.to_datetime(df['Date'])

# Feature engineering: Use the difference between High and Low prices as a feature
df['Price_Variation'] = df['High Price'] - df['Low Price']

# Use 'Price_Variation' as the input feature and 'Close' as the target variable
X = df[['Price_Variation']]
y = df['Close Price']


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Plot the actual vs predicted values
plt.scatter(X_test, y_test, color='black', label='Actual')
plt.plot(X_test, y_pred, color='blue', linewidth=3, label='Predicted')
plt.xlabel('Price Variation')
plt.ylabel('Close Price')
plt.legend()
plt.show()
