@state_trigger("binary_sensor.defrost_v_behu == 'on'", hold=90)
def zapocitanie_defrostu():
    
    # ZÍSKANIE HODNÔT PRE DODATOČNÚ KONTROLU
    delta_t = float(state.get("sensor.dt_tc") or 0)
    # Aktuálny odber kompresora
    spotreba = float(state.get("sensor.aktualna_spotreba_tc") or 0)

    # OVERENIE REÁLNOSTI DEFROSTU
    # Defrost uznáme, len ak mrzne výmenník (delta_t < 0) 
    # a kompresor má odber nad 100W (nie je v standby)
    if delta_t < 0 and spotreba > 100:
        counter.increment(entity_id="counter.pocet_defrostov")
        log.info(f"Defrost potvrdený: Delta T je {delta_t}°C a spotreba je {spotreba}W.")
    else:
        log.warning(f"Defrost ignorovaný: Podmienky nesplnené (Delta T: {delta_t}, Spotreba: {spotreba}W).")
