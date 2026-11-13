
import requests
import pandas as pd

API_URL = "https://jsonplaceholder.typicode.com/users"

try:
    # Step 1: Send GET request
    response = requests.get(
        API_URL,
        timeout=15
    )

    # Step 2: Validate HTTP response
    response.raise_for_status()

    # Step 3: Convert JSON response
    users = response.json()

    # Step 4: Convert to DataFrame
    df = pd.json_normalize(users)

    print("Total Users: ", len(df))

    # Step 5: Select required columns
    selected_columns = [
        "id",
        "name",
        "username",
        "email",
        "address.city",
        "company.name"
    ]

    df = df[selected_columns]

    # Step 6: Rename columns
    df = df.rename(columns={
        "id": "UserID",
        "name": "Name",
        "username": "Username",
        "email": "Email",
        "address.city": "City",
        "company.name": "Company"
    })

    # Step 7: Validate records
    df = df.drop_duplicates(subset=["UserID"])

    df = df.dropna(
        subset=["UserID", "Email"]
    )

    # Step 8: Display results
    print("\nExtracted User Data:")
    print(df.to_string(index=False))

    # Step 9: Export data
    df.to_csv(
        "api_users.csv",
        index=False
    )

    print("\nAPI Data Extracted Successfully!")

except requests.exceptions.RequestException as error:
    print("API Request Failed:", error)

except (ValueError, KeyError, TypeError) as error:
    print("API Data Processing Failed:", error)
