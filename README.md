# Tempasto · fatto a mano

**Der Teigplaner für neapolitanische Pizza.** Du sagst, wann gebacken wird, und Tempasto sagt dir, wann du was tun musst: vom Wasser-Kaltstellen bis zur letzten Pizza aus dem Ofen.

Kostenlos, ohne Werbung, ohne Konto. Deine Daten bleiben auf dem Handy.

<p>
  <img src="docs/start.png" width="180" alt="Startseite">
  <img src="docs/pizzen.png" width="180" alt="Pizzen auswählen">
  <img src="docs/einkauf.png" width="180" alt="Einkaufsliste">
  <img src="docs/programma.png" width="180" alt="Backplan">
  <img src="docs/backmodus.png" width="180" alt="Backmodus">
  <img src="docs/pause.png" width="180" alt="Pause im Backmodus">
</p>

---

## Warum es Tempasto gibt

Der Name verbindet *tempo* und *impasto*, die Zeit und den Teig. Mehr braucht guter Pizzateig nicht, aber die Zeit muss stimmen.

Guter Pizzateig braucht Zeit, meist 24 bis 72 Stunden. Die Frage ist nie *wie*, sondern *wann*: Wann muss der Teig angesetzt werden, damit am Donnerstag um 19 Uhr die erste Pizza aus dem Ofen kommt? Wann portionieren, wann aus dem Kühlschrank, wann den Ofen an?

Tempasto rechnet das rückwärts aus und begleitet dich dann Schritt für Schritt durch den ganzen Teig.

## Was die App kann

**Planen**
- Backtermin, Anzahl der Teiglinge (bis 20) und Gehzeit (24, 48 oder 72 h) wählen
- Die App rechnet rückwärts aus, wann du den Teig ansetzt, und passt die Hefemenge an Gehzeit und Kühlschranktemperatur an
- Vorlagen wie „Freitagspizza“ speichern und mit einem Tipp für den nächsten passenden Termin übernehmen
- Läuft etwas anders als geplant: „Später dran?“ verschiebt den restlichen Plan samt Erinnerungen
- Du sagst, wann gegessen wird. Die App rechnet die Backzeit aller Pizzen mit ein
- Plan starten: Erst dann erinnert die App ans Wasser, ans Teigansetzen und an jeden Schritt
- Vor dem Start eine Liste „Bevor es losgeht“ mit allem, was du brauchst
- Raumtemperatur, Kneten mit Maschine oder von Hand, Ofentemperatur und Backzeit einstellbar
- Mehl: Tempasto-Mix, klassisch Tipo 00, mit Vollkorn oder eine eigene Mischung aus bis zu drei Mehlen
- Nachtruhe einstellbar: In diese Zeit legt die App keine Handgriffe
- Zuschlag von 3 oder 5 % für den Teig, der an Schüssel und Händen hängen bleibt
- Zeitplan und Mengen als Text teilen, zum Beispiel per WhatsApp

**Pizzen und Einkauf**
- Pizzen von der Karte wählen oder eigene zusammenstellen
- Die Einkaufsliste schreibt sich selbst, in Gramm
- Mit Ersatz aus dem Supermarkt, falls es die Caputo-Mehle nicht gibt
- Getrennt nach „Jetzt“ und „Frisch kaufen“, damit Mozzarella und Basilikum nicht zu früh im Kühlschrank liegen
- Liste kopieren oder direkt per WhatsApp teilen

**Backen**
- Das *Programma* zeigt den ganzen Ablauf auf einen Blick, mit Kühlschrank- und Raumtemperatur-Phasen. Es öffnet sich mit einem Tipp auf den Zeitstrahl
- Der Backmodus läuft direkt auf der Startseite, die anderen Reiter bleiben erreichbar. Er führt durch jeden Schritt: Mengen, Handgriffe, „Fertig, wenn …“-Kriterien und eine ausführliche Anleitung
- Pausen laufen mit Countdown, lange Gare mit wachsendem Teigling und Gare in Prozent
- Die Farbe zeigt die Phase: kühles Blau im Kühlschrank, warmes Beige bei Raumtemperatur
- Ofenprofil für Gas-, Holz- und Elektro-Pizzaofen oder den Backofen mit Stein. Temperatur, Backzeit und Anheizzeit richten sich danach
- Ofen-Timer für mehrere Pizzen gleichzeitig, mit Hinweis zum Drehen

**Android-App**
- Erinnerungen auch bei geschlossener App, mit „Erledigt“ und „+10 Min“ direkt in der Benachrichtigung
- Antippen der Erinnerung öffnet direkt den aktuellen Schritt
- Bildschirm bleibt im Backmodus an
- Fachbegriffe wie Autolyse oder Stockgare lassen sich antippen und werden erklärt
- Versehentlich abgebrochen? 10 Sekunden lang lässt sich das rückgängig machen
- Ellbogen-Modus: lange irgendwo drücken heißt *Erledigt*, wenn die Hände voller Teig sind
- Passt sich an Handy und Tablet an
- Läuft komplett offline

## Das Rezept

Tempasto arbeitet mit einem festen Grundrezept:

| | |
|---|---|
| Mehl | Tempasto-Mix (Caputo Cuoco, Nuvola, Semola 1.000 : 1.000 : 300), klassisch Tipo 00, mit Vollkorn oder eigene Mischung |
| Salz | 2,8 % aufs Mehl |
| Öl | keins im Teig, wie in Neapel |
| Wasser | 58 bis 70 % |
| Hefe | frisch oder trocken, von der App berechnet |
| Teiglinge | 250, 280 oder 300 g |

Ablauf: Mehl und Wasser mischen, Autolyse, Kneten, Falten und ab in den Kühlschrank, Portionieren, Akklimatisieren, Backen.

## Installieren

Tempasto gibt es (noch) nicht im Play Store. Die fertige APK liegt unter **[Releases](../../releases)**.

1. Die neueste `Tempasto-….apk` auf dem Handy herunterladen
2. Beim ersten Mal erlauben, dass der Browser Apps installieren darf
3. Installieren und Benachrichtigungen zulassen

Updates werden einfach über die alte Version installiert, die Daten bleiben erhalten.

## Technik

- Die App ist eine einzelne HTML-Datei (`www/index.html`) ohne Framework und ohne externe Abhängigkeiten
- Für Android wird sie mit [Capacitor](https://capacitorjs.com) verpackt
- Native Funktionen: Benachrichtigungen, Teilen, Dateien, Bildschirm-an, Zurück-Taste
- Die Verbindung zwischen App und Android steckt in `www/bridge.js`
- Gespeichert wird nur lokal auf dem Gerät

```
www/            Die App (HTML, Brücke zu Android, Schriften)
android/        Android-Projekt (Capacitor)
tools/          Hilfsskripte zum Bauen von www/ und der App-Symbole
.github/        Bauanleitung für GitHub Actions
docs/           Screenshots
```

## Selbst bauen

Die APK wird über GitHub Actions gebaut, und zwar nur auf Knopfdruck:

**Actions → APK bauen → Run workflow**

Nach etwa 5 bis 10 Minuten liegt die signierte APK unter *Releases*.

Signiert wird mit einem Schlüssel, der nicht im Repository liegt, sondern als GitHub-Secret hinterlegt ist (`KEYSTORE_BASE64`, `KEYSTORE_PASSWORD`, `KEY_ALIAS`, `KEY_PASSWORD`). Wer das Projekt selbst baut, braucht einen eigenen Schlüssel.

Lokal geht es mit Node 22, JDK 21 und dem Android SDK:

```bash
npm ci
npx cap sync android
cd android && ./gradlew assembleRelease
```

## Datenschutz

Tempasto sammelt keine Daten und sendet nichts an den Entwickler. Planung, Pizzen und Einstellungen liegen nur auf deinem Gerät. Eine Sicherung kannst du unter *Mehr → Daten sichern* selbst erstellen.

## Lizenz

Der Code steht unter der [MIT-Lizenz](LICENSE). Die Schriften (Bricolage Grotesque, Figtree, IBM Plex Mono) stehen unter der SIL Open Font License, Capacitor unter der MIT-Lizenz.

---

*Tempasto · fatto a mano* von Maximilian Welter
