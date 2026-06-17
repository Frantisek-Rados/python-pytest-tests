# Python pytest testy – QA portfólio

**Autor:** František Radoš  
**Dátum:** 2026-06-17

---

## Obsah repozitára

| Súbor | Popis |
|-------|-------|
| `test_prvy.py` | Prvý automatizovaný test (assert 1+1 == 2) |
| `test_api.py` | API testy s `requests` – GET /posts/1, kontrola statusu a JSON title |
| `test_parametrizacia.py` | Parametrizovaný test – jeden test, 5 rôznych ID (1, 2, 3, 4, 5) |

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

3. Spusti všetky testy:
```bash
pytest
```

Alebo spusti konkrétny súbor:
```bash
pytest test_prvy.py
pytest test_api.py
pytest test_parametrizacia.py
```

---


## Kontakt
Ak máš otázky k tomuto projektu, napíš mi na GitHub.

```

