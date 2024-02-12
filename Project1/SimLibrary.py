# Author: Zhicheng Yang
# Date: 10/12/2023
# Description: SIR model

import copy
import matplotlib.pyplot as plt


# Function to read and store the configuration data
def read_configuration_file_data(file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()

            threshold = int(lines[0].split(":")[1])
            infectious_period = int(lines[1].split(":")[1])

            region_data = []
            for line in lines[2:]:
                row = line.strip().split(",")
                region_data.append(row)
            for row in region_data:
                for e in row:
                    if e not in "sriv":
                        raise ValueError(f"ERROR: {e} is not a valid state!")
            return threshold, infectious_period, region_data
    except FileNotFoundError as exc:
        raise exc
    except ValueError as e:
        print(f"ERROR: {e}")
        print()
        # print("Process finished with exit code -1")
        exit(-1)
    except Exception:
        print("ERROR: There's something wrong with the input file!")
        print()
        # print("Process finished with exit code -2")
        exit(-2)


def display(day, states):
    print(f"Day: {day} ")
    for row in states:
        for element in row:
            print(element[0], end=" ")
        print()
    print()


def simulate_outbreak(region_data, threshold, infectious_period):
    health_states = [[[element, 0] for element in row] for row in region_data]
    day = 0
    peak_day = 0
    peak_infectious_count = 0
    susceptible_number = []
    infectious_number = []
    recovered_number = []
    offset_list = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    while True:
        # calculate and store SIR people
        for row in health_states:
            for i in row:
                if i[0] == "i" and day - i[1] == infectious_period:
                    i[0] = "r"
        display(day, health_states)
        day += 1
        current_infectious = 0
        current_susceptible = 0
        current_recovered = 0
        for row in health_states:
            for i in row:
                if i[0] == "i":
                    current_infectious += 1
                if i[0] == "s":
                    current_susceptible += 1
                if i[0] == "r":
                    current_recovered += 1
        if current_infectious > peak_infectious_count:
            peak_infectious_count = current_infectious
            peak_day = day - 1
        susceptible_number.append(current_susceptible)
        infectious_number.append(current_infectious)
        recovered_number.append(current_recovered)
        if current_infectious == 0:
            break
        # recovered people
        current_states = copy.deepcopy(health_states)

        for i in range(len(health_states)):
            for j in range(len(health_states[0])):
                if health_states[i][j][0] == "s":
                    counter = 0
                    for tup in offset_list:
                        if 0 <= i + tup[0] < len(health_states) and 0 <= j + tup[
                            1
                        ] < len(health_states[0]):
                            if health_states[i + tup[0]][j + tup[1]][0] == "i":
                                counter += 1
                    if counter >= threshold:
                        current_states[i][j][0] = "i"
                        current_states[i][j][1] = day

        health_states = current_states
    print(f"Outbreak Duration: {day-1} days")
    print(f"Peak Day: Day {peak_day}")
    print(f"Peak Infectious Count: {peak_infectious_count} people")

    return (susceptible_number, infectious_number, recovered_number, day)


def painter(list_i, list_s, list_r, day):
    plt.title("SIR State Counts")
    x = list(range(day))
    plt.plot(x, list_s)
    plt.plot(x, list_i)
    plt.plot(x, list_r)
    plt.xlabel("Days")
    plt.ylabel("Counts")
    plt.legend(["S", "I", "R"])
    plt.show()
