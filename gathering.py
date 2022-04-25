import random

def create_name_list():
    names = []
    f = open("./names.txt", "r")
    content = f.read().split("\n")
    return content
    
def get_random_number_list():
    random_number_list = random.sample(range(20), 20)
    print_all(random_number_list)
    return random_number_list

def print_all(random_list):
    # this function is for debugging
    for element in random_list:
        print(element)

def main():
    names = create_name_list()
    random_indexes = get_random_number_list()
    groups = []
    group = []
    
    for index in range(len(random_indexes)):
        random_index = random_indexes[index]
        random_name = names[random_index]
        group.append(random_name)

        if index % 5 == 4:
            groups.append(group)
            group = []
            
    print_all(groups)

if __name__ == "__main__":
    main()