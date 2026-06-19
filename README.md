# Python pytest testy – QA portfólio

**Autor:** František Radoš  
**Dátum:** 2026-06-19

---

## Stav projektu

![CI](https://github.com/Frantisek-Rados/python-pytest-tests/actions/workflows/ci.yml/badge.svg)

Všetky testy automaticky bežia na GitHub Actions po každom pushnutí. Aktuálny stav: **všetky testy prechádzajú**.

---

## Obsah repozitára

| Súbor | Popis |
|-------|-------|
| `test_prvy.py` | Prvý automatizovaný test (assert 1+1 == 2) |
| `test_api.py` | API testy s `requests` – GET /posts/1, kontrola statusu a JSON title |
| `test_parametrizacia.py` | Parametrizovaný test – jeden test, 5 rôznych ID (1, 2, 3, 4, 5) |
| `test_playwright_uvod.py` | UI test s Playwright – otvorenie stránky, kontrola nadpisu |
| `test_login_pom.py` + `pages/` | UI test s Page Object Model (POM) – prihlásenie na SauceDemo |
| `.github/workflows/ci.yml` | CI/CD pipeline – automatické spúšťanie testov na GitHub Actions |

---

## Spustenie testov

1. Nainštaluj pytest:
```bash
pip install pytest
```

2. Nainštaluj requests (pre API testy):
```bash
pip install requests
```

3. Nainštaluj Playwright (pre UI testy):
```bash
pip install playwright pytest-playwright
playwright install
```

4. Spusti všetky testy:
```bash
pytest
```

Alebo spusti konkrétny súbor:
```bash
pytest test_api.py
```

---

## Čo už viem / Čo som sa naučil

- ✅ Základy pytest (assert, funkcie `test_*`)
- ✅ API testy s `requests` (GET, status kód, JSON asercie)
- ✅ Parametrizácia – jeden test, viac vstupov (`@pytest.mark.parametrize`)
- ✅ Page Object Model (POM) – čisté a udržiavateľné UI testy
- ✅ Playwright – automatizácia prehliadača (vrátane headless režimu pre CI)
- ✅ Práca s GitHub a README
- ✅ **GitHub Actions (CI/CD)** – automatické spúšťanie testov po každom pushnutí

---

## GitHub Actions (CI/CD)

Tento repozitár používa GitHub Actions na automatické spúšťanie testov. Pipeline je definovaná v `.github/workflows/ci.yml`.

**Čo sa stane po každom pushnutí?**
1. Spustí sa čistý Ubuntu runner
2. Nainštaluje sa Python 3.11
3. Nainštalujú sa závislosti (pytest, requests, playwright, pytest-playwright)
4. Playwright si stiahne prehliadače
5. Spustia sa všetky testy
6. Výsledok (zelená/červená fajka) sa zobrazí pri commite

---

## Najbližšie plány

- Ďalšie testovacie scenáre (napr. negatívne testy, rôzne používateľské roly)
- Playwright – pokročilé selektory a čakania
- Generovanie testovacích dát

---

## Kontakt

Ak máš otázky k tomuto projektu, napíš mi na GitHub.

