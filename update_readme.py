import sys, os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":

    load_dotenv()
    session_cookie = os.getenv("AOC_COOKIE")
    if not session_cookie:
        print("No cookie found in .env file")
        sys.exit(1)

    url = "https://adventofcode.com"
    page = requests.get(url, cookies={"session": session_cookie})
    soup = BeautifulSoup(page.content, "html.parser")
    
    days = [0] * 25

    for day in range(1, 26):
        # Get a with class calnder-day{i}
        day_link = soup.find("a", class_=f"calendar-day{day}")
        # Get parameter aria-label
        if day_link:
            aria_label = day_link["aria-label"]
            if ("one star" in aria_label):
                days[day - 1] = 1
            elif ("two stars" in aria_label):
                days[day - 1] = 2

    with open("../README.md", "r", encoding="utf-8") as f:
        lines = f.read()
        idx = lines.index('Progress:') - 1
        text, progress = lines[:idx+1], lines[idx+1:]
        progressEmoji = "⬛🟨🟩"
        progressBar = ""
        for v in days:
            progressBar += progressEmoji[v]
        days_completed = progressBar.count("🟩")
        print(progressBar)

    with open("../README.md", "w", encoding="utf-8") as f:
        f.write(text)
        f.write(f"Progress: {days_completed}/25\n")
        f.write("".join(progressBar))
        f.write("\n```")