from siteCollaviz import postToDict
from siteCollaviz import connexion
from siteCollaviz import reponse
from siteCollaviz import lecture
from siteCollaviz import tempsEcriture
from siteCollaviz import investissement

def calculsIndicateurs(fichier):
    data = pd.read_csv(fichier, encoding='utf-8')
    Dict = postToDict.PostToDict(data)
    tempsMoyenConnexiontdelille = connexion.tempsMoyenConnexion(data, 'tdelille')
    tempsMoyenConnexionall = connexion.tempsMoyenConnexionall(data)
    tempsMoyenPostReponsetdelille = reponse.tempsMoyenPostReponse(data, Dict, 'tdelille')
    tempsMoyenPostReponseall = reponse.tempsMoyenPostReponseall(data, Dict)
    tempsMoyenPostLecturetdelille = lecture.tempsMoyenPostLecture(data, Dict, 'tdelille')
    tempsMoyenPostLectureall = lecture.tempsMoyenPostLectureall(data, Dict)
    tempsMoyenEcrituretdelille = tempsEcriture.tempsEcritureReponseMoyen(data, 'tdelille')
    tempsMoyenEcritureall = tempsEcriture.tempsEcritureReponseMoyenToutLeMonde(data)
    res = [[tempsMoyenEcrituretdelille,10,tempsMoyenConnexiontdelille,tempsMoyenPostLecturetdelille,tempsMoyenPostReponsetdelille], [tempsMoyenEcritureall,15,tempsMoyenConnexionall,tempsMoyenPostLectureall,tempsMoyenPostReponseall]]
    return res

def calculsNbActions(data):
    moyenneNBAction = investissement.nbActionsUtilisateurMoy(data, ["Répondre à un message", "Connexion", "Poster un nouveau message", "Afficher le contenu d'un message"], ["tdelille", "mmay", "ddaniaupotter", "gachort"])
    nbAction = investissement.nbActionsUtilisateur(data, ["Répondre à un message", "Connexion", "Poster un nouveau message", "Afficher le contenu d'un message"], ["tdelille", "mmay", "ddaniaupotter", "gachort"])
    res = [nbAction[0], nbAction[1], nbAction[2], nbAction[3], moyenneNBAction]
    return res
