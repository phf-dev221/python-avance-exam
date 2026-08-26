"""La classe Adherent."""

from .erreurs import TropDEmprunts

LIMITE_EMPRUNTS = 3


class Adherent:
    """Un adherent de la mediatheque et ses emprunts en cours."""

    def __init__(self, nom, numero):
        self._nom = nom
        self._numero = numero
        self._emprunts = []

    @property
    def nom(self):
        return self._nom

    @property
    def numero(self):
        return self._numero

    @property
    def emprunts(self):
        return list(self._emprunts)

    def peut_emprunter(self):
        return len(self._emprunts) < LIMITE_EMPRUNTS

    def _ajouter_emprunt(self, document):
        if not self.peut_emprunter():
            raise TropDEmprunts(
                f"{self._nom} a deja {LIMITE_EMPRUNTS} documents empruntes"
            )
        self._emprunts.append(document)

    def _retirer_emprunt(self, document):
        self._emprunts.remove(document)

    def __len__(self):
        return len(self._emprunts)

    def __str__(self):
        return f"{self._nom} (#{self._numero})"
