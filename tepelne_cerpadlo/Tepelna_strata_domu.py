"""
Tento skript počíta okamžitú tepelnú stratu domu (W) 
na základe prestupu tepla a rozdielu teplôt (In/Out).
Vzorec: P = H * (T_interior - T_exterior)
"""

@state_trigger("sensor.teplota_izba", "sensor.vonkajsia_teplota")
def vypocitaj_tepelnu_stratu():
    # KONŠTANTA (Tepelná strata objektu W/K)
    # H hodnota vyjadruje, koľko Wattov unikne z domu pri rozdiele 1°C
    H = float(state.get("input_number.h_w_per_k") or 80)

    # PRIEMERNÁ VNÚTORNÁ TEPLOTA
    # Spájame dáta z troch rôznych senzorov pre presnejší priemer
    t_in_1 = float(state.get("sensor.teplota_izba") or 22)
    t_in_2 = float(state.get("sensor.qingping_air_monitor_2_temperature") or 22)
    t_in_3 = float(state.get("sensor.qingping_air_monitor_temperature") or 22)
    
    t_in_avg = (t_in_1 + t_in_2 + t_in_3) / 3

    # VONKAJŠIA TEPLOTA
    t_out = float(state.get("sensor.vonkajsia_teplota") or 0)

    # VÝPOČET STRATY
    strata_w = H * (t_in_avg - t_out)
    
    # Zaokrúhlenie na 1 desatinné miesto
    strata_final = round(max(0, strata_w), 1)

    # ZÁPIS DO SENZORA
    state.set("sensor.aktualna_tepelna_strata", strata_final, {
        "unit_of_measurement": "W",
        "friendly_name": "Okamžitá tepelná strata domu",
        "icon": "mdi:home-thermometer"
    })
