# Bestellservice

:dart: Ziele:
 - Planung der Nachrichtenflüsse mit UML-Sequenzdiagrammen
 - Implementierung und Test mit [FastAPI](https://fastapi.tiangolo.com/)

:no_entry: Abgrenzungen:
 - Keine Authentifizierung
 - Kein Frontend

:clipboard: **arbeitsauftrag**
 - Planen Sie die restlichten Nachrichtenflüsse, indem Sie geeignete UML-Sequenzdiagramme erzeugen.
 - Identifizieren Sie Wissenslücken (und sammeln Sie diese an geeigneter Stelle)
 - Beginnen Sie mit der Implementierung

## Auszug aus dem Lastenheft
### Beschreibung des Ist-Zustands
Ein Pizza-Restaurant hat bisher sein Angebot über eine Webseite veröffentlicht und Bestellungen via Telefon entgegengenommen. Ein geeignetes Beispiel ist im Order [api](api/) abgelegt.

### Beschreibung des Soll-Zustands
Um einen größeren Marktanteil zu erreichen, sollen diese Bestellungen in Zukunft direkt über die Webseite (oder durch direkten Zugriff auf die API durch Drittanbieter-Webseiten) erfolgen.
Die Kunden sollen über das aktuelle Menu abfragen können und anschließend die Bestellung übermitteln. Zu jeder Bestellung soll eine Telefonnummer und ein Name übermittelt werden. Der Kunde erhält anschließend den Preis der Bestellung und eine Bestellnummer.

Vor Ort benötigen die Mitarbeiter eine Übersicht aller aktuellen Bestellungen. Der Einfachheit halber gehen wir davon aus, dass jede Bestellung innerhalb einer Stunde erledigt ist. Es müssen also nur Bestellungen angezeigt werden, die innerhalb der letzten 60 Minuten eingegangen sind.

## Fachkonzept
Ausgehend von der Situationsbeschreibung wurden bereits erste UML-Diagrame erstellt.

### Anwendungsfalldiagramm
Das nachfolgende UML-Use-Case Diagramm zeigt die Anwendungsfälle, die das neue System zur Verfügung stellen soll.

![UML-UseCase Diagramm](diagramme/UML-UseCase.drawio.svg)

### Sequenzdiagramm
Die Abfolge der Nachrichtenflüsse soll in UML-Sequenzdiagrammen dargestellt werden. Für jeden Anwendungsfall soll ein Sequenzdiagramm erstellt werden. Zur Modellierung wurde der [Live-Editor](https://mermaid.live) von [Mermaid.js](https://mermaid.js.org/syntax/sequenceDiagram.html#sequence-diagrams) verwendet.

#### 1. Menu abfragen
[![](https://mermaid.ink/img/pako:eNplUV1PwjAU_SvNTUw0DtwYhdEHEz-IaOQjgSezxJTtMqqsw65VgfDPfOOP2a0YTexTc849536cHSRFisCgxDeDMsFbwTPF81gS-9ZcaZGINZea3KwESv0fv5rc_wdvr4dTh56ccKMLafI5Koc4o8bl5bmVMnLXn5GLHKVxrMUqqjJgJEP9XFGnZ46s0EbjrFELf0lGFJZmpf861CWJQq7x-aUs5C9n9W6EP70ZeRSlRpKiIu-oFoevbM4VSjLky9UWhUbpDWazScv3ndFoPOsTJbKlJsWC_PgNhNV_CJUSFJI8TMcjsjXq8JW8ZpjhHGUzluBBjirnIrVX31VuMegl5hgDs98UF7xaBWK5t6XV8aYbmQDTyqAHZp3ajY4hAVvwVWlRTIUu1NAlWQfqgc0B2A4-gQUhbYZB1PZpQIOw0215sAHW6TXDKOxSvxdQ2uqG7b0H26Kwpn4z6kUhbffCVhRFlLZrs6eac1OowmTLY_f9N9IKtk0?type=png)](https://mermaid.live/edit#pako:eNplUV1PwjAU_SvNTUw0DtwYhdEHEz-IaOQjgSezxJTtMqqsw65VgfDPfOOP2a0YTexTc849536cHSRFisCgxDeDMsFbwTPF81gS-9ZcaZGINZea3KwESv0fv5rc_wdvr4dTh56ccKMLafI5Koc4o8bl5bmVMnLXn5GLHKVxrMUqqjJgJEP9XFGnZ46s0EbjrFELf0lGFJZmpf861CWJQq7x-aUs5C9n9W6EP70ZeRSlRpKiIu-oFoevbM4VSjLky9UWhUbpDWazScv3ndFoPOsTJbKlJsWC_PgNhNV_CJUSFJI8TMcjsjXq8JW8ZpjhHGUzluBBjirnIrVX31VuMegl5hgDs98UF7xaBWK5t6XV8aYbmQDTyqAHZp3ajY4hAVvwVWlRTIUu1NAlWQfqgc0B2A4-gQUhbYZB1PZpQIOw0215sAHW6TXDKOxSvxdQ2uqG7b0H26Kwpn4z6kUhbffCVhRFlLZrs6eac1OowmTLY_f9N9IKtk0)

#### 2. Bestellung aufgeben
#### 3. Bestellungen einsehen



