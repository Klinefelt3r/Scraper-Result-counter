from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Define the URL
url = 'https://www.stanica.sk/program/'

# Set up Chrome options (headless or not)
options = Options()
options.headless = False  # Set to True to run in headless mode
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)
driver.get(url)

# Wait for the events to load (up to 10 seconds)
try:
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'tt-evt-li__event-info')))
    events = driver.find_elements(By.CLASS_NAME, 'tt-evt-li__event-info')
except TimeoutException:
    print("Timed out waiting for events to load")
    driver.quit()

# Loop through the events and extract the required details
event_details = []

for event in events:
    try:
        # Extract the event title
        event_title = event.find_element(By.CLASS_NAME, 'tt-evt-li__name').text
    except:
        event_title = "N/A"
    
    try:
        # Extract the event date and time
        event_date_time = event.find_element(By.CLASS_NAME, 'tt-evt-li__sub-info elementor-repeater-item-ff3fa99 tt-evt-li__sub-info--BeginDateTime').text
    except:
        event_date_time = "N/A", "N/A"
    
    try:
        # Extract the number of dates the event spans over
        event_dates_count = event.find_element(By.CLASS_NAME, 'tt-evt-li__sub-info--BeginOrDatesCount').text
    except:
        event_dates_count = "N/A"
    
    # Append the event details to the list
    event_details.append({
        'Event Name': event_title,
        'Event Date and Time': event_date_time,
        'Event Dates Count': event_dates_count
    })

# Create a DataFrame from the event_details list
df = pd.DataFrame(event_details)

# Convert the DataFrame to a JSON string
json_data = df.to_json(orient='records')

# Print the JSON string
print("JSON Data:")
print(json_data)

# Convert the DataFrame to a CSV string
csv_data = df.to_csv(index=False)

# Print the CSV string
print("\nCSV Data:")
print(csv_data)

# Convert the DataFrame to a dictionary
dict_data = df.to_dict(orient='records')

# Print the dictionary
print("\nDictionary Data:")
print(dict_data)

# Close the browser once šicko v poradku
driver.quit()