import pandas as pd
pd.set_option('display.max_columns', None)

data = pd.read_csv('../fraud-card-transactions.csv')

dataset_first_rows = data.head()
dataset_last_rows = data.tail()
dataset_info = data.info

missing_values = data.isnull().any(axis=1)
duplicate_rows = data[data.duplicated()]

print("Missing values from the dataset:")
print(missing_values)

print("Duplicated rows from the dataset:")
print(duplicate_rows)

chip_pin_df = data[["used_chip", "used_pin_number", "fraud"]]
total_transactions = len(chip_pin_df)
total_fraud = chip_pin_df["fraud"].sum()
total_fraud_by_chip = chip_pin_df[chip_pin_df["used_chip"] == 1]["fraud"].sum()
total_fraud_by_pin = chip_pin_df[chip_pin_df["used_pin_number"] == 1]["fraud"].sum()

print("Total transactions: ", total_transactions)
print("Total frauds: ", total_fraud)
print("Fraud cases using chip: ", total_fraud_by_chip)
print("Fraud cases using pin number: ", total_fraud_by_pin)