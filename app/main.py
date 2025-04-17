class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(person["name"], person["age"]) for person in people]

    index = 0

    for person in people:
        if person.get("wife"):
            people_list[index].wife = person["wife"]
        elif person.get("husband"):
            people_list[index].husband = person["husband"]

        index += 1

    for person in people_list:
        if hasattr(person, "wife"):
            if person.wife is not None:
                person.wife = Person.people[person.wife]
        if hasattr(person, "husband"):
            if person.husband is not None:
                person.husband = Person.people[person.husband]

    return people_list
