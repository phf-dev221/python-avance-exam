"""La classe Mediatheque : le point d'entree qui relie documents et adherents."""

from itertools import count

from .adherent import Adherent
from .erreurs import AdherentInconnu, DocumentIndisponible, DocumentInconnu


class Mediatheque:
    """Gere les documents, les adherents, et les prets."""

    def __init__(self, nom):
        self._nom = nom
        self._documents = {}
        self._adherents = {}
        self._compteur_adherents = count(1)

    @property
    def nom(self):
        return self._nom

    def ajouter_document(self, document):
        self._documents[document.code] = document

    def inscrire(self, nom):
        numero = f"A{next(self._compteur_adherents):03d}"
        adherent = Adherent(nom, numero)
        self._adherents[numero] = adherent
        return adherent

    def _trouver_document(self, code):
        try:
            return self._documents[code]
        except KeyError:
            raise DocumentInconnu(f'Aucun document avec le code "{code}"') from None

    def _trouver_adherent(self, numero):
        try:
            return self._adherents[numero]
        except KeyError:
            raise AdherentInconnu(f'Aucun adherent avec le numero "{numero}"') from None

    def emprunter(self, numero, code):
        adherent = self._trouver_adherent(numero)
        document = self._trouver_document(code)

        if not document.disponible:
            raise DocumentIndisponible(f'Le document "{document.titre}" est deja emprunte')

        adherent._ajouter_emprunt(document)
        document._marquer_emprunte()
        return document

    def rendre(self, numero, code):
        adherent = self._trouver_adherent(numero)
        document = self._trouver_document(code)

        adherent._retirer_emprunt(document)
        document._marquer_rendu()
        return document

    def rechercher(self, mot):
        mot = mot.lower()
        return [doc for doc in self._documents.values() if mot in doc.titre.lower()]

    def documents_disponibles(self):
        return [doc for doc in self._documents.values() if doc.disponible]

    def emprunts_de(self, numero):
        adherent = self._trouver_adherent(numero)
        return adherent.emprunts
