# Green Mobility

## Hintergrund

Ein E-Bike-Verleih möchte seine Flotte digital verwalten. Es gibt verschiedene Fahrzeugtypen, die alle grundlegende Eigenschaften teilen, sich aber in der Berechnung ihrer Reichweite und ihres Status unterscheiden.

- - -

## Deine Aufgabe

Implementiere ein (objektorientiertes) Python-Programm, das die Konzepte von Vererbung, Abstraktion und Enums nutzt. Finde adäquate Datenstrukturen, Methoden, usw. in Python, um die Anforderungen zu erfüllen.

### 1. System-Struktur

*   **Enum `FahrzeugStatus`:** Definiere ein Enum mit den Zuständen: `VERFUEGBAR`, `IN_BENUTZUNG`, `WARTUNG`.
*   **Abstrakte Basisklasse `Fahrzeug`:**
    *   Attribute: `modell_name`, `batterie_stand` (0–100) und `basis_reichweite`.
    *   Eine abstrakte Methode `berechne_restreichweite()`, die die km-Anzahl zurückgibt.
*   **Subklasse `EBike`:**
    *   Implementiert `berechne_restreichweite()`: `batterie_stand * basis_reichweite / 100`.
*   **Subklasse `ELastenrad`:**
    *   Zusätzliches Attribut: `ladung_kg` (int).
    *   Implementiert `berechne_restreichweite()`: Wie beim E-Bike, aber pro 10kg Ladung werden 2km von der Gesamtreichweite abgezogen.

- - -

### 2. Methoden & Logik

*   **Konstruktor `__init__`:** Initialisiere die Attribute und setze den Status standardmäßig auf `VERFUEGBAR`.
*   **Methode `status_update()`:** Ändert den Status des Fahrzeugs basierend auf dem Batteriestand (z.B. wenn `batterie_stand < 10`, setze Status auf `WARTUNG`).

- - -

### 3. Das Hauptprogramm (Main)

*   Erstelle eine Liste mit mindestens einem `EBike` und einem `ELastenrad`.
*   Nutze eine _Schleife_, um die Reichweite aller Fahrzeuge in der Liste zu berechnen und auszugeben.
*   Polymorphie: Rufe für jedes Objekt in der Liste die Methode `status_update()` auf und gib den Namen des Fahrzeugs sowie den resultierenden `FahrzeugStatus` aus.

## Abgabe

Reiche alle Dateien als `Zip` ein. Viel Erfolg!