# 1. NASTAVENIE SPÚŠŤAČA (Trigger)
# Ak CO2 klesne pod 550 a drží sa tam 15 minút (900 sekúnd)
@state_trigger("sensor.qingping_air_monitor_2_co2 < 550", hold=900)
def vypnutie_rekuperacie():
    
    # 2. ZÍSKANIE HODNÔT (Stavy senzorov)
    teplota_vonku = float(state.get("sensor.vonkajsia_teplota"))
    pocasie = state.get("weather.forecast_home")

    # 3. PODMIENKY (Conditions)
    
    # Podmienka 1: Teplota vonku musí byť nad 13 stupňov
    teplota_ok = teplota_vonku > 13
    
    # Podmienka 2: Kontrola, či neprší alebo nesneží (zoznam zlého počasia)
    zle_pocasie = ["rainy", "pouring", "snowy-rainy", "lightning-rainy", "hail"]
    pocasie_ok = pocasie not in zle_pocasie

    # 4. VYHODNOTENIE A AKCIA
    if teplota_ok and pocasie_ok:
        select.select_option(entity_id="select.rekuperacia_rezim", option="off")
        
        # Zápis do logu, aby sme spätne vedeli, že sa to vyplo
        log.info("Automatizácia: Rekuperácia bola vypnutá (CO2 je nízke a počasie je vhodné).")
    else:
        # Ak podmienky neboli splnené, neurobíme nič, len si to môžeme zapísať
        log.info("Automatizácia: CO2 je nízke, ale vonku nie je vhodné počasie na vypnutie.")
