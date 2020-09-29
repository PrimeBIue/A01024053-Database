import csv

population_2010 = []
value_errors = ['--', 'NA']
country_exceptions = ['World', 'Country', 'Asia & Oceania', 'Africa', 'Europe', 'Central & South America', 'North America', 'Eurasia', 'Middle East']

with open("TextFiles/populationbycountry19802010millions.csv") as csvFile_1:
    reader_1 = csv.reader(csvFile_1)

    for row in reader_1:
         if row[-1] not in value_errors and row[0] not in country_exceptions:
              population_2010.append([float(row[-1]), row[0]])

population_2010.sort(reverse=True)
print(population_2010[:5])
    
greenhouse_gases_2010 = []


with open("TextFiles/greenhouse_gas_inventory_data_data.csv") as csvFile_2:
    reader_2 = csv.reader(csvFile_2)
    for row in reader_2:
         if row[1] == "2010" and row[3] == "greenhouse_gas_ghgs_emissions_including_indirect_co2_without_lulucf_in_kilotonne_co2_equivalent" and row[0] != 'European Union':
              greenhouse_gases_2010.append([float(row[2]), row[0]])

greenhouse_gases_2010.sort(reverse=True)
print(greenhouse_gases_2010[:5])

#Si parece que tiene relación proporcional la población de un lugar y su emisión de gases invernadero pero hacen falta datos en el segundo archivo para comprobarlo.