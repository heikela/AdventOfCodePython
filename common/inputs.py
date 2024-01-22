import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup

_requests_session = None

def _get_session() -> requests.Session:
    """Get a requests session object.
    
    Uses a pre-existing session object if available, otherwise creates a new one.
    """
    global _requests_session
    if _requests_session is None:
        _requests_session = requests.Session()
        load_dotenv()
        cookie_content = os.getenv("SESSION_COOKIE")
        if cookie_content is None:
            raise ValueError("No session cookie found")
        _requests_session.cookies.set("session", os.getenv("SESSION_COOKIE"))
    return _requests_session

def get_input(year: int, day: int) -> str:
    """Get the input for a given year and day.

    Uses a predownloaded input file if available, otherwise downloads the input.
    """
    file_name = f"inputs/{year}/{day}.txt"
    if not os.path.exists(file_name):
        # Download the input
        session = _get_session()
        response = session.get(f"https://adventofcode.com/{year}/day/{day}/input")
        response.raise_for_status()
        os.makedirs(f"inputs/{year}", exist_ok=True)
        with open(file_name, "w") as f:
            f.write(response.text)
    with open(file_name) as f:
        return [line.rstrip("\n\r") for line in f.readlines()]

def get_test_snippet(year: int, day: int, block: int) -> str:
    """Get a particular test snippet from a task description.

    Caches on disk and uses a cached file if available.
    The blocks are defined as anything between <pre><code> and </code></pre> tags.
    The first block is block 0.
    """
    file_name = f"inputs/{year}/{day}_test_{block}.txt"
    if not os.path.exists(file_name):
        session = _get_session()
        response = session.get(f"https://adventofcode.com/{year}/day/{day}")
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        code_in_pre = [tag for tag in soup.find_all("code")
                       if tag.parent.name == "pre"]
        snippet = code_in_pre[block].text
        os.makedirs(f"inputs/{year}", exist_ok=True)
        with open(file_name, "w") as f:
            f.write(snippet)
    with open(file_name) as f:
        return [line.rstrip("\n\r") for line in f.readlines()]
