import matplotlib.pyplot as plt
from funtions import *

#
excel_file = "D:/" \
             "David/" \
             "001. Cursos/" \
             "013. SENA/" \
             "001. Análisis y desarrollo de software/" \
             "Fase 1 - Análisis/" \
             "Entregas/" \
             "GA2-240201528-AA3-EV01/" \
             "dataset_inmunizacion_2015_2023.xlsx"
column_name = "DEPARTAMENTO "

# column_values = get_columns_value(excel_file, column_name)


column_values = ["DAVID", "DAVID", "NATALIA", "KARINA"]

# graphic
relative_cumulative_frequency = calculate_relative_cumulative_frequency(column_values)
values = list(relative_cumulative_frequency.keys())
cumulative_frequencies = list(relative_cumulative_frequency.values())

plt.bar(values, cumulative_frequencies)
plt.xlabel('Valores')
plt.ylabel('Frecuencia Relativa Acumulada')
plt.title('Frecuencia Relativa Acumulada para la Lista')

plt.show()


# print results
# print("Conjunto de datos: ", column_values)
print("Frecuencia absoluta: ", calculate_absolute_frequency(column_values))
print("Frecuencia absoluta acumulada: ", calculate_absolute_cumulative_frequency(column_values))
print("Frecuencia relativa: ", calculate_relative_frequency(column_values))
print("Frecuencia relativa acumulada: ", calculate_relative_cumulative_frequency(column_values))
# print("Media: ", calculate_average(column_values))
# print("Mediana: ", calculate_median(column_values))
# print("Moda: ", calculate_mode(column_values))
