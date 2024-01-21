import os
import requests
from dotenv import load_dotenv

def get_input(year: int, day: int) -> str:
    """Get the input for a given year and day.
    
    Uses a predownloaded input file if available, otherwise downloads the input.
    """
    if not os.path.exists(f"inputs/{year}/{day}.txt"):
        # Download the input
        load_dotenv()
        session = requests.Session()
        cookie_content = os.getenv("SESSION_COOKIE")
        if cookie_content is None:
            raise ValueError("No session cookie found")
        session.cookies.set("session", os.getenv("SESSION_COOKIE"))
        response = session.get(f"https://adventofcode.com/{year}/day/{day}/input")
        response.raise_for_status()
        os.makedirs(f"inputs/{year}", exist_ok=True)
        with open(f"inputs/{year}/{day}.txt", "w") as f:
            f.write(response.text)
    with open(f"inputs/{year}/{day}.txt") as f:
        return f.readlines()
