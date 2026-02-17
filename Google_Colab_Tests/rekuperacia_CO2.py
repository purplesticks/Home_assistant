co2_obyvacka = 400
co2_spalna = 800
niekto_je_doma = True

if co2_obyvacka > 600 and niekto_je_doma:
  print("Obývačka je vydýchaná. Zapínam rekuperáciu!")
else:
  print("Vzduch je v obývačke čistý. Šetrím elektrinu.")

if co2_spalna > 600 and niekto_je_doma:
  print("Spálňa je vydýchaná. Zapínam rekuperáciu!")
else:
  print("Vzduch je v spálni čistý. Šetrím elektrinu.")
