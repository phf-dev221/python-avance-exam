import pytest

from mediatheque import DVD, DocumentIndisponible, Document, Livre, Mediatheque, TropDEmprunts


def creer_mediatheque_avec_un_livre():
    media = Mediatheque("Test")
    livre = Livre("Titre", 2020, "L001", auteur="X", nb_pages=100)
    media.ajouter_document(livre)
    awa = media.inscrire("Awa")
    return media, livre, awa


def test_emprunt_rend_le_document_indisponible():
    media, livre, awa = creer_mediatheque_avec_un_livre()

    media.emprunter(awa.numero, "L001")

    assert not livre.disponible


def test_emprunter_document_deja_pret_leve_document_indisponible():
    media, livre, awa = creer_mediatheque_avec_un_livre()
    media.emprunter(awa.numero, "L001")

    with pytest.raises(DocumentIndisponible):
        media.emprunter(awa.numero, "L001")


def test_quatrieme_emprunt_leve_trop_d_emprunts():
    media = Mediatheque("Test")
    for i in range(4):
        media.ajouter_document(Livre(f"Livre {i}", 2020, f"L00{i}", auteur="X", nb_pages=100))
    awa = media.inscrire("Awa")

    media.emprunter(awa.numero, "L000")
    media.emprunter(awa.numero, "L001")
    media.emprunter(awa.numero, "L002")

    with pytest.raises(TropDEmprunts):
        media.emprunter(awa.numero, "L003")


def test_rendre_remet_le_document_en_circulation():
    media, livre, awa = creer_mediatheque_avec_un_livre()
    media.emprunter(awa.numero, "L001")

    media.rendre(awa.numero, "L001")

    assert livre.disponible


def test_duree_pret_livre_et_dvd():
    livre = Livre("Titre", 2020, "L001", auteur="X", nb_pages=100)
    dvd = DVD("Film", 2020, "D001", realisateur="Y", duree_min=90)

    assert livre.duree_pret() == 21
    assert dvd.duree_pret() == 7


def test_rechercher_est_insensible_a_la_casse():
    media = Mediatheque("Test")
    media.ajouter_document(
        Livre("L'Aventure ambigue", 1961, "L001", auteur="Cheikh Hamidou Kane", nb_pages=191)
    )

    resultats = media.rechercher("aventure")

    assert len(resultats) == 1
    assert resultats[0].code == "L001"


def test_document_est_abstraite():
    with pytest.raises(TypeError):
        Document("x", 2020, "C1")
