# Author: Zhicheng Yang
# Date: 10/12/2023
# Description: main function
import SimLibrary


def main():
    file_name = input("Please enter the name of the region file: ")
    try:
        (
            threshold,
            infectious_period,
            region_data,
        ) = SimLibrary.read_configuration_file_data(file_name)
    except FileNotFoundError:
        while True:
            file_name = input(
                f"{file_name} does not exist! Please enter the name of the file: "
            )
            try:
                (
                    threshold,
                    infectious_period,
                    region_data,
                ) = SimLibrary.read_configuration_file_data(file_name)
            except FileNotFoundError:
                continue
            else:
                break
    list_s, list_i, list_r, day = SimLibrary.simulate_outbreak(
        region_data, threshold, infectious_period
    )
    SimLibrary.painter(list_i, list_s, list_r, day)


if __name__ == "__main__":
    main()

