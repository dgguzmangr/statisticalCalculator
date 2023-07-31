# get Excel file and column
import pandas as pd


def get_columns_value(excel_path_file, column_name):
    try:
        df = pd.read_excel(excel_path_file)
        if column_name not in df.columns:
            print(f"La columna '{column_name}' no existe en el archivo.")
            return None
        column_values = df[column_name].tolist()
        return column_values

    except FileNotFoundError:
        print("No se encontró el archivo especificado.")
        return None


# dictionary to calculate absolute frequency of each value in the list
def calculate_absolute_frequency(column_values):
    absolute_frequency = {}

    for value in column_values:
        if value in absolute_frequency:
            absolute_frequency[value] += 1
        else:
            absolute_frequency[value] = 1

    return absolute_frequency


# dictionary to calculate absolute cumulative frequency of each value in the list
def calculate_absolute_cumulative_frequency(column_values):
    absolute_frequency = {}
    cumulative_frequency = 0

    for value in sorted(column_values):
        cumulative_frequency += 1
        absolute_frequency[value] = cumulative_frequency

    return absolute_frequency


# dictionary to calculate relative frequency of each value in the list
def calculate_relative_frequency(column_values):
    absolute_frequency = {}
    relative_frequency = {}

    for value in column_values:
        if value in absolute_frequency:
            absolute_frequency[value] += 1
        else:
            absolute_frequency[value] = 1

    total_elements = len(column_values)

    for value, freq in absolute_frequency.items():
        relative_frequency[value] = freq / total_elements

    return relative_frequency


# dictionary to calculate relative cumulative frequency of each value in the list
def calculate_relative_cumulative_frequency(column_values):
    relative_frequency = calculate_relative_frequency(column_values)
    relative_cumulative_frequency = {}
    cumulative_frequency = 0

    for value in sorted(column_values):
        cumulative_frequency += relative_frequency[value]
        relative_cumulative_frequency[value] = cumulative_frequency

    return relative_cumulative_frequency


# calculate the average in the list
def calculate_average(column_values):
    numeric_values = [value for value in column_values if isinstance(value, (int, float))]

    if len(numeric_values) == 0:
        print("No hay valores numéricos en la lista.")
        return None

    addition = sum(numeric_values)
    average = addition / len(numeric_values)

    return average


# calculate the median in the list
def calculate_median(column_values):
    sorted_data_set = sorted(column_values)
    n = len(sorted_data_set)

    if n % 2 == 1:
        median = sorted_data_set[n // 2]
    else:
        median = (sorted_data_set[(n // 2) - 1] + sorted_data_set[n // 2]) / 2.0

    return median


# calculate the mode in the list
def calculate_mode(column_values):
    frequency = {}

    for value in column_values:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1

    mode = []
    max_frequency = max(frequency.values())

    for value, freq in frequency.items():
        if freq == max_frequency:
            mode.append(value)

    return mode
