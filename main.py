from utils import get_data, get_filtered_data, get_last_values, get_formated_data


def main():
    COUNT_VALUES = 5
    FILTERED_EMPTY_FROM = True

    data = get_data()
    data = get_filtered_data(data, FILTERED_EMPTY_FROM)
    data = get_last_values(data, COUNT_VALUES)
    data = get_formated_data(data)

    for row in data:
        print(row, end='\n')


if __name__ == "__main__":
    main()
