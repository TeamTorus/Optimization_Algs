import numpy as np
from preprocesser import read_points_file


def export_ctrl_points(ctrl_points, filename, polynomial_degree = 5):
    with open(filename, 'w') as file:
        file.write("START\n")

        # write to the file in the format: %9.8f\t%9.8f\t%9.8f\n
        file.write("{:9.8f}\t{:9.8f}\t{:9.8f}\n".format(ctrl_points[-2], ctrl_points[-1], 0))
        ctrl_points2 = ctrl_points[:-2]

        unique_points = 0

        try:
            while (unique_points < len(ctrl_points2)):
                for i in range(polynomial_degree):
                    file.write("{:9.8f}\t{:9.8f}\t{:9.8f}\n".format(ctrl_points2[unique_points], ctrl_points2[unique_points + 1], 0))
                    unique_points += 2
                file.write("END\n")
                file.write("START\n")
                file.write("{:9.8f}\t{:9.8f}\t{:9.8f}\n".format(ctrl_points2[unique_points - 2], ctrl_points2[unique_points - 1], 0))

        except IndexError:
            file.write("{:9.8f}\t{:9.8f}\t{:9.8f}\n".format(ctrl_points[-2], ctrl_points[-1], 0))
            file.write("END")


if __name__ == "__main__":
    output = read_points_file("points.txt")
    print(output)
    export_ctrl_points(output, "output.txt")
    print("Output written to output.txt")