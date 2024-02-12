# Author: Zhicheng Yang
# Date: 10/12/2023
# Description: generate input file
import random

def generate_input_file():
    # Prompt the user for input parameters
    region_width = int(input("Enter the width of the region: "))
    region_height = int(input("Enter the height of the region: "))
    total_population = int(input("Enter the total population: "))
    infectious_count = int(input("Enter the number of infectious people: "))
    vaccinated_count = int(input("Enter the number of vaccinated people: "))
    threshold = int(input("Enter the threshold for infection: "))
    infectious_period = int(input("Enter the infectious period: "))
    input_file_name = input("Enter the name of the input file: ")

    # Create the region data based on user input
    region_data = [['s'] * region_width for _ in range(region_height)]

    # Generate random locations for 'i' (infectious people)
    for _ in range(infectious_count):
        while True:
            row = random.randint(0, region_height - 1)
            col = random.randint(0, region_width - 1)
            if region_data[row][col] == 's':
                region_data[row][col] = 'i'
                break

    # Generate random locations for 'v' (vaccinated people)
    for _ in range(vaccinated_count):
        while True:
            row = random.randint(0, region_height - 1)
            col = random.randint(0, region_width - 1)
            if region_data[row][col] == 's':
                region_data[row][col] = 'v'
                break

    # Write the input file without region information
    with open(input_file_name, "w") as file:
        file.write(f"threshold:{threshold}\n")
        file.write(f"infectious_period:{infectious_period}\n")
        for row in region_data:
            file.write(",".join(row) + "\n")

    print(f"Input file '{input_file_name}' has been generated successfully.")

if __name__ == "__main__":
    generate_input_file()
