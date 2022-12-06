"""
V data/meteo_stanice.txt zisti:
pocet merani
A vypise:
namerane teploty
najvyssiu nameranu teplotu
kod stanice s najvyssou nameranou teplotou
priemernu teplotu vsetkych stanic"""

measurement_count = 0
temperatures = ""
max_temperature = -273.16  # the lowest possible temperature
max_temp_code = "Physics"
temperature_total = 0

fr = open("data/meteo_stanice.txt", encoding="utf-8").readlines()
for line in fr:
    measurement_count += 1
    temperatures += f"{line[21:26]}°C, "
    if float(line[22:26]) * (1 - 2 * (line[21] == "-")) > max_temperature:
        max_temperature = float(line[21:26])
        max_temp_code = line[:4]
    temperature_total += float(line[22:26]) * (1 - 2 * (line[21] == "-"))
average_temperature = "{:.2f}".format(temperature_total / measurement_count)

print(f"Namerané teploty sú:\n{temperatures[:-2]}\n"
      f"-------------------------------------------------"
      f"\nNajvyššia nameraná teplota bola {max_temperature}°C"
      f"\nKod stanice s najvyššou nameranou teplotou je {max_temp_code}"
      f"\nPriemerná nameraná teplota bola {average_temperature}")
