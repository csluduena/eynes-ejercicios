import random


def simple_list():
    """
    Genera una lista de 10 diccionarios con id único y age aleatorio.

    Returns:
        Lista de 10 diccionarios con claves 'id' y 'age'
    """
    persons = []
    for i in range(10):
        person = {
            "id": i + 1,  # ID único empezando desde 1
            "age": random.randint(1, 100)  # Edad aleatoria entre 1 y 100
        }
        persons.append(person)

    return persons


def sort_list():
    pass
