# Środowiska wirtualne w Python'ie

## Biblioteka `virtualenv`

Do obsługi środowisk wirtualnych wykorzystujemy bibliotekę `virtualenv`.

Instalacja biblioteki (wystarczy wykonać jeden raz)

```bash
pip install virtualenv
```

lub

```bash
python -m pip install virtualenv
```

## Tworzenie nowego środowiska wirtualnego

```bash
python -m venv nazwa_srodowiska
```

## Aktywacja środowiska

```bash
nazwa_srodowiska\Scripts\activate
```

Jeżeli to nie zadziała ze względu na błąd typu

```
nazwa_srodowiska\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies
```

to należy najpierw wykonać

```bash
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
```

## Zapis wymaganych paczek do pliku `requirements.txt`

```bash
pip freeze > requirements.txt
```

lub

```bash
python -m pip freeze > requirements.txt
```

## Instalacja paczek z pliku `requirements.txt`

```bash
pip install -r requirements.txt
```

lub

```bash
python -m pip install -r requirements.txt
```