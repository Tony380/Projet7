"""Papybot random sentences file"""
import random

no_result = ["Je n'ai rien trouvé à ce sujet, peux tu préciser?",
             "Je ne me souviens plus très bien, j'ai besoin de précisions...",
             "Je ne sais plus, il faut que tu m'éclaires un peu...",
             "Aucune idée, précise pour voir?"]

adress = ["Ah oui! Je connais bien, voici l'adresse : ",
          "Bien sûr, l'adresse est : ",
          "Je me souviens bien de l'adresse : ",
          "Oui, j'y suis déjà allé, l'adresse c'est : "]

wiki = ["D'ailleurs, je ne t'ai pas raconté! ",
        "Au fait, je me rapelle! ",
        "Maintenant que j'y pense... ",
        "Si mes souvenirs sont bons, "]


def sentence():
    """Return a random sentence"""
    res = random.choice(no_result)
    adr = random.choice(adress)
    wik = random.choice(wiki)
    return {'res': res, 'adr': adr, 'wik': wik}
