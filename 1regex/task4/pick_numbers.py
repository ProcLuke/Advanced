import re

def pick_numbers(text: str) -> list[str]:
    numbs = re.findall(r"\d+", text.replace(" ", "").replace("\t", ""))
    return [int(num) for num in numbs]
