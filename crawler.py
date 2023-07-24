import requests
from bs4 import BeautifulSoup

def find_nth_char(string : str, char : str, n : int) -> int:
    for i, c in enumerate(string):
        if char == c:
            n -= 1
            if n == 0:
                return i
    return i

def extract_domain_protocol(webpage : str) -> str:
    # Up to end of domain or end of string
    i = find_nth_char(webpage, "/", 3)
    if webpage[i] == "/":
        return webpage[:i]
    return webpage

def is_relative(link : str) -> bool:
    return link.startswith("http")

def relative_to_abs(webpage : str, link : str) -> str:
    if not is_relative(link):
        return extract_domain_protocol(webpage) + link
    return link

def find_links(webpage : str) -> map:
    reqs = requests.get(webpage)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    return map(lambda x : relative_to_abs(webpage, x.get("href").lstrip()), soup.find_all('a'))

print(list(find_links("https://www.reuters.com/business/finance/")))
print(extract_domain_protocol("https://www.reuters.com/business/finance/"))