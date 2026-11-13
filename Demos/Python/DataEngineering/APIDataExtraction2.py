
import requests
import pandas as pd

from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

API_URL = "https://jsonplaceholder.typicode.com/posts"

# Step 1: Configure retries
retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"],
    respect_retry_after_header=True
)

adapter = HTTPAdapter(max_retries=retry_strategy)

session = requests.Session()
session.mount("https://", adapter)

all_posts = []
page = 1
page_size = 20

try:
    while True:

        # Step 2: Request one page
        response = session.get(
            API_URL,
            params={
                "_page": page,
                "_limit": page_size
            },
            timeout=15
        )

        response.raise_for_status()

        # Step 3: Parse JSON
        posts = response.json()

        if not isinstance(posts, list):
            raise ValueError("Expected a list of posts")

        # Step 4: Stop when no records remain
        if not posts:
            break

        all_posts.extend(posts)

        print(
            f"Page {page}: Retrieved {len(posts)} records"
        )

        # Step 5: Stop after the last page
        if len(posts) < page_size:
            break

        page += 1

    # Step 6: Convert to DataFrame
    df = pd.DataFrame(all_posts)

    # Step 7: Remove duplicates
    df = df.drop_duplicates(subset=["id"])

    # Step 8: Export
    df.to_csv(
        "all_api_posts.csv",
        index=False
    )

    print("\nTotal Records:", len(df))
    print(df.head())

except requests.exceptions.RequestException as error:
    print("API Extraction Failed:", error)

except (ValueError, KeyError) as error:
    print("Invalid API Response:", error)

finally:
    session.close()
