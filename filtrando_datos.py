from database import DATA

def run():
    all_platzi_workers = list(filter(lambda worker: worker["organization"] == "Platzi", DATA))
    all_platzi_workers = list(map(lambda worker: worker["name"], all_platzi_workers))
    all_python_devs = list(filter(lambda worker: worker["language"] == "python", DATA))
    all_python_devs = list(map(lambda worker: worker["name"], all_python_devs))
    adults = [worker["name"] for worker in DATA if worker["age"] > 18]
    old_people = [worker["name"] for worker in DATA if worker["age"] > 70]

    print("->Programadores en python:")
    for worker in all_python_devs:
        print(worker)
    
    print("\n")

    print("->Trabajadores de Platzi:")
    for worker in all_platzi_workers:
        print(worker)

    print("\n")

    print("->Adultos:")
    for worker in adults:
        print(worker)
    
    print("\n")

    print("->Adultos mayores:")
    for worker in old_people:
        print(worker)
    
if __name__ == '__main__':
    run()