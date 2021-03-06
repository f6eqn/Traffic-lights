# Traffic_lights:
-----------------

Exercice de programmation: Feux tricolores de signalisation routière.

Historique:
-----------

Cet exercice est un standard de l'apprentissage de la programmation.
J'en ai eu une première exéprience en 1982 lors d'une première découverte de la programmation en language Graphset.
J'ai repris le sujet lors d'un enseignement prodigué à des classes de première S et STI2D au lycée
Marcel Rudloff à Strasbourg en 2017 où j'exerçais comme professeur en sciences de l'ingénieur (SII).
L'objectif était d'initier les élèves à la programmation en langage C++ avec une plateforme Arduino Uno.

Cahier des charges:
-------------------

Le cahier des charges est donné par le document pdf : TP Shibuya Traffic Lights.docx

Ce TP fait suite à un premier module sur l'Arduino, où les élèves ont appréhendé le matériel et l'IDE.
Il convient de respecter les étapes car elles permettent une progression dans la difficulté et permettent
d'orienter vers des solutions "structurées" (utilisation de boucles, de sous-programmes, recherches en tables, etc.)
plutôt que purement séquentielles.

Objectifs de progrès:
---------------------

1 - Appréhender le langage Micro Python et la carte Rasperry Pico sur un exemple suffisamment complexe.

2 - Identifier les spécificités versus Arduino/C++ pour la mise en oeuvre de structures.

3 - Assimiler la configuration du hardware (pin out, GPIO) et les particularités de gestions des interruptions.

4 - Utiliser les types de variables (listes, dictionnaires) et les branchements spécifiques à Python/Micro Python.

5 - Limiter les recours aux structures de test ("Don't ask, Do!")

Bilan:
------

1 - Le projet a été mené à bout et les solutions techniques sont fonctionnelles de manière identiques sur les
    deux plates formes.

2 - Les spécificités suivantes ont été identifiées:
	- boucle itérative "for" avec utilisation de liste (for in range) ou substitution avec une boucle while.
	- branchement conditionnel en adressage indirect (recherche en table) en remplacement d'un switch/case
	- transmission des données globales/locales au sein des fonctions.
	- gestion des interruptions du module "machine"

3 - Les difficultés rencontrées ont été les suivantes:
	- faible disponibilité de documentation en français sur le Net.
	- les exemples, manuels ou tutoriels sont soit trop simples soit faisant appel à des plates formes différentes.
	- la définition des sous-programmes (routines, fonctions) et l'usage de variables globales/locales est difficile
	  du fait de la trop grande simplicité du Python dans ce domaine (absence de définition des types de variables)
	  et de la particularité du Micro Python (utilisation du "return"?)
	- faible documentation du machine.Pin.IRQ et parametrage de sa routine call_back.

Points forts:
-------------

L'étude a grandement été facilitée par l'ouvrage "Get started with Micro Python on Raspberry Pi Pico" de l'organisation
Raspberry Pi (voir document Rpi_Pipico_Digital_v10.pdf). La progression est très pédagogique et particulièrement bien
illustrée et documentée. Dommage que le document ne soit disponible qu'en anglais. Ce document devrait constituer
un précieux bréviaire (après traduction) pour la formation de débutants dans un Fablab ou dans l'enseignement.

Facilité d'utilisation de l'environnement de programmation (IDE) Thommy sur Raspberry Pi4 (Linux).La mise en oeuvre depuis
un système d'exploitation Windows sera un excellent sujet pour une prochaine étude.
