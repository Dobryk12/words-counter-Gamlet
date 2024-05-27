import csv
import re
from collections import Counter
from dataclasses import dataclass
import bs4
import aiohttp
import asyncio


@dataclass
class Course:
    word: str
    count: int


BASE_URL = "https://www.ukrlib.com.ua/world/printit.php?tid=2&page="

URLS = [BASE_URL + str(i) for i in range(1, 16)]


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


def remove_punctuation_and_digits(text: str) -> str:
    return re.sub(r"[^\w\s]|[\d]", "", text)


async def parse_book_words(url: str) -> list:
    html = await fetch(url)
    soup = bs4.BeautifulSoup(html, "html.parser")
    text = remove_punctuation_and_digits(soup.find(class_="prose", id="content").text.strip()).lower()
    return text.split()


def save_word_counts_to_csv(courses: list, filename: str) -> None:
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Word", "Count"])
        writer.writerows((course.word, course.count) for course in courses)


async def main():
    tasks = [parse_book_words(url) for url in URLS]
    all_words = await asyncio.gather(*tasks)

    word_counts = Counter(word for words in all_words for word in words)
    courses = [Course(word, count) for word, count in word_counts.items()]
    sorted_courses = sorted(courses, key=lambda x: x.count, reverse=True)

    save_word_counts_to_csv(sorted_courses, "word_counts.csv")

if __name__ == "__main__":
    asyncio.run(main())
