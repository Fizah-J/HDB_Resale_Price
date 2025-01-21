import requests
import csv
from concurrent.futures import ThreadPoolExecutor

# Function to query OneMap API and retrieve details for an address
def get_address_details(address):
    search_url = f"https://www.onemap.gov.sg/api/common/elastic/search?searchVal={address}&returnGeom=Y&getAddrDetails=Y&pageNum=1"
    try:
        response = requests.get(search_url, timeout=10)  # Set a timeout value (e.g., 10 seconds)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        data = response.json()
        if data.get("found"):
            return data["results"][0]
        else:
            return None
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

# Path to your unique address CSV file
input_path = r"C:\Users\fizah\Documents\WordPress Site\Data Analyst Site\unique_address.csv"
output_path = r"C:\Users\fizah\Documents\WordPress Site\Data Analyst Site\unique_add_details.csv"

# Open and read the CSV file
with open(input_path, mode='r', newline='', encoding='utf-8-sig') as infile:  # Using 'utf-8-sig' to handle BOM
    reader = csv.DictReader(infile)
    
    # Print the field names to debug the column headers
    print("Headers:", reader.fieldnames)
    
    # Manually inspect and print the first row to ensure data is being read correctly
    first_row = next(reader)
    print("First Row:", first_row)

    # Now, if the column name is correctly identified, proceed
    addresses = [row['unique_address'] for row in reader]  # Ensure 'street_name' is the correct column name

# Prepare data for output
output_data = [["Street Name", "Postal", "Latitude", "Longitude"]]  # Add headers

# Function to process address details
def process_address(address):
    address_details = get_address_details(address)
    if address_details:
        postal = address_details.get("POSTAL", "N/A")
        latitude = address_details.get("LATITUDE", "N/A")
        longitude = address_details.get("LONGITUDE", "N/A")
        
        # Append the original address and its details
        output_data.append([address, postal, latitude, longitude])  # Keep the original address
        print("Street Name:", address)
        print("Postal:", postal)
        print("Latitude:", latitude)
        print("Longitude:", longitude)
        print()
    else:
        print("Details not found for:", address)

# Number of threads (adjust as needed)
num_threads = 10

# Use ThreadPoolExecutor to parallelize the processing
with ThreadPoolExecutor(max_workers=num_threads) as executor:
    executor.map(process_address, addresses)

# Save the updated data to a new CSV file
with open(output_path, mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(output_data)

print("Updated CSV file saved to:", output_path)
