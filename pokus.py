import re

m = re.search(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", "moje ip je 172.99.2.30 daish", flags=re.IGNORECASE | re.MULTILINE)

e = re.compile(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", flags=re.IGNORECASE | re.MULTILINE)
m = e.search("moje ip je 172.99.2.30 daish")


print(m)

if m:
    print(m.groups())
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
    print(m.group(3))

seznam = re.split(r"\s", "ahoj,             nazdar,    , sad \n bobob")
print(seznam)