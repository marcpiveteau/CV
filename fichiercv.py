import streamlit as st
import pandas as pd
from streamlit_player import st_player

st.markdown("<h1 style='text-align: center; color: #3283FE;'>Marc PIVETEAU</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: Black;font-size: 30px;'>Disponible pour un poste dans la Data</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: Black;font-size: 24px;'>Alternance Data Scientist / CDI Data Analyst</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: Black;font-size: 20px;'>A partir de février 2022</h1>", unsafe_allow_html=True)

st_player('https://youtu.be/D5jS14ZvPOE')

st.markdown("<h1 style='text-align: center; color: #3283FE;font-size: 20px;'>Hard skills - Soft skills</h1>", unsafe_allow_html=True)
recherche = st.selectbox("Découvrez mes hard skills et soft skills",['Choisissez une compétence :','Hard skills', 'Soft skills'])

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
recherche2 = st.selectbox("Découvrez mon parcours de formation ?",['Choisissez une formation :','Wild Code School (2021-2022) : Formation Data Analyst','Université de Grenoble (2006) : Licence en gestion et commerce de bois', 'Institution Saint Joseph (2005) : BTS Gestion Forestière'])

if recherche2 =='Wild Code School (2021-2022) : Formation Data Analyst':
	st.markdown("<h1 style='text-align: center; color: Black;font-size: 20px;'>Formation présentielle de Data Analyst</h1>", unsafe_allow_html=True)
	lien= '[Wild Code School](https://www.wildcodeschool.com/fr-FR)'
	st.markdown(lien, unsafe_allow_html=True)
	st.markdown("<h1 style='text-align: center; color: Black;font-size: 15px;'>Bougez le curseur pour voir les compétences développées :</h1>", unsafe_allow_html=True)
	recherchewild = st.select_slider('Le curseur :',options=['1/Collecter la donnée','2/ Traiter la donnée', '3/ Modéliser et présenter la donnée'])
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
	st.markdown("<h1 style='text-align: center; color: Black;font-size: 20px;'>Cochez pour voir les projets réalisés et hackathon</h1>", unsafe_allow_html=True)
	projet1 = st.checkbox("Projet 1 : Aide à la prise de décision pour une entreprise")
	if projet1:
		st.write("Etapes : Analyse de données , KPI et Dashboard ")
		st.write('Outils utilisés : MySQL, Tableau software ')
		lienprojet1= '[Cliquez ici pour voir le projet ](https://1drv.ms/p/s!AnPXp85bWZSV3T0f594tbOBm7gzv?e=nWVYMS)'
		st.markdown(lienprojet1, unsafe_allow_html=True)
	projet2 = st.checkbox("Projet 2 : Création d'un système de recommandation de film")
	if projet2:
		st.write("Etapes : Nettoyage et analyse des données / Machine learning")
		st.write("Outils utilisés : Pandas, Python, Seaborn, sklearn, Power BI et Streamlit")
		lienprojet2= '[Cliquez ici pour voir les graphiques](https://share.streamlit.io/marcpiveteau/projet2/main/statnanflix.py)'
		st.markdown(lienprojet2, unsafe_allow_html=True)
		lienprojet3= '[Cliquez ici pour utiliser le système de recommandation](https://share.streamlit.io/marcpiveteau/projetreco/main/recomandation.py)'
		st.markdown(lienprojet3, unsafe_allow_html=True)
	hackathon = st.checkbox("Hackathon : création d'une API de recommandation de musique")
	if hackathon:
		st.write("Etapes : Nettoyage et analyse des données / Machine learning / interface interactive")
		st.write("Outils utilisés : Pandas, Python, sklearn, Plotly et Streamlit")
if recherche2 =='Université de Grenoble (2006) : Licence en gestion et commerce de bois':
	st.markdown("<h1 style='text-align: center; color: Black;font-size: 20px;'>licence en gestion et commerce des produits de la filière forestière</h1>", unsafe_allow_html=True)
	st.markdown('**Memoire :**')
	st.write("Analyse des demandes des clients et tendances sur les nouveau produits bois.")
	st.write("Référencement, mise en place du stock, formation et accompagnement des commerciaux")

if recherche2 =='Institution Saint Joseph (2005) : BTS Gestion Forestière':
	st.markdown("<h1 style='text-align: center; color: Black;font-size: 20px;'>BTS en gestion forestière</h1>", unsafe_allow_html=True)
	st.markdown('**rapport de stage:**')
	st.write("récolte, traitement et analyse de données sur les conséquences d'une gestion en futaie irrégulière sur le peuplement, flore et sol: Excel et stat box")

st.write('----'*20)
st.markdown("<h1 style='text-align: center; color: #3283FE;font-size: 20px;'>Experiences professionnelles</h1>", unsafe_allow_html=True)
recherche3 = st.selectbox("Découvrez mes expériences professionnelles :",['Choisissez une expérience :' ,'Independant immobilier chez proprietes-privees.com (2017 -2021)','Commercial chez Reseau pro (2010 -2017)', 'Vendeur interne chez Saint Gobain (2006-2010)'])
if recherche3 =='Independant immobilier chez proprietes-privees.com (2017 -2021)':
	st.markdown("<h1 style='text-align: center; color: Black;font-size: 20px;'>Independant en immobilier</h1>", unsafe_allow_html=True)
	lienpp = '[Mon site professionnel](https://www.proprietes-privees.com/negociateur/marc.piveteau)'
	st.markdown(lienpp, unsafe_allow_html=True)
	st.markdown('**Mes missions :**')
	st.write("- Prospection, estimation, relation client, accompagnement client")
	st.write("- Rédaction compromis de vente et de bail de location, constitution et suivi des dossiers")
	st.write("- Gestion courante de l'entreprise (déclaration du CA, TVA, assurance ...)")
	st.write("- Veille et analyse du marché pour suivre son évolution.")
if recherche3 =='Commercial chez Reseau pro (2010 -2017)':
	st.markdown("<h1 style='text-align: center; color: Black;font-size: 20px;'>Commercial</h1>", unsafe_allow_html=True)
	st.markdown('**Mes missions :**')
	st.write("- Redressement et suivi de portefeuilles client")
	st.write("- Définition de la tarification client, prise de commandes, recommandation et prescription technique")
if recherche3 =='Vendeur interne chez Saint Gobain (2006-2010)':
	st.markdown("<h1 style='text-align: center; color: Black;font-size: 20px;'>Vendeur interne</h1>", unsafe_allow_html=True)
	st.markdown('**Mes missions :**')
	st.write("Accueil client, chiffrage, vente, gestion des livraisons et suivi de la comptabilité")
	
st.write('----'*20)
st.markdown("<h1 style='text-align: center; color: #3283FE;font-size: 20px;'>Les plus</h1>", unsafe_allow_html=True)
recherche4 = st.selectbox(" Langues, bénévolat, loisirs",['Langues', 'Bénévolat', 'Loisirs'])
if recherche4 =='Langues':
	st.write("Anglais niveau intermediaire")
if recherche4 =='Bénévolat':
	st.markdown("<h1 style='text-align: center; color: Black;font-size: 20px;'>Bureau du basket</h1>", unsafe_allow_html=True)
	st.write("Responsable de l'organisation des tournois internes et externes pour l'ensemble des licenciés et coordination avec les bénévoles")
	st.markdown("<h1 style='text-align: center; color: Black;font-size: 20px;'>Comité de parents</h1>", unsafe_allow_html=True)
	st.write("Responsable de l'organisation de la journée lucrative (randonnée, chasse aux trésors...)")
if recherche4 =='Loisirs':
	st.write("Le basket en tant que joueur et coach d'une équipe de jeunes")
	st.write("La nature et la forêt")
	st.write("Les voyages (Bénin, Les Canaries, Portugal, Irlande)")

st.write('----'*20)

st.markdown("<h1 style='text-align: center; color: Black;font-size: 15px;'>Programme de l'alternance</h1>", unsafe_allow_html=True)
lienalternance= "[cliquez pour voir le programme de la formation en alternance ](https://www.wildcodeschool.com/fr-FR/formations/formation-data-scientist/remote-francais)"
st.markdown(lienalternance, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #3283FE;font-size: 20px;'>Contactez-moi</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: black;font-size: 15px;'>marcpiveteau@hotmail.fr</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: black;font-size: 15px;'>06-74-36-45-38</h1>", unsafe_allow_html=True)

lien= '[wild Code School](https://www.wildcodeschool.com/fr-FR)'
	
lienlinkedin = '[Linkedin](https://www.linkedin.com/in/marc-piveteau-63a4b0130/)'
st.markdown(lienlinkedin, unsafe_allow_html=True)
liengit = '[Github](https://github.com/marcpiveteau)'
st.markdown(liengit, unsafe_allow_html=True)

