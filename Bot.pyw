import random
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Application, ContextTypes

from aiogram import Bot, Dispatcher, types ,executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup

import requests


# Importer le module random
import random
Token = '7187221275:AAEmjEjDtWW5NnrCg80qw8PV97bQ8lIPYwU'
PROXY_URL = "http://13.49.226.125:3128"
bot = Bot(token=Token)
dp = Dispatcher(bot)

def incrementer_nb(chaine):
  fichier= "utilisateurs.txt"
  # Ouvrir le fichier en mode lecture et écriture
  with open(fichier, "r+") as f:
    # Lire toutes les lignes du fichier dans une liste
    lignes = f.readlines()
    # Aller au début du fichier
    f.seek(0)
    # Parcourir chaque ligne
    for ligne in lignes:
      # Extraire le nom, l'id et le nb de la ligne
      nom, id, usr,nb = ligne.split(":")
      # Comparer l'id avec la chaîne
      if id.strip() == chaine:
        # Incrémenter le nb de 1
        nb = int(nb) + 1
        # Formater la nouvelle ligne avec le nb mis à jour
        nouvelle_ligne = f"{nom}:{id}:{usr}:{nb}\n"
        # Ecrire la nouvelle ligne dans le fichier
        f.write(nouvelle_ligne)
      else:
        # Ecrire la ligne inchangée dans le fichier
        f.write(ligne)
    # Tronquer le fichier à la position actuelle
    f.truncate()

# Définition de la fonction genererChaine
def genererChaine():
  # Initialiser une liste vide pour stocker les caractères
  caracteres = []
  # Générer 5 chiffres aléatoires entre 0 et 9 et les ajouter à la liste
  for i in range(5):
    chiffre = random.randint(0, 9)
    caracteres.append(str(chiffre))
  # Générer 5 lettres aléatoires entre A et Z et les ajouter à la liste
  for i in range(5):
    lettre = chr(random.randint(65, 90))
    caracteres.append(lettre)
  # Mélanger la liste de caractères
  random.shuffle(caracteres)
  # Convertir la liste en une chaîne et la retourner
  chaine = "".join(caracteres)
  return chaine


# Définition de la fonction mettreInfo
def mettreInfo(chaine):
  # Ouvrir le fichier info.txt en mode lecture et écriture
  fichier = open("info.txt", "r+")
  # Lire le contenu du fichier et le stocker dans une liste de lignes
  lignes = fichier.readlines()
  # Fermer le fichier
  fichier.close()
  # Extraire partie1 et partie2 de la chaîne
  partie1, partie2 = chaine.split(":")
  # Initialiser un booléen pour indiquer si partie1 a été trouvée
  trouve = False
  # Parcourir la liste des lignes
  for i in range(len(lignes)):
    # Si la ligne commence par partie1, la remplacer par la chaîne
    if lignes[i].startswith(partie1):
      lignes[i] = chaine + "\n"
      trouve = True
      break
  # Si partie1 n'a pas été trouvée, ajouter la chaîne à la fin de la liste
  if not trouve:
    lignes.append(chaine + "\n")
  # Ouvrir le fichier info.txt en mode écriture
  fichier = open("info.txt", "w")
  # Écrire la liste des lignes dans le fichier
  fichier.writelines(lignes)
  # Fermer le fichier
  fichier.close()

# Définition de la fonction getInfo
def getInfo(partie1):
  # Ouvrir le fichier info.txt en mode lecture
  fichier = open("info.txt", "r")
  # Lire le contenu du fichier et le stocker dans une liste de lignes
  lignes = fichier.readlines()
  # Fermer le fichier
  fichier.close()
  # Parcourir la liste des lignes
  for ligne in lignes:
    # Si la ligne commence par partie1, extraire et retourner partie2
    if ligne.startswith(partie1):
      partie2 = ligne.split(":",1)[1].strip()
      return partie2
  # Si partie1 n'a pas été trouvée, retourner None
  return None




def recuperer_noms():
  fichier= "utilisateurs.txt"
  # Créer une chaîne vide pour stocker les noms
  chaine_noms = ""
  # Ouvrir le fichier en mode lecture
  with open(fichier, "r") as f:
    # Lire toutes les lignes du fichier
    lignes = f.readlines()
    # Parcourir chaque ligne
    for ligne in lignes:
      # Extraire le nom de la ligne
      nom = ligne.split(":")[0].strip()+" : "+ligne.split(":")[2].strip()
      # Ajouter le nom à la chaîne avec deux sauts de ligne
      chaine_noms += nom + " \n \n"
  # Retourner la chaîne des noms
  return "LISTE DES MEMBRES :  \n \n" + chaine_noms

def enregistrer_id(id, nom,username):
  fichier= "utilisateurs.txt"
  # Ouvrir le fichier en mode lecture et écriture, ou le créer s'il n'existe pas
  with open(fichier, "a+") as f:
    # Aller au début du fichier
    f.seek(0)
    # Lire toutes les lignes du fichier dans une liste
    lignes = f.readlines()
    # Vérifier si l'id existe déjà dans le fichier
    existe = False
    for ligne in lignes:
      # Extraire l'id de la ligne
      id_ligne = ligne.split(":")[1].strip()
      # Comparer l'id avec celui passé en paramètre
      if id_ligne == id:
        # L'id existe déjà, on met le drapeau à True
        existe = True
        break
    # Si l'id n'existe pas, on l'ajoute à la fin du fichier avec le nom
    if not existe:
      # Formater la ligne à écrire
      ligne = f"{nom}:{id}:{username} \n"
      # Ecrire la ligne dans le fichier
      f.write(ligne)

def recuperer_id():
  fichier= "utilisateurs.txt"
  # Créer une liste vide pour stocker les id
  liste_id = []
  # Ouvrir le fichier en mode lecture
  with open(fichier, "r") as f:
    # Lire toutes les lignes du fichier
    lignes = f.readlines()
    # Parcourir chaque ligne
    for ligne in lignes:
      # Extraire l'id de la ligne
      id = ligne.split(":")[1].strip()
      # Convertir l'id en entier
      id = int(id)
      # Ajouter l'id à la liste
      liste_id.append(id)
  # Retourner la liste des id
  return liste_id

def recuperer_idPersonnne(nom):
  fichier="utilisateurs.txt"
  # Ouvrir le fichier en mode lecture
  with open(fichier, "r") as f:
    # Lire toutes les lignes du fichier
    lignes = f.readlines()
    # Parcourir chaque ligne
    for ligne in lignes:
      # Extraire le nom et l'id de la ligne
      id_ligne = ligne.split(":")[1].strip()
      nom_ligne=ligne.split(":")[0].strip()
      # Comparer le nom avec celui passé en paramètre
      if nom_ligne.strip().__contains__(nom) :
        # Retourner l'id correspondant
        return id_ligne.strip()
    # Si le nom n'est pas trouvé, retourner None
    return None


def recuperer_nbPersonnne(ident):
  id=str(ident)
  fichier="utilisateurs.txt"
  # Ouvrir le fichier en mode lecture
  with open(fichier, "r") as f:
    # Lire toutes les lignes du fichier
    lignes = f.readlines()
    # Parcourir chaque ligne
    for ligne in lignes:
      # Extraire le nom et l'id de la ligne
      id_ligne = ligne.split(":")[1].strip()
      nb_ligne=ligne.split(":")[3].strip()
      # Comparer le nom avec celui passé en paramètre
      if id_ligne.strip().__contains__(id) :
        # Retourner l'id correspondant
        return int(nb_ligne)
    # Si le nom n'est pas trouvé, retourner None
    return None


swamp=getInfo("swamp")
img=getInfo("img")
vip=getInfo("vip")
x1=getInfo("1x")
bw=getInfo("bw")
mb=getInfo("mb")
mpr=getInfo("mpr")
lb=getInfo("lb")
gg=getInfo("88")

canal=getInfo("canal")
print(canal)

#button1 = InlineKeyboardButton(text="Commencer", callback_data="In_First_button") 
button2 = InlineKeyboardButton(text="Notre canal officiel 🏆", url=canal) 
keyboard_inline = InlineKeyboardMarkup().add( button2) 


   
        
@dp.message_handler(commands=['membres']) 
async def Membres(message: types.Message): 
  await bot.send_message(chat_id=message.chat.id,text=recuperer_noms())

########################################################################################################################################################
##################################################################################################################################################################
# LES CLAVIERS DE REPONSES 
################################################################################################################################################################   
# Creating the reply keyboard 

async def proposer_clavier3(message: types.Message):
  # Créer un clavier avec les trois boutons et les emoji
  keyboard_reply3 = types.ReplyKeyboardMarkup(
    resize_keyboard=False, one_time_keyboard=False).add("1XBET 🟦📱", "BETWINNER 🟩📱", "MELBET 🎲","MEGAPARI 🟩📱","LINEBET 🎲","888STARZ 🟦📱", "Retour Menu 📋")
  # Envoyer un message avec le clavier
  await message.answer("Choisissez une option parmi les suivantes :", reply_markup=keyboard_reply3)


async def proposer_clavier2(message: types.Message):
  # Créer un clavier avec les trois boutons et les emoji
  keyboard_reply2 = types.ReplyKeyboardMarkup(
    resize_keyboard=False, one_time_keyboard=False).add("C'est fait ✅", "Retour Menu 📋")
  # Envoyer un message avec le clavier
  await message.answer_photo(photo=swamp,caption=f"Ici; vous allez recevoir les prédictions pour le jeu 'SWAMP LAND'\n\n\
 \
\n🛑 Mais pour que les prédictions puissent fonctionner de façon optimale, vous devez obligatoirement créer un nouveau compte 1xbet, MELBET, Linebet ,MEGAPARI,888starz, ou betwinner avec le code promo : {getInfo('code')} ou {getInfo('code2')}  ✅\n\n\
 \
 \
\n\nSi c \'est fait cliquez sur 'C \'est fait ✅'", reply_markup=keyboard_reply2)  
  
async def proposer_clavier4(message: types.Message):
  # Créer un clavier avec les trois boutons et les emoji
  keyboard_reply4 = types.ReplyKeyboardMarkup(
    resize_keyboard=False, one_time_keyboard=False).add("Trouver la bonne case 🔍", "Retour Menu 📋")
  # Envoyer un message avec le clavier
  await message.answer_photo(photo=swamp,caption=f"À fin de recevoir les meilleures prédictions sur 'SWAMP LAND', vous devez être  obligatoirement inscrit avec le code promo : {getInfo('code')} OU {getInfo('code2')}  \
 \
si c \'est fait ✅ , \
cliquez sur 'Trouver la bonne case' pour commencer les prédictions \
 \
👇👇👇👇👇👇", reply_markup=keyboard_reply4)  

async def proposer_clavier5(message: types.Message):
  # Créer un clavier avec les deux boutons
  keyboard_reply5 = types.ReplyKeyboardMarkup(
    resize_keyboard=False, one_time_keyboard=False).add("Soldes 💰", "Retirer 🏧")
  # Envoyer un message avec le clavier
  await message.answer("Choisissez une option parmi les suivantes :", reply_markup=keyboard_reply5)

keyboard_reply1 = types.ReplyKeyboardMarkup(
    resize_keyboard=False, one_time_keyboard=False).add("📱COUPON DU JOUR🔥", "JEU DE PRÉDICTION 🎲", "⚽COUPON VIP⚽", "AIDE❗", "CANAL OFFICIEL⚜️", "GAGNEZ 1000 FCFA💰")
########################################################################################################################################################
##################################################################################################################################################################
# LES CLAVIERS DE REPONSES 
################################################################################################################################################################  


# Handling the /start and /help commands
########################################################################################################################################################
##################################################################################################################################################################
# LES FONCTIONS DE REPONSES CLAVIER
################################################################################################################################################################  

 
@dp.message_handler(commands=['start', 'menu']) 
async def welcome(message: types.Message):
    
    print(message.get_args())
    if message.get_args():
      if str(message.get_args())!=str(message.from_user.id):
        incrementer_nb(str(message.get_args()))
    # Sending a greeting message that includes the reply keyboard 
    await message.answer_photo(photo=img,caption=f"Bonjour {message.from_user.full_name} et bienvenue.\nCe bot vous présente differentes options veuillez choisir l'une d'entre elles en fonction de ce que vous voulez.\n\nMerci.",reply_markup=keyboard_reply1)

    #await message.reply("Choisissez une proposition", reply_markup=keyboard_inline)
    enregistrer_id(str(message.chat.id),message.from_user.full_name,"@"+ str( message.from_user.username))
   

   

########################################################################################################################################################
##################################################################################################################################################################
# LES FONCTIONS DE REPONSES CLAVIER
################################################################################################################################################################  

   
# Handling all other messages 
@dp.message_handler() 
async def check_rp(message: types.Message): 

    if message.text == "📱COUPON DU JOUR🔥": 
        # Responding with a message for the first button 
        await message.reply_photo(photo=img,caption=f"Veuillez vous inscrire sur 1XBET, MELBET, LINEBET ,MEGAPARI,888STARZ, ou BETWINNER avec le code promo : \n \n{getInfo('code2')} OU \n \n{getInfo('code')} ✅ \n \n \nLIENS D'INSCRIPTION: \n \n\n➡️ Lien d'inscription 1xbet🟦 \nhttps://refpa4948989.top/L?tag=d_2146357m_1573c_&site=2146357&ad=1573 \n \n\n➡️ Lien d'inscription BETWINNER 🟩 \n \nhttps://bwredir.com/1YH3 \n \n\n➡️ Lien d'inscription melbet \n \nhttps://refpakrtsb.top/L?tag=d_2584859m_45415c_&site=2584859&ad=45415 \n \n\n➡️ Lien d'inscription 888starz 🔴 \n \n \nhttps://bonuspack.fun/L?tag=d_2931631m_63543c_&site=2931631&ad=63543 \n \n\n➡️ Lien d'inscription  MEGAPARI 📱 \nhttps://refpaiozdg.top/L?tag=d_3192437m_25437c_&site=3192437&ad=25437 \n \n\n➡️ Lien d'inscription  LINEBET 📱 \n\nhttps://jt12.lineorg.com/") 
        await proposer_clavier3(message=message)
    elif message.text == "JEU DE PRÉDICTION 🎲": 
        # Responding with a message for the second button
        await proposer_clavier2(message=message) 
    elif message.text== "⚽COUPON VIP⚽":
        await message.reply_photo(vip,caption=f"Pour avoir accès à notre coupon VIP, veuillez vous inscrire en utilisant le code promo {getInfo('code')} OU {getInfo('code2')} \nVoici les bookmakers où vous pouvez le code : \n 1XBET, MELBET, LINEBET ,MEGAPARI,888STARZ, ou BETWINNER\nAprès votre inscription; bien vouloir envoyer les captures d'écran qui montrent que vous avez utilisé nos codes promo.\nMerci.")
 
    elif message.text== "AIDE❗":
        await message.reply(f"✅1XBET pronos: \nCette option n'est disponible que pour ceux qui veulent créer un nouveau compte 1XBET \n \n\n➡️ Veuillez donc créer un nouveau compte en utilisant le code promo ✅ {getInfo('code')} OU {getInfo('code2')} ✅ \n \n\n➡️Ensuite, faites une capture d’écran et envoyez-là ici!!! \n \n🔴NB: Toute personne envoyant de fausses captures d’écrans sera immédiatement expulsée du bot !!! \n \nEnvoyez la capture d’écran ici 👇 \n \n\n➡️Pour avoir accès au coupon gratuit, vous devez obligatoirement créer un nouveau compte 1xbet en utilisant notre code promo : ✅ \n{getInfo('code')} OU {getInfo('code2')} ✅ \n \n\n➡️Ensuite vous devrez faire votre premier dépôt pour commencer à gagner avec nos coupons gratuits  \n \n✅✅Gagnez 100% de vos paris avec nos coupons gratuits !!!")

   
    elif message.text== "CANAL OFFICIEL⚜️":
        # Sending a greeting message that includes the reply keyboard 
        await message.reply_photo(photo=img,caption="Vous devez obligatoirement rejoindre notre canal officiel !!!", reply_markup=keyboard_inline)
   
    elif message.text== "GAGNEZ 1000 FCFA💰":
       # Créer un clavier avec les deux boutons
        keyboard_reply5 = types.ReplyKeyboardMarkup(
          resize_keyboard=False, one_time_keyboard=False).add("Soldes 💰", "Retirer 🏧")
        # Envoyer un message avec le clavier
        await message.answer(f"Vous avez la possibilité de gagner 100 000 fcfa en invitant plus de monde à rejoindre le bot\n \
 \
Voici votre lien de parrainage(Prennez-en grand soin):\n\n\
{getInfo('lien')}?start={message.from_user.id}\n\n\
 \
Vous avez {recuperer_nbPersonnne(message.from_user.id)} membres dans votre équipe\n\n\
 \
Pour chaque personne invitée vous recevrez 1000 fcfa\n\n\
 \
Dès que vous atteignez 100 000 FCFA, \
 \
Cliquez sur:\n\
récupérer le cheick✅",reply_markup=keyboard_reply5)
    elif message.text=="1XBET 🟦📱":
        await message.answer_photo(photo=x1,caption=f"Cette option est disponible uniquement pour ceux qui veulent créer un nouveau compte **1XBET** \n \n\n➡️Donc veuillez créer un nouveau compte en utilisant le code promo ** {getInfo('code2')} OU {getInfo('code')} ** \n \n\n➡️Ensuite, faites une capture d’écran et envoyez-là ici \n \n🔴NB: toute personne envoyant de fausses captures d'écrans sera immédiatement expulsée du bot !!! \n \nEnvoyez la capture d’écran ici 👇")
    elif message.text=="BETWINNER 🟩📱":
        await message.answer_photo(photo=bw,caption=f"Cette option est disponible uniquement pour ceux qui veulent créer un nouveau compte **BETWINNER** \n \n\n➡️Donc veuillez créer un nouveau compte en utilisant le code promo ** {getInfo('code2')} OU {getInfo('code')} ** \n \n\n➡️Ensuite, faites une capture d’écran et envoyez-là ici \n \n🔴NB: toute personne envoyant de fausses captures d'écrans sera immédiatement expulsée du bot !!! \n \nEnvoyez la capture d’écran ici 👇")
    elif message.text=="MELBET 🎲":
        await message.answer_photo(photo=mb,caption=f"Cette option est disponible uniquement pour ceux qui veulent créer un nouveau compte **MELBET** \n \n\n➡️Donc veuillez créer un nouveau compte en utilisant le code promo ** {getInfo('code2')} OU {getInfo('code')} ** \n \n\n➡️Ensuite, faites une capture d’écran et envoyez-là ici \n \n🔴NB: toute personne envoyant de fausses captures d'écrans sera immédiatement expulsée du bot !!! \n \nEnvoyez la capture d’écran ici 👇")
    elif message.text=="MEGAPARI 🟩📱":
        await message.answer_photo(photo=mpr,caption=f"Cette option est disponible uniquement pour ceux qui veulent créer un nouveau compte **MEGAPARI** \n \n\n➡️Donc veuillez créer un nouveau compte en utilisant le code promo ** {getInfo('code2')} OU {getInfo('code')} ** \n \n\n➡️Ensuite, faites une capture d’écran et envoyez-là ici \n \n🔴NB: toute personne envoyant de fausses captures d'écrans sera immédiatement expulsée du bot !!! \n \nEnvoyez la capture d’écran ici 👇")
    elif message.text=="LINEBET 🎲":
        await message.answer_photo(photo=lb,caption=f"Cette option est disponible uniquement pour ceux qui veulent créer un nouveau compte **LINEBET** \n \n\n➡️Donc veuillez créer un nouveau compte en utilisant le code promo ** {getInfo('code2')} OU {getInfo('code')} ** \n \n\n➡️Ensuite, faites une capture d’écran et envoyez-là ici \n \n🔴NB: toute personne envoyant de fausses captures d'écrans sera immédiatement expulsée du bot !!! \n \nEnvoyez la capture d’écran ici 👇")
    elif message.text=="888STARZ 🟦📱":
        await message.answer_photo(photo=gg,caption=f"Cette option est disponible uniquement pour ceux qui veulent créer un nouveau compte **888STARZ** \n \n\n➡️Donc veuillez créer un nouveau compte en utilisant le code promo ** {getInfo('code2')} OU {getInfo('code')} ** \n \n\n➡️Ensuite, faites une capture d’écran et envoyez-là ici \n \n🔴NB: toute personne envoyant de fausses captures d'écrans sera immédiatement expulsée du bot !!! \n \nEnvoyez la capture d’écran ici 👇")
    
    elif message.text=="menu":
        await message.answer("Que pouvons-nous faire pour vous ? (Choisissez l'une des options du menu)", reply_markup=keyboard_reply1) 
    elif message.text=="Retour Menu 📋":
        await message.answer("Que pouvons-nous faire pour vous ? (Choisissez l'une des options du menu)", reply_markup=keyboard_reply1) 
    elif message.text=="C'est fait ✅": 
          # Créer un clavier avec les trois boutons et les emoji
        keyboard_reply4 = types.ReplyKeyboardMarkup(
        resize_keyboard=False, one_time_keyboard=False).add("Trouver la bonne case 🔍", "Retour Menu 📋")
  # Envoyer un message avec le clavier
        await message.answer_photo(photo=swamp,caption=f"À fin de recevoir les meilleures prédictions sur 'SWAMP LAND', vous devez être  obligatoirement inscrit avec le code promo : {getInfo('code')} OU {getInfo('code2')}  \
           \
si c \'est fait ✅ , \
cliquez sur 'Trouver la bonne case' pour commencer les prédictions \
 \
👇👇👇👇👇👇", reply_markup=keyboard_reply4)
    elif message.text=="Trouver la bonne case 🔍": 
        await message.answer(f"Veuilliez choisir la case {random.randint(1,5)}") 
    elif message.text=="Soldes 💰": 
        await message.reply(f"👋 Cher {message.from_user.full_name} \
\n➡️Votre solde est de {recuperer_nbPersonnne(message.from_user.id)*1000} FCFA💰\n\n\
\n➡️Vous avez invité au total {recuperer_nbPersonnne(message.from_user.id)} membres dans votre équipe👥\n \
 \
\n➡️Voici votre lien de parrainage (Prennez-en soin) \n\n\
{getInfo('lien')}?start={message.from_user.id}\n\n\
\n➡️Gagner 1000 FCFA pour chaque personne invitée\n\nRetrait minimum 30000 FCFA") 
    elif message.text=="Retirer 🏧": 
          await message.reply(f"👋 Cher {message.from_user.full_name} \
\n➡️Votre solde est de {recuperer_nbPersonnne(message.from_user.id)*1000} FCFA💰\n\n\
\n➡️Vous avez invité au total {recuperer_nbPersonnne(message.from_user.id)} membres dans votre équipe👥\n \
\n➡️Voici votre lien de parrainage \n \
{getInfo('lien')}?start={message.from_user.id}\n \
\n➡️Gagner 1000 FCFA pour chaque personne invitée\n \
Retrait minimum : 30000 FCFA")
    elif message.text.startswith("code:") or message.text.startswith("canal:") or message.text.startswith("code2:"):
      mettreInfo(message.text) 
      await message.reply(f"Nous avons changé l'information  '{message.text}'") 

      
    
          
    

@dp.message_handler(content_types=types.ContentType.PHOTO) 
async def check_Photo(message: types.Message): 
    
    if message.caption.__contains__("🔥🔥"): 
        # Responding with a message that includes the text of the user's message 
        liste=recuperer_id()
        messageDeroupe=message.caption[8::1]
        print(messageDeroupe)
        message.caption=messageDeroupe
        
        for id in liste :
          await bot.forward_message(chat_id=id, message_id=message.message_id,from_chat_id= message.chat.id)
    elif message.photo:
        await message.reply("Merci ! Votre image sera envoyee à l'administrateur")
        #await bot.forward_message(chat_id=recuperer_idPersonnne("Gates Tem"), message_id=message.message_id,from_chat_id= message.chat.id)
        


# Starting the bot 
executor.start_polling(dp)

executor.start_polling(dp)

