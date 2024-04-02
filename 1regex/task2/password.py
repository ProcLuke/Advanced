import re

# Přijímá hesla o délce 8-16 znaků, obsahující alespoň jedno velké písmeno, jedno číslo a jeden speciální znak.
def validate_password(password):
    return bool(re.match(r'^(?=.*[A-Z])(?=.*\d)(?=.*\W).{8,16}$', password))