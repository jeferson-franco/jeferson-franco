import re

import requests
from bs4 import BeautifulSoup

# Fetch the HTML content
url = "https://www.tiobe.com/tiobe-index/"
response = requests.get(url)
html_content = response.text

# Parse the HTML
soup = BeautifulSoup(html_content, "html.parser")


# Function to format rows into Markdown table format
def format_as_markdown_table(header, rows):
    markdown_table = "| " + " | ".join(header) + " |\n"
    markdown_table += "|-" * len(header) + "|\n"
    for row in rows:
        markdown_table += "| " + " | ".join(row) + " |\n"
    return markdown_table


# Extract and format the "top20" table
top20_table = soup.find("table", id="top20")
# Find the header row of the "top20" table
top20_table_header_row = top20_table.find("thead").find("tr")
# Extract the text of the first header cell
first_column_name = top20_table_header_row.find("th").text.strip()
# Use this extracted text as the first column name
top20_header = [first_column_name, "Programming Language", "Ratings"]
top20_rows = []
for row in top20_table.find_all("tr")[1:]:  # Skip header row
    cols = row.find_all("td")
    top20_rows.append(
        [cols[0].text.strip(), cols[4].text.strip(), cols[5].text.strip()]
    )
top20_markdown = format_as_markdown_table(top20_header, top20_rows)

# Extract and format the "otherPL" table
otherPL_table = soup.find("table", id="otherPL")
otherPL_header = ["Position", "Programming Language", "Ratings"]
otherPL_rows = []
for row in otherPL_table.find_all("tr")[1:]:  # Skip header row
    cols = row.find_all("td")
    otherPL_rows.append(
        [cols[0].text.strip(), cols[1].text.strip(), cols[2].text.strip()]
    )
otherPL_markdown = format_as_markdown_table(otherPL_header, otherPL_rows)

# Combine both tables
combined_markdown = top20_markdown + "\n" + otherPL_markdown

# Read the current README.md content
with open("README.md", "r") as file:
    readme_content = file.read()

# Replace the content between the TIOBE_TABLE tags
updated_readme = re.sub(
    r"<!-- TIOBE_TABLE_START -->.*?<!-- TIOBE_TABLE_END -->",
    f"<!-- TIOBE_TABLE_START -->\n{combined_markdown}<!-- TIOBE_TABLE_END -->",
    readme_content,
    flags=re.DOTALL,
)

# Write the updated content back to README.md
with open("README.md", "w") as file:
    file.write(updated_readme)
