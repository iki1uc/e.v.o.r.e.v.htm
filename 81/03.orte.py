# Orte — Python — Universal Ort, immer Home Arbeit
# Ort = Orte. Bewegung = Bewegungen.

ORTE = [
    (1, "Bett", "Schlafen"),
    (2, "Tisch", "Schreiben"),
    (3, "Tür", "Einsteigen"),
    (4, "Fenster", "Gucken"),
    (5, "Küche", "Futtern"),
    (6, "Bad", "Mist raus"),
    (7, "Straße", "Gehen"),
    (8, "Uni", "Lernen"),
    (9, "Denkraum", "Spirit holen"),
]

def orten(id):
    # Orten = Finden + Setzen + Quadranisieren
    for oid, name, nutzung in ORTE:
        if oid == id:
            # Universal Ort: Immer Home Arbeit
            return f"Ort {oid}: {name} — Nutzung: {nutzung} — Universal Ort: Immer Home Arbeit — Rückflug Garantie"
    return "Kein Ort"

def quadranisieren():
    # 4 Quadranten + 1 Mitte
    return {
        "Q1": "Oben Links — Alt",
        "Q2": "Oben Rechts — Neu",
        "Q3": "Unten Links — Stand — 9 unten",
        "Q4": "Unten Rechts — Stage — 3 oben",
        "Mitte": "41 — Universal Ort — Ort = Orte",
    }

print(orten(9))
print(quadranisieren())
