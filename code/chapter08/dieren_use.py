from dieren import Kat, Hond, Koe

sjors   = Kat('Sjors', 'bruin')         # Een bruine kat genaamd Sjors
sjimmie = Hond('Sjimmie', 'knalgroen')  # Een chemische hond genaamd Sjimmie
bertha7 = Koe('Bertha 7', 'Wit')        # Een witte koe genaamd Bertha 7

sjors.maak_geluid()
sjimmie.maak_geluid()
bertha7.maak_geluid()

sjors.spin()

sjimmie.apport()

bertha7.geef_melk()
bertha7.eet_gras()
bertha7.geef_melk()