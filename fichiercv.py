import streamlit as st
import pandas as pd
from streamlit_player import st_player

st.markdown("<h1 style='text-align: center; color: #3283FE;'>PIVETEAU Marc</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: Black;font-size: 30px;'>Recherche une entreprise pour une alternance en Data Scientist ou un poste de Data Analyst</h1>", unsafe_allow_html=True)

st_player('https://youtu.be/D5jS14ZvPOE')

st.markdown("<h1 style='text-align: center; color: #3283FE;font-size: 20px;'>Hard skills - Soft skills</h1>", unsafe_allow_html=True)
recherche = st.selectbox("Que souhaitez vous voir ?",['Choisi entre hard skill et soft skill :','Hard skills', 'Soft skills'])

#https://share.streamlit.io/marcpiveteau/cv/main/fichiercv.py	
if recherche =='Hard skills':
	st.write('pour voir le détail clique sur le bouton')
	if(st.button('Collecte de données')):
		st.markdown('**Mysql**')
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/CV/main/t%C3%A9l%C3%A9chargement.jpg)")
	if(st.button('Traitement de données')):
		lienpandas = "[exemple d'un traitement de données d'un dataframe](https://colab.research.google.com/drive/1g66yTOzycusv1P5QLHkW2Z0JE9MfgaEM?usp=sharing)"
		st.markdown(lienpandas, unsafe_allow_html=True)
		st.markdown('**Python, Pandas, Numpy, Excel, power bi query, google sheet**')
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/CV/main/pythonexc.jpg)")
	if(st.button('Dashboard et Dataviz')):
		lienpowerbi = "[exemple d'un dashboard sur Power BI ](https://app.powerbi.com/view?r=eyJrIjoiN2NjM2ZmNjQtMmYzZi00MDA1LWFmYTUtNTBhMTY2MjEzYjg5IiwidCI6IjE0NTJmNzE3LTQ5MTItNDE1Yi1hZjg1LWQ3Njc5YWM0MWQwNiJ9)"
		st.markdown(lienpowerbi, unsafe_allow_html=True)
		#<iframe width="600" height="373.5" src="https://app.powerbi.com/view?r=eyJrIjoiN2NjM2ZmNjQtMmYzZi00MDA1LWFmYTUtNTBhMTY2MjEzYjg5IiwidCI6IjE0NTJmNzE3LTQ5MTItNDE1Yi1hZjg1LWQ3Njc5YWM0MWQwNiJ9" frameborder="0" allowFullScreen="true"></iframe>
		st.markdown('**Tableau software, Power BI, excel, streamlit**')
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/CV/main/dataviz.jpg)")
	if(st.button('Machine learning')):
		st.markdown('**Scikit learn, nltk**')
		lienexosklearn= "[exemple d'un exercice que j'ai fait pour utiliser de sklearn et nltk](https://colab.research.google.com/drive/14QOW9JIGGg7t_-7RAwX_NmTNmLU35_vJ?usp=sharing)"
		st.markdown(lienexosklearn, unsafe_allow_html=True)
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/CV/main/scikit%20learn.jpg)")
	if(st.button('Méthode Agile')):
		st.markdown('**scrum**')
		st_player('https://www.youtube.com/watch?v=anZcEIQlpoY&t=331s')

if recherche =='Soft skills':
	if(st.button('adaptabilité')):
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/CV/main/adaptabilit%C3%A93.jpg)")
	if(st.button("Esprit d'équipe")):
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/CV/main/esprit%20d'%C3%A9quipe.jpg)")
	if(st.button('Créativité')):
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/CV/main/creativite-personnel-2.jpg)")
	if(st.button("Ouverture d'esprit")):
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/CV/main/ouverture%20d'esprit.jpg)")
	if(st.button('Fiabilité')):
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/CV/main/fiabilit%C3%A92.jpg)")
	if(st.button('Intégrité')):
		st.markdown("![Alt Text](https://raw.githubusercontent.com/marcpiveteau/CV/main/integrit%C3%A92.jpg)")

st.write('----'*20)

st.markdown("<h1 style='text-align: center; color: #3283FE;font-size: 20px;'>Formation</h1>", unsafe_allow_html=True)
recherche2 = st.selectbox("Que souhaitez vous voir dans mon parcourt de formation ?",['Choisissez entre les différentes formation :','Wild Code School (2021-2022)','Université de grenoble (2006)', 'Institution saint joseph (2005)'])

if recherche2 =='Wild Code School (2021-2022)':
	st.markdown("<h1 style='text-align: center; color: Black;font-size: 20px;'>Formation présentielle de Data Analyst</h1>", unsafe_allow_html=True)
	lien= '[wild Code School](https://www.wildcodeschool.com/fr-FR)'
	st.markdown(lien, unsafe_allow_html=True)
	st.markdown("<h1 style='text-align: center; color: Black;font-size: 15px;'>Bougez le curseur pour voir les compétences développées :</h1>", unsafe_allow_html=True)
	recherchewild = st.select_slider('le curseur :',options=['1/Collecter la donnée','2/ Traiter la donnée', '3/ Modéliser et présenter la donnée'])
	if recherchewild == '1/Collecter la donnée':
		st.write('Effectuer une requête sur une base dedonnées avec SQL et API REST')
		st.write('Automatiser la collecte de contenu surdes pages web  avec scraping HTML')
		st.write('Interpréter le format JSON et effectuer du géocodage')
		st.write('Comprendre les enjeux du RGPD')
	if recherchewild == '2/ Traiter la donnée':
		st.write("Utiliser l'algorithmie en Python et la programmation orientée objet")
		st.write("Utiliser les matrices NumPy et les DataFrames Pandas")
		st.write('Retraiter les outliers et les valeurs manquantes')
		st.write('Rendre son code propre "clean code"')
	if recherchewild == '3/ Modéliser et présenter la donnée':
		st.write("Comprendre le Machine Learning : scikit learn, classification et regression")
		st.write("Traiter automatiquement le langage NLP")
		st.write('Utiliser les plateformes de data science(KNIME) et de Big Data')
		st.write('Manipuler la #Dataviz interactive et dynamique (Plotly et Bokeh)')
		st.write('Réaliser des dashboards et de la cartographie PowerBI et Tableau ')
	st.markdown("<h1 style='text-align: center; color: Black;font-size: 20px;'>Projets réalisés et hackathon</h1>", unsafe_allow_html=True)
	st.markdown("<h1 style='text-align: center; color: Black;font-size: 15px;'>Bougez le curseur pour voir les différents projets :</h1>", unsafe_allow_html=True)
	recherchewild2 = st.select_slider("le curseur projets et hackatton:",options=['projet 1','projet 2', 'hackathon'])
	if recherchewild2 == 'projet 1':
		st.write('Projet 1: analyse de donnée et présentation Dashboard : My SQL, Tableau software ')
		st.write('le dashboard a été réalisé sur tableau software, il était interactif mais pour le partager un power point a été fait')
		lienprojet1= '[lien power point pour projet 1 ](https://1drv.ms/p/s!AnPXp85bWZSV3T0f594tbOBm7gzv?e=nWVYMS)'
		st.markdown(lienprojet1, unsafe_allow_html=True)
	if recherchewild2 == 'projet 2':
		st.write("Projet 2: nettoyage, analyse et système de recommandation à partir d'un Dataframe de films : Pandas, Python, Seaborn, Power BI et Streamlit")
		lienprojet2= '[projet 2 les graphiques](https://share.streamlit.io/marcpiveteau/projet2/main/statnanflix.py)'
		st.markdown(lienprojet2, unsafe_allow_html=True)
		lienprojet3= '[projet 2 de recommandation](https://share.streamlit.io/marcpiveteau/projetreco/main/recomandation.py)'
		st.markdown(lienprojet3, unsafe_allow_html=True)
	if recherchewild2 == 'hackathon':
		st.write("hackathon: création d'une API sur le theme de la musique : Pandas, Python, sklearn, Plotly et Streamlit")
if recherche2 =='Université de grenoble (2006)':
	st.markdown("<h1 style='text-align: center; color: Black;font-size: 20px;'>licence en gestion et commerce des produits de la filière forestière</h1>", unsafe_allow_html=True)
	st.markdown('**Memoire :**')
	st.write("Analyse des demandes des clients et tendances sur les nouveau produits bois.")
	st.write("Référencement, mise en place du stock, formation et accompagnement des commerciaux")

if recherche2 =='Institution saint joseph (2005)':
	st.markdown("<h1 style='text-align: center; color: Black;font-size: 20px;'>BTS en gestion forestière</h1>", unsafe_allow_html=True)
	st.markdown('**rapport de stage:**')
	st.write("récolte, traitement et analyse de données sur les conséquences d'une gestion en futaie irrégulière sur le peuplement, flore et sol: Excel et stat box")

st.write('----'*20)
st.markdown("<h1 style='text-align: center; color: #3283FE;font-size: 20px;'>Experience</h1>", unsafe_allow_html=True)
recherche3 = st.selectbox("Que souhaitez vous voir dans mon experience professionnel ?",['Choisissez suivant les différents experience :' ,'Independant immobilier chez proprietes-privees.com (2017 -2021)','Commercial chez Reseau pro (2010 -2017)', 'vendeur interne chez Saint gobain (2006-2010)'])
if recherche3 =='Independant immobilier chez proprietes-privees.com (2017 -2021)':
	st.markdown("<h1 style='text-align: center; color: Black;font-size: 20px;'>Independant en immobilier</h1>", unsafe_allow_html=True)
	lienpp = '[ma page propriétés-privées.com](https://www.proprietes-privees.com/negociateur/marc.piveteau)'
	st.markdown(lienpp, unsafe_allow_html=True)
	st.markdown('**mes missions :**')
	st.write("Prospection, Estimation, relation client, accompagnement client")
	st.write("Rédaction compromis de vente et de bail de location, constitution et suivit des dossiers")
	st.write("Gestion courante de l'entreprise (déclaration chiffre, TVA, assurance, ...)")
	st.write("Veille du marché et analyse continuelle du marché pour suivre l'évolution.")
if recherche3 =='Commercial chez Reseau pro (2010 -2017)':
	st.markdown("<h1 style='text-align: center; color: Black;font-size: 20px;'>Commercial</h1>", unsafe_allow_html=True)
	st.markdown('**mes missions :**')
	st.write("redressement et suivit de différents portefeuille client")
	st.write("mise en place de tarification suivant le marché et les clients, prise des commandes, recommandation et prescription technique")
if recherche3 =='vendeur interne chez Saint gobain (2006-2010)':
	st.markdown("<h1 style='text-align: center; color: Black;font-size: 20px;'>Vendeur interne</h1>", unsafe_allow_html=True)
	st.markdown('**mes missions :**')
	st.write("accueil client, chiffrage, vente, gestion des livraisons et suivit de la comptabilité")
	
st.write('----'*20)
st.markdown("<h1 style='text-align: center; color: #3283FE;font-size: 20px;'>Les plus</h1>", unsafe_allow_html=True)
recherche4 = st.selectbox("Les Plus ( langue, benevolat, loisirs)",['Choisissez le point qui vous interresse :','Langue', 'bénévolat', 'loisirs'])
if recherche4 =='Langue':
	st.write("anglais niveau intermediaire :")
	st.write("Dans ce monde de la data les cours et les infos des outils que j'utilise sont en anglais et je les comprends très bien")
	st.write("Pour l'oral j'arrive a me faire comprendre, certains daily sont en anglais")
if recherche4 =='bénévolat':
	st.markdown("<h1 style='text-align: center; color: Black;font-size: 20px;'>bureau du basket</h1>", unsafe_allow_html=True)
	st.write("Responsable de l'organisation des tournois interne et externe pour l'ensemble des licenciés et coordinations avec les autres Bénévoles")
	st.markdown("<h1 style='text-align: center; color: Black;font-size: 20px;'>comité de parent</h1>", unsafe_allow_html=True)
	st.write("responsable de l'organisation de la journée lucrative (randonnée, chasse aux trésors,...)")
if recherche4 =='loisirs':
	st.write("Le basket en tant que joueur et coach d'une équipe de jeune")
	st.write("La nature")
	st.write("Les voyages (Bénin,Les Canaris, Portugal, Irlande,...")

st.write('----'*20)
st.markdown("<h1 style='text-align: center; color: #3283FE;font-size: 20px;'>me contacter</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: black;font-size: 15px;'>marc.piveteau@hotmail.fr</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: black;font-size: 15px;'>06-74-36-45-38</h1>", unsafe_allow_html=True)

lien= '[wild Code School](https://www.wildcodeschool.com/fr-FR)'
	
lienlinkedin = '[linkedin](https://www.linkedin.com/in/marc-piveteau-63a4b0130/)'
st.markdown(lienlinkedin, unsafe_allow_html=True)
liengit = '[Github](https://github.com/marcpiveteau)'
st.markdown(liengit, unsafe_allow_html=True)
