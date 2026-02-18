# Smart Home Automation: Riadenie rekuperácie (Python)

Tento projekt demonštruje prepis domácej automatizácie z YAML do jazyka **Python**. Cieľom bolo sprehľadniť logiku rozhodovania pri vetraní na základe kvality vzduchu a vonkajších podmienok.

## Čo tento program rieši?
Program automaticky vypína rekuperačnú jednotku v momente, keď je v dome čerstvý vzduch s cieľom znížiť spotrebu rekuperície a žnížiť opotrebenie filtrov. 

### Hlavné funkcie:
- **Sledovanie CO2:** Reaguje na pokles pod 550 ppm pomocou `state_trigger`.
- **Inteligentné podmienky:** Kontroluje, či je vonku aspoň 13°C.
- **Filter počasia:** Obsahuje zoznam nepriaznivých stavov (dážď, sneženie), pri ktorých sa rekuperácia nevypne.
- **Hysterézia:** Časový zámok (15 minút) zabraňuje neustálemu zapínaniu a vypínaniu pri hraničných hodnotách.
