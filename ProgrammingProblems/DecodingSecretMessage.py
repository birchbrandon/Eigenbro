import requests
from bs4 import BeautifulSoup


def decode_message(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    table = soup.find("table")
    rows = table.find_all("tr")

    data = []
    for row in rows[1:]: 
        cols = row.find_all("td")
        x = int(cols[0].text.strip())
        char = cols[1].text.strip()
        y = int(cols[2].text.strip())
        data.append((x, char, y))

    max_x = max(data, key=lambda item: item[0])[0]
    max_y = max(data, key=lambda item: item[2])[2]

    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for x, char, y in data:
        grid[y][x] = char

    grid.reverse()

    for row in grid:
        print("".join(row))


def decode_message_debug(url):
    # Step 1: Fetch the content of the URL
    response = requests.get(url)
    print("Response received from URL")

    # Step 2: Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    print("HTML content parsed with BeautifulSoup")

    # Step 3: Find the table and extract rows
    table = soup.find("table")
    rows = table.find_all("tr")
    print(f"Found {len(rows) - 1} data rows in the table")

    # Step 4: Extract x, character, and y from each row
    data = []
    for index, row in enumerate(rows[1:], start=1): 
        cols = row.find_all("td")
        x = int(cols[0].text.strip())
        char = cols[1].text.strip()
        y = int(cols[2].text.strip())
        data.append((x, char, y))
        print(f"Row {index}: x = {x}, char = '{char}', y = {y}")

    # Step 5: Determine grid dimensions
    max_x = max(data, key=lambda item: item[0])[0]
    max_y = max(data, key=lambda item: item[2])[2]
    print(f"Grid dimensions: max_x = {max_x}, max_y = {max_y}")

    # Step 6: Create an empty grid
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    print("Empty grid created:")
    for row in grid:
        print("".join(row))

    # Step 7: Populate the grid with coordinate pairs
    for x, char, y in data:
        grid[y][x] = f"({x},{y})"
        print(f"Placed coordinates ({x},{y}) in place of '{char}'")

    print("Populated grid with coordinate pairs:")
    for row in grid:
        print(" ".join(row))

    # Step 8: Print the final grid
    print("\nFinal grid (as output):")
    for row in grid:
        print(" ".join(row))

# Example usage
url = "https://docs.google.com/document/d/e/2PACX-1vSHesOf9hv2sPOntssYrEdubmMQm8lwjfwv6NPjjmIRYs_FOYXtqrYgjh85jBUebK9swPXh_a5TJ5Kl/pub"  # Replace with the actual URL
decode_message(url)
