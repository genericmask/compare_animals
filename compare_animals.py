

def main():
    test_path = "file_name.txt"
    ans_path = "file_name.txt"

    test = get_list(test_path)
    ans = get_list(ans_path)
    
    # Add if statements using this as a template for each comparison you want to make
    if(test is not None and ans is not None):
        print(f"\n{test_path}")
        compare(test, ans)

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

def remove_ws(listOfElems):
    lines = []
    for elem in listOfElems:
        lines.append("".join(elem.split()))
    return lines

# accepts a list of things to test and a list of answers.
def compare(listOfElems, ans_key):
    ans_ref = remove_ws(ans_key) # Get a list with no ws in each element to make comparison easier
    dictOfDupes = dict()
    not_in = 0
    order = 0
    duplicates = 0
    age_temp = 0
    for elem in listOfElems:
        error = ""
        try:
            name, gender, age, weight = elem.split()
            if "".join(elem.split()) not in ans_ref:
                error = " -- Doesn't match answer key" 
                not_in += 1
            if int(age) < int(age_temp):
                error += " -- Out of order"
                order += 1
            else:
                age_temp = age
            if elem in dictOfDupes:
                dictOfDupes[elem] += 1
                error += " -- Duplicate"
                duplicates += 1
            else:
                dictOfDupes[elem] = 1  
            print ("{:<12} {:<7} {:<2} {:<5}".format(name, gender, age, weight), error)
        except ValueError as try_error:
            print(elem, "--", try_error)
            not_in += 1
    print(f"{not_in+order+duplicates} error(s)")
    print(f"Doesn't match answer key: {not_in}")
    print(f"Out of order: {order}")
    print(f"Duplicates: {duplicates}")

main()
