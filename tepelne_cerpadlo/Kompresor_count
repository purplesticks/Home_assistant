"""
Tento skript monitoruje štarty kompresora tepelného čerpadla.
Využíva logiku z binary_sensora, ktorý je definovaný spotrebou nad 125W
a obsahuje 10-minútový delay_off na elimináciu krátkych prestávok - defrost.
"""

# Trigger
# Sledujeme zmenu stavu binárneho senzora z 'off' na 'on'
@state_trigger("binary_sensor.kompresor_tc == 'on'")
def zapocitaj_start_kompresora():
    
    # Zvýšenie počítadla (Counter)
    # Tento counter ukladá celkový počet štartov pre analýzu životnosti stroja
    counter.increment(entity_id="counter.pocet_zapnuti_kompresora")
    
    # ZÍSKANIE DOPLNKOVÝCH DÁT PRE LOG
    # Vytiahneme si aktuálnu spotrebu v momente zopnutia
    aktualna_spotreba = state.get("sensor.aktualna_spotreba_tc")
    
    # ZÁPIS DO SYSTÉMOVÉHO DENNÍKA (Logging)
    log.info(f"KOMPRESOR ŠTART: Detekovaný nábeh zariadenia. Aktuálny odber: {aktualna_spotreba}W. Počítadlo inkrementované.")
