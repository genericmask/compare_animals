
def main():
    cats_path = "C:/Users/Casey/Downloads/sorted_cats.txt"
    dogs_path = "C:/Users/Casey/Downloads/sorted_dogs.txt"
    cats_ans_path = "C:/Users/Casey/Downloads/cats_ans.txt"
    dogs_ans_path = "C:/Users/Casey/Downloads/dogs_ans.txt"
    
    cats = get_list(cats_path)
    dogs = get_list(dogs_path)
    cats_ans = get_list_no_ws(cats_ans_path)
    dogs_ans = get_list_no_ws(dogs_ans_path)

    if(cats is not None and cats_ans is not None):
        compare(cats_path, cats, cats_ans)
    if(dogs is not None and dogs_ans is not None):
        compare(dogs_path, dogs, dogs_ans)

# accepts a file path and returns a list of the lines in the file.
def get_list(path):
    lines = []
    try:
        with open(path) as file:
            for line in file:
                lines.append(line)
        file.close()
    except:
        print(f"{path} not found.")
        return None
    return lines

# accepts a file path and returns a list of the lines in the file with no whitespace
def get_list_no_ws(path):
    lines = []
    try:
        with open(path) as file:
            for line in file:
                lines.append("".join(line.split()))
        file.close()
    except:
        print(f"{path} not found.")
        return None
    return lines

# accepts the name of what is being tested, a list of things to test, and a list of answers with no white space.
def compare(name, listOfElems, ans):
    print(f"\n{name}")
    dictOfElems = dict()
    not_in = 0
    order = 0
    duplicates = 0
    age_temp = 0
    for elem in listOfElems:
        error = ""
        try:
            name, gender, age, weight = elem.split()
            if "".join(elem.split()) not in ans:
                error = " -- Doesn't match answer key"
                not_in += 1
            if int(age) < int(age_temp):
                error += " -- Out of order"
                order += 1
            else:
                age_temp = age
            if elem in dictOfElems:
                dictOfElems[elem] += 1
                error += " -- Duplicate"
                duplicates += 1
            else:
                dictOfElems[elem] = 1  
            print ("{:<12} {:<7} {:<2} {:<7}".format(name, gender, age, weight), error)
        except ValueError as try_error:
            print(elem, "--", try_error)
            not_in += 1
    print(f"{not_in+order+duplicates} error(s)")
    print(f"Doesn't match answer key: {not_in}")
    print(f"Out of order: {order}")
    print(f"Duplicates: {duplicates}")

main()