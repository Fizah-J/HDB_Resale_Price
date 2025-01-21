import pandas as pd

# Paths to the CSV files
main_data_path = r""
unique_add_details_path = r""
output_path = r""

# Load the main data and unique address details
df_hdb_resale_price = pd.read_csv(main_data_path)
df_uniq_add = pd.read_csv(unique_add_details_path)

# Create new columns in the main data to hold postal, latitude, longitude, and region
df_hdb_resale_price['Postal'] = None
df_hdb_resale_price['Latitude'] = None
df_hdb_resale_price['Longitude'] = None

# Define the function that will process each address
def process_address(index, row):
    # Use the already existing 'address' column
    address = row['address']
    
    # Find matching rows in the unique addresses dataframe using substring matching
    matching_rows = df_uniq_add[df_uniq_add['Street Name'].str.contains(address.split()[0], na=False)]
    
    if not matching_rows.empty:
        # Further filtering for best match by checking keywords
        for _, match in matching_rows.iterrows():
            if address.lower() in match['Street Name'].lower():
                df_hdb_resale_price.at[index, 'Postal'] = match['Postal']
                df_hdb_resale_price.at[index, 'Latitude'] = match['Latitude']
                df_hdb_resale_price.at[index, 'Longitude'] = match['Longitude']
                break  # Break after first match
    
    # Print the current row for progress tracking
    print(f"Processed row {index + 1}")

# Iterate through each row in the dataframe to apply the address processing
for index, row in df_hdb_resale_price.iterrows():
    process_address(index, row)

# Save the updated dataframe to a new CSV file
df_hdb_resale_price.to_csv(output_path, index=False)

print("Merged data saved to:", output_path)
