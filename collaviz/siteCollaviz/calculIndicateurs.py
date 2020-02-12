from siteCollaviz import postToDict
from siteCollaviz import connexion
from siteCollaviz import reponse
from siteCollaviz import lecture
from siteCollaviz import tempsLecture
from siteCollaviz import tempsEcriture
from siteCollaviz import investissement
from siteCollaviz import gestionDate
import pandas as pd


def calculsIndicateurs(fichier, user, groupe, date1, date2):
    data = pd.read_csv(fichier, encoding='utf-8')
    data = gestionDate.gestionDateDataframe(data, date1, date2)
    Dict = postToDict.PostToDict(data)
    tempsMoyenConnexiontdelille = connexion.tempsMoyenConnexion(data, user)
    tempsMoyenConnexionall = connexion.tempsMoyenConnexionall(data)
    tempsMoyenConnexionGroupe = connexion.tempsMoyenConnexionGroupe(data, groupe)

    tempsMoyenLecturetdelille = tempsLecture.tempsLectureReponseMoyen(data, user)
    tempsMoyenLectureall = tempsLecture.tempsLectureReponseMoyenToutLeMonde(data)
    tempsMoyenLectureGroupe = tempsLecture.tempsLectureReponseMoyenGroupe(data, groupe)

    tempsMoyenPostReponsetdelille = reponse.tempsMoyenPostReponse(data, Dict, user)
    tempsMoyenPostReponseall = reponse.tempsMoyenPostReponseall(data, Dict)
    tempsMoyenPostReponseGroupe = reponse.tempsMoyenPostReponseGroupe(data, Dict, groupe)

    tempsMoyenPostLecturetdelille = lecture.tempsMoyenPostLecture(data, Dict, user)
    tempsMoyenPostLectureall = lecture.tempsMoyenPostLectureall(data, Dict)
    tempsMoyenPostLectureGroupe = lecture.tempsMoyenPostLectureGroupe(data, Dict, groupe)

    tempsMoyenEcrituretdelille = tempsEcriture.tempsEcritureReponseMoyen(data, user)
    tempsMoyenEcritureall = tempsEcriture.tempsEcritureReponseMoyenToutLeMonde(data)
    tempsMoyenEcritureGroupe = tempsEcriture.tempsEcritureReponseMoyenGroupe(data, groupe)

    res = [[tempsMoyenEcrituretdelille,tempsMoyenLecturetdelille,tempsMoyenConnexiontdelille,tempsMoyenPostLecturetdelille,tempsMoyenPostReponsetdelille],
     [tempsMoyenEcritureall,tempsMoyenLectureall,tempsMoyenConnexionall,tempsMoyenPostLectureall,tempsMoyenPostReponseall],
     [tempsMoyenEcritureGroupe,tempsMoyenLectureGroupe,tempsMoyenConnexionGroupe,tempsMoyenPostLectureGroupe,tempsMoyenPostReponseGroupe]]
    return res

def calculsNbActions(fichier, users):
    data = pd.read_csv(fichier, encoding='utf-8')
    nbAction = investissement.nbActionsUtilisateur(data, ["Répondre à un message", "Connexion", "Poster un nouveau message", "Afficher le contenu d'un message"], users)
    moyenneNBAction = investissement.nbActionsUtilisateurMoy(data, ["Répondre à un message", "Connexion", "Poster un nouveau message", "Afficher le contenu d'un message"], users)
    res = []
    for i in range (len(users)):
        res.append(nbAction[i])
    res.append(moyenneNBAction)

    return res
