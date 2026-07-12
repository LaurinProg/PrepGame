# Krisensimulation – Digital Game Based Learning

## Projektbeschreibung

**Krisensimulation** ist ein textbasiertes Serious Game, das Spielerinnen und Spieler durch eine realitätsnahe Krisensituation führt. Ziel des Projekts ist es, Wissen über persönliche Krisenvorsorge spielerisch zu vermitteln und durch eigene Entscheidungen die Auswirkungen von Vorbereitung, Ressourcenmanagement und psychischer Belastung erfahrbar zu machen.

Das Projekt basiert auf dem Ansatz des **Digital Game Based Learning (DGBL)**. Lernen erfolgt dabei nicht ausschließlich durch Informationsvermittlung, sondern durch aktives Entscheiden, Erleben von Konsequenzen und anschließende Reflexion.

---

## Lernziel

Das Spiel verfolgt folgende Lernziele:

* Bewusstsein für persönliche Krisenvorsorge schaffen
* Bedeutung von Wasser, Nahrung und Informationsquellen verdeutlichen
* Auswirkungen von Unsicherheit und Stress in Krisensituationen erfahrbar machen
* Entscheidungsprozesse unter begrenzten Ressourcen trainieren
* Reflexion über eigenes Verhalten und Vorbereitung fördern

Die Ergebnisse des Spiels werden am Ende analysiert und mit Empfehlungen zur Krisenvorsorge, beispielsweise des Bundesamtes für Bevölkerungsschutz und Katastrophenhilfe (BBK), verglichen.

---

## Spielprinzip

Die Spielerinnen und Spieler übernehmen die Verantwortung für eine Krisensituation über mehrere Tage.

Zu Beginn erfolgt eine Vorbereitungsphase:

* Auswahl von Ausrüstung und Vorräten
* Abwägung zwischen verschiedenen Bedürfnissen
* Planung mit begrenztem Inventarplatz

Während der Simulation müssen Entscheidungen getroffen werden:

* Ressourcen verwalten
* Informationen bewerten
* Ereignisse bewältigen
* Stress reduzieren
* langfristige Stabilität erhalten

Jede Entscheidung beeinflusst den weiteren Verlauf der Krise.

---

## Spielsysteme

### Ressourcenmanagement

Das Spiel simuliert zentrale Bereiche der Krisenvorsorge:

* Wasser
* Nahrung
* Batterien
* Informationsquellen
* persönliche Gegenstände

Die begrenzte Kapazität des Inventars zwingt zu strategischen Entscheidungen.

---

### Stress- und Informationssystem

Neben physischen Ressourcen berücksichtigt die Simulation auch psychologische Faktoren.

**Stress steigt beispielsweise durch:**

* fehlende Versorgung
* Unsicherheit
* Isolation
* schwierige Ereignisse

**Information reduziert Unsicherheit und unterstützt Entscheidungen.**

Dadurch wird verdeutlicht, dass Krisenvorsorge nicht nur aus materieller Vorbereitung besteht.

---

### Ereignissystem

Die Simulation verwendet dynamische Krisenereignisse:

Beispiele:

* Stromausfall
* Informationsmangel
* Dunkelheit
* Isolation
* Gerüchte
* fehlende Routine

Die Ereignisse unterscheiden sich abhängig vom gewählten Szenario und dem Verlauf der Krise.

---

### Reflexion und Analyse

Nach Abschluss der Simulation erfolgt eine Auswertung:

* Welche Entscheidungen wurden getroffen?
* Wie entwickelte sich die Situation?
* Welche Ressourcen waren besonders wichtig?
* Welche Vorsorgemaßnahmen haben geholfen?

Die Analyse verbindet Spielerfahrung mit realen Handlungsempfehlungen.

---

## Technische Umsetzung

### Technologien

* Python
* JSON-basierte Datenverwaltung
* Terminal User Interface
* modulare Systemarchitektur

---

## Architektur

Das Projekt ist modular aufgebaut:

```
project/
│
├── systems/
│   ├── action_system.py
│   ├── analysis_system.py
│   ├── atmosphere_system.py
│   ├── crisis_system.py
│   ├── effect_system.py
│   ├── event_system.py
│   ├── information_system.py
│   ├── inventory_system.py
│   ├── item_effect_system.py
│   ├── log_system.py
│   ├── preparation_system.py
│   ├── recommendation_system.py
│   ├── resource_system.py
│   ├── stress_system.py
│   ├── scenario_system.py
│   └── stress_tracking.py
│
├── data/
│   ├── events.json
│   ├── items.json
│   ├── recommendations.json
│   └── scenarios.json
│
├── ui.py
├── config.py
├── items.py
├── simulation.py
├── state.py
└── main.py
```

Die Trennung von Spielsystemen, Daten und Darstellung ermöglicht eine einfache Erweiterung weiterer Szenarien und Ereignisse.

---

## Installation

Repository klonen:

```bash
git clone https://github.com/LaurinProg/PrepGame
```

In das Projektverzeichnis wechseln:

```bash
cd <PROJECT_FOLDER>
```

Benötigte Pakete installieren:

```bash
pip install -r requirements.txt
```

Simulation starten:

```bash
python main.py
```

---

## Projektkontext

Das Projekt entstand im Rahmen des Studiums und untersucht, wie spielerische Simulationen zur Vermittlung von Wissen über Krisenvorsorge eingesetzt werden können.

Die Kombination aus Simulation, Entscheidungsfreiheit und Reflexion soll einen nachhaltigen Lernprozess ermöglichen.

---

## Ausblick

Geplante bzw. mögliche Erweiterungen:

* zusätzliche Krisenszenarien
* weitere Gegenstände
* weitere Ereignisse
* verbesserte grafische Oberfläche
* Mehrspieler- oder Gruppenmodus
* detailliertere Auswertung
* Erweiterung der Lerninhalte

