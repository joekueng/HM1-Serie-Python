import numpy as np
import timeit

def fact_rec(n):
    if n < 0 or np.trunc(n) != n:
        raise Exception('only positive integers')
    if n <= 1:
        return 1
    return int(n) * fact_rec(int(n) - 1)

def fact_for(n):
    if n < 0 or np.trunc(n) != n:
        raise Exception('only positive integers')
    n = int(n)
    res = 1
    for k in range(2, n + 1):
        res *= k
    return res

def _time_functions(n=500, repeats=5, number=100):
    t1 = timeit.repeat("fact_rec(n)", setup="from __main__ import fact_rec, n", number=number, repeat=repeats)
    t2 = timeit.repeat("fact_for(n)", setup="from __main__ import fact_for, n", number=number, repeat=repeats)
    return float(np.mean(t1)), float(np.mean(t2))

def _print_integer_tests():
    print("\nInteger-Tests: n! für n ∈ [190..200] (Ziffernanzahl)")
    for n in range(190, 201):
        val = fact_for(n)
        print(f"{n}! hat {len(str(val))} Ziffern")

def _print_float_tests():
    print("\nFloat-Tests: 170! und 171! als float")
    for n in [170, 171]:
        val = fact_for(n)
        try:
            fval = float(val)
            print(f"{n}! als float: {fval}")
        except OverflowError as e:
            print(f"{n}! als float: OverflowError ({e})")

if __name__ == "__main__":
    print("Korrektheitstest:")
    for n in [0, 1, 5, 10]:
        r = fact_rec(n)
        f = fact_for(n)
        print(f"{n}! -> rec: {r}, for: {f}, equal: {r == f}")

    n = 500
    repeats = 5
    number = 100
    avg_rec, avg_for = _time_functions(n=n, repeats=repeats, number=number)

    print("\nTiming:")
    print(f"n={n}, repeats={repeats}, number={number}")
    print(f"Rekursiv: {avg_rec:.6f} s")
    print(f"Iterativ: {avg_for:.6f} s")
    if avg_for > 0:
        ratio = avg_rec / avg_for
        if ratio >= 1:
            print(f"Iterativ ist ~{ratio:.2f}x schneller")
        else:
            print(f"Rekursiv ist ~{1/ratio:.2f}x schneller")

    _print_integer_tests()
    _print_float_tests()

    # --- Antworten (Aufgabe 3) ---
    # 1) Welche Funktion ist schneller?
    #    In der Praxis die iterative Version (geringerer Funktionsaufruf-Overhead).
    #    Faktor (bitte hier Ihren gemessenen Wert ausgeben und eintragen):
    #    z.B. iterativ ≈ 3.2x schneller als rekursiv bei n=500 (100 Läufe, 5 Wiederholungen).

    # 2) Grenze als Integer:
    #    Python-Integer haben beliebige Präzision -> keine feste Obergrenze für n! (nur Zeit/Speicher).

    # 3) Grenze als Float (double, float64):
    #    170! ist noch als float darstellbar; 171! führt zu Overflow (inf/OverflowError bei Umwandlung).

