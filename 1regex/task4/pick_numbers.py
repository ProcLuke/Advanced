import re

def pick_numbers(text: str) -> list[str]:
    numbs = re.split(r"\d+\ *[,:;]\ *", text, flags=re.MULTILINE)
    return numbs        #[int(num) for num in numbs]
