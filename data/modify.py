import pandas as pd

# Load the CSV file
file_path = "./original.csv"
df = pd.read_csv(file_path)

# Define customer mapping
customers = [
    "customer00",
    "customer01",
    "customer02",
    "customer03",
    "customer04",
    "customer05",
    "customer06",
    "customer07",
    "customer08",
    "customer09",
    "customer10",
    "customer11",
    "customer12",
    "customer13",
]

# Convert into user-centric format
records = []
for _, row in df.iterrows():
    for idx, customer in enumerate(customers):
        consumption_col = f"{customer}_cons_kWh"
        production_col = f"{customer}_prod_kWh"
        consumption_kwh = row[consumption_col] if consumption_col in df.columns else 0
        production_kwh = row[production_col] if production_col in df.columns else 0
        records.append(
            {
                "timestamp_utc": row["timestamp_utc"],
                "SIPX_EUR_kWh": row["SIPX_EUR_kWh"],
                "customer": customer,
                "consumption_kwh": consumption_kwh,
                "production_kwh": production_kwh,
            }
        )

# Create a DataFrame and Save
df_transformed = pd.DataFrame(records)
df_transformed.to_csv("transformed_energy_data.csv", index=False)
