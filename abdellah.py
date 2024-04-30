class UnitConverter:
    def __init__(self):
        self.conversion_factors = {
            "celsius_to_fahrenheit": lambda c: c * 9/5 + 32,
            "fahrenheit_to_celsius": lambda f: (f - 32) * 5/9,
            "kilometers_to_miles": lambda km: km * 0.621371,
            "miles_to_kilometers": lambda mi: mi / 0.621371,
            "kilograms_to_pounds": lambda kg: kg * 2.20462,
            "pounds_to_kilograms": lambda lb: lb / 2.20462
        }
    
    def convert(self, value, from_unit, to_unit):
        conversion_key = f"{from_unit}_to_{to_unit}"
        if conversion_key in self.conversion_factors:
            conversion_func = self.conversion_factors[conversion_key]
            result = conversion_func(value)
            return result
        else:
            return None

def main():
    converter = UnitConverter()

    print("Bienvenue dans le convertisseur d'unités!")

    while True:
        print("\nChoisissez une option:")
        print("1. Convertir une température")
        print("2. Convertir une distance")
        print("3. Convertir une masse")
        print("4. Quitter")

        choice = input("Votre choix  ")

        if choice == "1":
            value = float(input("Entrez la valeur : "))
            from_unit = input("Entrez l'unité d'origine (celsius/fahrenheit) : ").lower()
            to_unit = input("Entrez l'unité de destination (celsius/fahrenheit) : ").lower()
        elif choice == "2":
            value = float(input("Entrez la valeur : "))
            from_unit = input("Entrez l'unité d'origine (kilometers/miles) : ").lower()
            to_unit = input("Entrez l'unité de destination (kilometers/miles) : ").lower()
        elif choice == "3":
            value = float(input("Entrez la valeur : "))
            from_unit = input("Entrez l'unité d'origine (kilograms/pounds) : ").lower()
            to_unit = input("Entrez l'unité de destination (kilograms/pounds) : ").lower()
        elif choice == "4":
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
            continue

        result = converter.convert(value, from_unit, to_unit)
        if result is not None:
            print(f"Résultat de la conversion : {result}")
        else:
            print("Conversion non prise en charge.")

if __name__ == "__main__":
    main()
