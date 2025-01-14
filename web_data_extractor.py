from bs4 import BeautifulSoup
import json

# Load the HTML content
html_content = "<html>...</html>"  # Replace with actual HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Configurations for data extraction
sections_config = {
    "service_offerings": {"tag": "h2", "class": "service-title"},
    "case_studies": {"tag": "h2", "class": "case-study-title"},
    "client_testimonials": {"tag": "blockquote", "class": None},
    "thought_leadership": {"tag": "h2", "class": "thought-leadership-title"},
    "market_insights": {"tag": "h2", "class": "market-insight-title"}
}

# Initialize the data structure
data = {key: [] for key in sections_config.keys()}

# Extract data based on configurations
for key, config in sections_config.items():
    tag = config["tag"]
    css_class = config["class"]
    elements = soup.find_all(tag, class_=css_class) if css_class else soup.find_all(tag)
    
    for element in elements:
        data[key].append(element.get_text(strip=True))

# Print the extracted data
print(json.dumps(data, indent=4))

# Save data to a JSON file
with open("extracted_data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)
