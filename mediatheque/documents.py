"""Les documents de la mediatheque : la classe abstraite Document et ses
deux sous-classes concretes, Livre et DVD."""

from abc import ABC, abstractmethod


class Document(ABC):
    """Un document empruntable. Abstraite : on n'instancie que ses sous-classes."""

    def __init__(self, titre, annee, code):
        self._titre = titre
        self._annee = annee
        self._code = code
        self._disponible = True

    @property
    def titre(self):
        return self._titre

    @property
    def annee(self):
        return self._annee

    @property
    def code(self):
        return self._code

    @property
    def disponible(self):
        return self._disponible

    @abstractmethod
    def duree_pret(self):
        """Nombre de jours de pret autorise pour ce type de document."""
        raise NotImplementedError

    def _marquer_emprunte(self):
        self._disponible = False

    def _marquer_rendu(self):
        self._disponible = True

    def __str__(self):
        return (
            f'{type(self).__name__} "{self._titre}" ({self._annee}) '
            f"- a rendre sous {self.duree_pret()} jours"
        )

    def __eq__(self, other):
        if not isinstance(other, Document):
            return NotImplemented
        return self._code == other._code

    def __hash__(self):
        return hash(self._code)


class Livre(Document):
    """Un livre : prete pour 21 jours."""

    DUREE_PRET = 21

    def __init__(self, titre, annee, code, auteur, nb_pages):
        super().__init__(titre, annee, code)
        self._auteur = auteur
        self._nb_pages = nb_pages

    @property
    def auteur(self):
        return self._auteur

    @property
    def nb_pages(self):
        return self._nb_pages

    def duree_pret(self):
        return self.DUREE_PRET

    def __str__(self):
        return super().__str__() + f", de {self._auteur} ({self._nb_pages} pages)"


class DVD(Document):
    """Un DVD : prete pour 7 jours."""

    DUREE_PRET = 7

    def __init__(self, titre, annee, code, realisateur, duree_min):
        super().__init__(titre, annee, code)
        self._realisateur = realisateur
        self._duree_min = duree_min

    @property
    def realisateur(self):
        return self._realisateur

    @property
    def duree_min(self):
        return self._duree_min

    def duree_pret(self):
        return self.DUREE_PRET

    def __str__(self):
        return super().__str__() + f", realise par {self._realisateur} ({self._duree_min} min)"
