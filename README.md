# Mini-projet POO — Une mediatheque en Python

Gestion d'une petite mediatheque (livres, DVD, adherents et prets) en Python,
avec un accent mis sur la conception objet : encapsulation, heritage,
polymorphisme et abstraction.

## Lancer la demonstration

```bash
python main.py
```

## Lancer les tests

```bash
pytest -q
```

## Structure du projet

```
mediatheque/
├── __init__.py
├── documents.py    # Document (abstraite), Livre, DVD
├── adherent.py      # Adherent
├── mediatheque.py    # Mediatheque
└── erreurs.py       # MediathequeError et ses sous-classes
tests/
└── test_mediatheque.py
main.py
```

## Auteur

Pape Hamady Fall - M1 DSIA - ISI / 2025-2026
