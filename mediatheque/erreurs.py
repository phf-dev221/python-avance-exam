"""Exceptions propres a la mediatheque."""


class MediathequeError(Exception):
    """Classe de base pour toutes les erreurs de la mediatheque."""


class DocumentIndisponible(MediathequeError):
    """Leve quand on tente d'emprunter un document deja emprunte."""


class TropDEmprunts(MediathequeError):
    """Leve quand un adherent depasse la limite de 3 emprunts."""


class DocumentInconnu(MediathequeError):
    """Leve quand le code d'un document ne correspond a rien."""


class AdherentInconnu(MediathequeError):
    """Leve quand le numero d'un adherent ne correspond a personne."""
