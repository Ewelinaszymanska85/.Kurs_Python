while True:
    log_file = None
    try:
        log_file = open("log.txt", "a", encoding="utf-8")

        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        operacja = input("Podaj operację (+, -, *, /): ")

        if operacja == "+":
            wynik = a + b
        elif operacja == "-":
            wynik = a - b
        elif operacja == "*":
            wynik = a * b
        elif operacja == "/":
            if b == 0:
                raise ZeroDivisionError("Nie można dzielić przez zero!")
            wynik = a / b
        else:
            raise ValueError("Nieznana operacja!")

    except Exception as e:
        print("Wystąpił błąd:", e)
        if log_file:
            log_file.write(f"Błąd: {type(e).__name__} - {e}\n")
    else:
        print("Wynik:", wynik)
    finally:
        if log_file:
            log_file.close()
        print("Kolejna operacja...\n") 
        