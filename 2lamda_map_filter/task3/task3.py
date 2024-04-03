def add_initials(people):
    def add_initials(p):
        p["initials"] = p["name"][0] + p["surname"][0]
        return p
    return list(map(add_initials, people))