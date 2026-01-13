# Analiza danych COVID-19 📊

Krótki opis projektu, plików i instrukcje uruchomienia.

---

## Opis projektu

Projekt zawiera zbiory danych i skrypty do wstępnego przetwarzania oraz prostych analiz związanych z danymi COVID-19 (m.in. nadmiarowe zgony i potwierdzone zgony na 100k mieszkańców).

## Struktura repozytorium

- `data/` – dane źródłowe (plik `covid_data.csv`) oraz `README.MD` specyficzne dla folderu danych.
- `notebooks/` – notatniki analityczne (jeśli występują).
- `scripts/` – skrypty Pythona do przetwarzania danych, np. `scripts/data_cleaning.py`.
- `outputs/` – miejsce na wygenerowane wykresy i wyniki analizy.

## Najważniejsze skrypty

- `scripts/data_cleaning.py` – wczytuje `data/covid_data.csv`, oczyszcza dane (mapowanie kolumn, konwersje typów), i wyświetla Top 10 państw według liczby zgonów.

Przykładowe uruchomienie:

```bash
python ./scripts/data_cleaning.py
```

> Uwaga: skrypt oczekuje pliku `data/covid_data.csv` i poprawnych nagłówków; skrypt zawiera mechanizmy mapowania typowych nazw kolumn (`Day` → `date`, `Entity` → `location`).

## Zależności

Zalecane pakiety Python:

```bash
pip install pandas numpy matplotlib
```

**Autor:** 
Przemysław Radomski
