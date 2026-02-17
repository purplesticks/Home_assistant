"""
Tento skript počíta aktuálnu účinnosť tepelného čerpadla (COP).
Využíva fyzikálny vzorec pre tepelný výkon: Q = m * c * ΔT
"""

@state_trigger("sensor.teplota_vystupu", "sensor.teplota_vstupu", "sensor.aktualna_spotreba_tc")
def aktualizuj_cop():
    # KONŠTANTY A VSTUPY
    RHO = 1000  # Hustota vody (kg/m3)
    CP = 4186   # Špecifická tepelná kapacita vody (J/kg.K)
    
    prietok_m3h = float(state.get("input_number.prietok_vody_tc") or 0)
    t_vystup = float(state.get("sensor.teplota_vystupu") or 0)
    t_vstup = float(state.get("sensor.teplota_vstupu") or 0)
    prikon_w = float(state.get("sensor.aktualna_spotreba_tc") or 0)
    
    # 2. VÝPOČET TEPELNÉHO VÝKONU (W)
    prietok_m3s = prietok_m3h / 3600
    delta_t = t_vystup - t_vstup
    tepelny_vykon_w = RHO * CP * prietok_m3s * delta_t
    
    # LOGIKA VÝPOČTU COP
    # Výpočet robíme len ak kompresor reálne beží (príkon > 200W), 
    # aby sme sa vyhli nezmyselným číslam pri vypnutom stroji.
    if prikon_w > 200:
        vypocitane_cop = tepelny_vykon_w / prikon_w
        
        # Ošetrenie reálneho rozsahu (COP býva v praxi 0 až 8)
        # Pomocou funkcie min/max zabezpečíme "clamping" (orezanú hranicu)
        finalne_cop = max(0, min(vypocitane_cop, 8))
        finalne_cop = round(finalne_cop, 2)
    else:
        finalne_cop = 0.0

    # ZÁPIS VÝSLEDKU
    # Zapíšeme výsledok do virtuálneho senzora v Home Assistante
    state.set("sensor.aktualne_cop_tc", finalne_cop, {
        "unit_of_measurement": "COP",
        "friendly_name": "Aktuálne COP TČ",
        "icon": "mdi:gauge"
    })
