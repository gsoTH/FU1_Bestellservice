# requirements installieren
Die genutzten Erweiterungen sind in der Datei /api/requirements.txt aufgelistet. Diese können mit pip installiert werden:

#### Windows
```
pip install -r .\api\requirements.txt 
```

## venv
### erstellen
```
python -m venv [bezeichnung] 
```
Ein Beispiel wäre: ``python -m venv my-venv `` Hierdurch wird ein Ordner my-venv innerhalb meines Repos erstellt.

### aktivieren
Innerhalb der erstellten Umgebung gibt es ein Skript, das wir ausführen müssen.
#### Windows
```
# In cmd.exe
venv\Scripts\activate.bat
# In PowerShell
venv\Scripts\Activate.ps1
```

#### Linux and MacOS
```
$ source myvenv/bin/activate
```

### deaktivieren
Der Befehl ist in allen Betriebssystemen identisch: 
``deactivate``