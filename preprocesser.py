import numpy as np

# open txt file and read the content
def read_points_file(file_path):

    arr = []
    arr2 = []
    params = []
    consider_next = True

    with open(file_path, 'r') as file:
        for idx, line in enumerate(file):
            if line == "START\n":
                consider_next = False
                continue
            if line == "END\n" or line == "END":
                consider_next = True
                continue
            if consider_next:
                arr.append(line.split(' '))
                # print(line)
            else:
                print("Not considering line: ", line)
                consider_next = True

    # remove empty strings
    for elem in arr:
        for small_elem in elem:
            if small_elem == '':
                elem.remove(small_elem)
            # remove '\n' from the end of the string if it exists
        
        elem[-1] = elem[-1].replace('\n', '')

    for elem in arr:
        arr2.append([float(i) for i in elem])

    params = np.array([elem[:-1] for elem in arr2])
    flat_params = []
    for elem in params:
        for small_elem in elem:
            flat_params.append(small_elem)
    return flat_params


if __name__ == "__main__":
    output = read_points_file("points.txt")
    print(output)