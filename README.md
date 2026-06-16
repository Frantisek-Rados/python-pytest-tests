# Python pytest testy – QA portfólio

**Autor:** František Radoš  
**Dátum:** 2026-06-16

---

## Obsah repozitára

| Súbor | Popis |
|-------|-------|
| `test_prvy.py` | Prvý automatizovaný test (assert 1+1 == 2) |
| `test_api.py` | API testy s `requests` – GET /posts/1, kontrola statusu a JSON title |

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
pytest test_api.py
```

