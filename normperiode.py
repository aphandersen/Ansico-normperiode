print("ANSICO NORMPERIODE 0.1\n")

normperiode_standard = int(input("Antal uger i normperioden?\n"))
feriedage = int(input("Antal feriedage i perioden?\n"))

normperiode = normperiode_standard - feriedage / 5
antal_AN = normperiode * 7 // 6
antal_weekend = normperiode // 2
antal_fridage = normperiode * 2
antal_timer = normperiode * 37

print("\nFaktisk normperiode:",normperiode)
print("Antal nattevagter:",str(antal_AN))
print("Antal weekender:",str(antal_weekend))
print("Antal fridøgn:",str(antal_fridage))
print("Antal normtimer:",str(antal_timer))

print("\n(Der tages forbehold for beregningsfejl og usikkerhed ved manglende faktorer)")