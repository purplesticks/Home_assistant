# VSTUPNÉ ÚDAJE
H_konstanta = 80              # Tepelná strata tvojho domu (W/K)
t_vonku = -5.0                # Vonkajšia teplota (°C)

# Tvoje 3 vnútorné senzory
t_izba_1 = 22.5               
t_izba_2 = 21.8
t_izba_3 = 22.1

# VÝPOČET (Logika z Home Assistanta)

# Priemer vnútornej teploty
t_in_avg = (t_izba_1 + t_izba_2 + t_izba_3) / 3

# Výpočet straty: H * (T_in - T_out)
tepelna_strata_w = H_konstanta * (t_in_avg - t_vonku)

# Finálna úprava (zaokrúhlenie a ochrana proti záporným hodnotám)
vysledok_w = round(max(0, tepelna_strata_w), 1)

# VÝSTUP
print(f"Priemerná teplota vnútri: {round(t_in_avg, 2)} °C")
print(f"Vonkajšia teplota:        {t_vonku} °C")
print("-" * 35)
print(f"AKTUÁLNA STRATA DOMU:     {vysledok_w} W")
