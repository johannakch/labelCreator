# Label Creator

Dieses Projekt enthält eine Python Applikation mit einer Benutzeroberfläche, die die Erstellung von Informationsetiketten für Druckplattenpakete realisiert. 


# Motivation:
Druckplatten, als Teil der Druckvorstufe, sind individuelle Vorlagen für Druckerzeugnisse, die nach Bebilderung und Entwicklung die entsprechende Abbildung des späteren Erzeugnisses sowie Informationen zu Farbe, Bogenart uvm. enthalten. Die Druckplatten dienen zur Erzeugung des Endergebnisses auf dem Papier (oder auch anderen Materialien) in Druckereien. In sogenannten CIP3-Files sind alle Informationen zu einem Druckauftrag gespeichert. Die Druckplatten werden geordnet in Pakete zum Transport an die Druckereien verpackt.
Die Pakete bekommen anschließend din A5 große Etiketten mit Informationen zu deren Inhalt. Um die manuelle Beschriftung solcher Etiketten zu ersetzen, hilft die Applikation, den Vorgang weitgehend zu automatisieren bzw. mit wenigen Klicks schneller und einfacher zu gestalten.

# Funktionsweise:
Wird die Applikation gestartet öffnet sich ein Startfenster, in dem man die gewünschte CIP3 Datei zu dem Druckauftrag auswählt. 
![alt text](https://raw.githubusercontent.com/johannakch/labelCreator/editing/suchdialog2.png)
Im nächsten Schritt werden automatisch die Werte wie Kundenname der Druckerei, Auftragsnummer und Auftragsname aus der zuvor ausgewählten Datei ausgelesen.
![alt text](https://raw.githubusercontent.com/johannakch/labelCreator/editing/app1.png)
Des Weiteren kann der Benutzer auswählen, um welches Teilprodukt es sich handelt (Umschlag, Inhalt oder individuelle Bezeichnung).  
Anschließend wird die benötigte Anzahl an Etiketten ausgewählt und zu jedem Etikett die Bogenart sowie die Anzahl der Farben angegeben.
![alt text](https://raw.githubusercontent.com/johannakch/labelCreator/editing/app3.png)
Mit Klick auf "PDF" wird ein .pdf Dokument erzeugt, das alle Etiketten auf jeweils einer Seite enthält, welche nun ausgedruckt und an den Paketen angebracht werden können.
![alt text](https://raw.githubusercontent.com/johannakch/labelCreator/editing/app4.png)

# Aufbau:
Die Applikation ist in Python geschrieben und nutzt das Standardtool Tkinter für die Benutzeroberfläche. Teilfunktionen wurden in einzelne Klassen ausgelagert. Zur Generierung von PDF's wird die ReportLab PDF Library verwendet.
