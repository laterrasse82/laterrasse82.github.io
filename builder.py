#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import carte

#######################################################################
# fonctions ###########################################################
#######################################################################
def headerhtml(titre_page):
    entete = """
<!DOCTYPE html><html lang="en">
 <head>
   <meta charset="utf-8" />
   <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
   <meta name="description" content="" />
   <meta name="author" content="" />
   <title>La Terrasse - """
    entete += titre_page
    entete += """
   </title>
   <link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
   <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.5.0/font/bootstrap-icons.css" rel="stylesheet" type="text/css" />
   <link href="https://fonts.googleapis.com/css?family=Lato:300,400,700,300italic,400italic,700italic" rel="stylesheet" type="text/css" />
   <link href="css/styles.css" rel="stylesheet" />
 </head>
 <body>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark static-top">
   <div class="container">
	<a href="index.html"><img src="assets/img/logo.svg" alt="" width="50" height="50"></a>
    <a class="navbar-brand" href="index.html">La Terrasse</a>
                <button class="navbar-toggler navbar-toggler-right text-white" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                    Menu
                    <i class="fas fa-bars"></i>
                </button>
                <div class="collapse navbar-collapse" id="navbarResponsive">
                    <ul class="navbar-nav ms-auto">
                        <li class="nav-item"><a class="nav-link" href="boissons.html">Boissons</a></li>
			            <li class="nav-item"><a class="nav-link" href="restauration.html">Restauration</a></li>
                        <li class="nav-item"><a class="nav-link" href="acces.html">Acc??s</a></li>
                        <li class="nav-item"><a class="nav-link" href="contact.html">Contact</a></li>
			            <li class="nav-item"><a class="nav-link" href="remerciements.html">Remerciements</a></li>
                    </ul>
                </div>
            </div>
        </nav>"""
    return entete

#######################################################################
footerhtml = """        <!-- Footer-->
        <footer class="footer bg-dark text-white">
            <div class="container">
                <div class="row">
                    
                    <div class="text-center">
                        <ul class="list-inline">
                            <li class="list-inline-item me-4">
                                <a href="#!"><i class="bi-facebook fs-1" style="color: #b7975a;"></i></a>
                            </li>
                            <li class="list-inline-item">
                                <a href="#!"><i class="bi-instagram fs-1" style="color: #b7975a;"></i></a>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </footer>
        <!-- Bootstrap core JS-->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
        <!-- Core theme JS-->
        <script src="js/scripts.js"></script>
        <!-- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *-->
        <!-- * *                               SB Forms JS                               * *-->
        <!-- * * Activate your form at https://startbootstrap.com/solution/contact-forms * *-->
        <!-- * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *-->
        <script src="https://cdn.startbootstrap.com/sb-forms-latest.js"></script>
    </body>
</html>
"""

#######################################################################
def titre(texte):
    reponse = """<section class="py-5 bg-dark">
            <div class="container mt-5 my-5 bg-dark text-white">
                <div class="row justify-content-center">
                    <div class="col-lg-6">
                        <h1>""" + texte + """</h1>
                    </div>
                </div>
            </div>
        </section>
        """
    return reponse

#######################################################################
showcase_debut = """<section class="showcase bg-dark text-white" >
            <div class="container-fluid p-0">"""

def showcase_im_droite(url_img, titre, texte):
    reponse = """<div class="row g-0">
                    <div class="col-lg-6 order-lg-2 text-white showcase-img" style="background-image: url('""" + url_img + """')"></div>
                    <div class="col-lg-6 order-lg-1 my-auto showcase-text">
                        <h2>""" + titre + """</h2>
                        <p class="lead mb-0">""" + texte + """</p>
                    </div>
                </div>
        """
    return reponse

def showcase_im_gauche(url_img, titre, texte):
    reponse = """<div class="row g-0">
                    <div class="col-lg-6 text-white showcase-img" style="background-image: url('""" + url_img + """')"></div>
                    <div class="col-lg-6 my-auto showcase-text">
                        <h2>""" + titre + """</h2>
                        <p class="lead mb-0">""" + texte + """</p>
                    </div>
                </div>
        """
    return reponse

showcase_fin = "</div></section>"

#######################################################################
def logo(url_logo):
    reponse = """<header class="masthead">
            <div class="container position-relative">
                <div class="row justify-content-center">
                    <div class="col-xl-6">
						<img class="img-fluid" src="###-!-###" >
                        <div class="text-center text-white">
                        </div>
                    </div>
                </div>
            </div>
        </header>
        """.replace("###-!-###", url_logo)
    return reponse

#######################################################################
googlemap = """<div class="map-responsive"><iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d10234.235289095723!2d1.3354825258171867!3d43.96174252913296!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x12ac0f7d2c589d6f%3A0x4e2308b2987e614d!2sSkatepark%20Bressols!5e0!3m2!1sfr!2sfr!4v1644418258139!5m2!1sfr!2sfr" width="100pc" height="450" style="border:0;" allowfullscreen="" loading="lazy"></iframe></div>"""
osmacces = """
<section class="py-1 bg-dark">
    <div class="container my-1 bg-dark text-white">
        <div class="row justify-content-center">
            <div class="col-lg-9">
            <div class="map-responsive">
            
<iframe src="https://umap.openstreetmap.fr/fr/map/acces-la-terrasse_721036?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false" width="200" height="800" style="border:0;" allowfullscreen="" loading="lazy"></iframe>

</div></div></div></div></section>"""

osmlocalisation = """
<section class="py-1 bg-dark">
    <div class="container my-1 bg-dark text-white">
        <div class="row justify-content-center">
            <div class="col-lg-9">
            <div class="map-responsive">
            
<iframe src="https://umap.openstreetmap.fr/fr/map/la-terrasse-82_721008?scaleControl=false&miniMap=false&scrollWheelZoom=false&zoomControl=true&allowEdit=false&moreControl=true&searchControl=null&tilelayersControl=null&embedControl=null&datalayersControl=true&onLoadPanel=undefined&captionBar=false" width="200" height="800" style="border:0;" allowfullscreen="" loading="lazy"></iframe>

</div></div></div></div></section>"""


#######################################################################
def banniere(titre, texte):
    reponse = """
<section class="py-1 bg-dark">
    <div class="container mt-5 my-1 bg-dark text-white">
        <div class="row justify-content-center">
            <div class="col-lg-6">
                <h2>""" + titre + """</h2>
                <p class="lead">""" + texte + """
                </p>
            </div>
        </div>
    </div>
</section>
"""
    return reponse

#######################################################################
def carousel(nom, images):
    temp = """
<section class="py-1 bg-dark">
    <div class="container my-1 bg-dark text-white">
        <div class="row justify-content-center">
            <div class="col-lg-9">
                <div id="###-nom-###" class="carousel slide" data-bs-ride="carousel">
                <!-- Indicators/dots -->
                    <div class="carousel-indicators">"""
    cpt = 0
    for im in images:
        if cpt == 0:
            temp += """<button type="button" data-bs-target="####-nom-###" data-bs-slide-to="###-nb-###" class="active"></button>""".replace("###-nb-###", str(cpt))
        else:
            temp += """<button type="button" data-bs-target="####-nom-###" data-bs-slide-to="###-nb-###"></button>""".replace("###-nb-###", str(cpt))
        cpt += 1
                        
    temp += """</div>

                <!-- The slideshow/carousel -->
                <div class="carousel-inner bg-dark">"""
    cpt = 0
    for im in images:
        if cpt == 0:
            temp += """<div class="carousel-item active"><img src="###-url-###" class="d-block w-100"></div>""".replace("###-url-###", im)
        else:
            temp += """<div class="carousel-item"><img src="###-url-###" class="d-block w-100"></div>""".replace("###-url-###", im)
        cpt += 1
    
    temp += """</div>
                <!-- Left and right controls/icons -->
                <button class="carousel-control-prev" type="button" data-bs-target="####-nom-###" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon"></span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="####-nom-###" data-bs-slide="next">
                    <span class="carousel-control-next-icon"></span>
                </button>
                </div>
            </div>
        </div>
    </div>
</section>"""
    reponse = temp.replace("###-nom-###", nom)
    return reponse

#######################################################################
# pages ###############################################################
#######################################################################
pages = {}

#######################################################################
# page accueil ########################################################
#######################################################################
pages["index"] = logo("assets/img/logo.png")

pages["index"] += showcase_debut

pages["index"] += showcase_im_droite(url_img = "assets/img/ambiance.jpg",
                                       titre = "L'ambiance",
                                       texte = "La Terrasse vous accueille dans un d??cor naturel et ??l??gant sur les berges du Tarn. Envie de passer un moment en famille, entre amis, en ext??rieur, en buvant un verre en musique autour d???une planche dans un cadre magnifique. </br> Alors rejoignez nous pour une parenth??se dans votre quotidien.")
                                       
pages["index"] += showcase_im_gauche(url_img = "assets/img/boissons.jpg",
                                       titre = "Les boissons",
                                       texte = """<b>Selon votre envie du moment et avec mod??ration, nous vous proposons :</b></br>
<i class="bi bi-play"></i>Pressions et bi??res locales</br>
<i class="bi bi-play"></i>Vin de la r??gion</br>
<i class="bi bi-play"></i>Des planteurs maisons</br>
<i class="bi bi-play"></i>Des boissons sans alcool : coktails de fruits frais, eau aromatis??e, soda...</br>""")

pages["index"] += showcase_im_droite(url_img = "assets/img/restauration.jpg",
                                       titre = "La restauration",
                                       texte = """<b>Boire, c???est sympa, mais manger des produits locaux, c???est pas mal non plus???</br>
Nous vous proposons :</br></b>
<i class="bi bi-play"></i>Planche de charcuterie.</br>
<i class="bi bi-play"></i>Planche de fromage.</br>
<i class="bi bi-play"></i>Planche vegetarienne.</br>
Les planches sont accompagn??es d'un pain sp??cial.""")

pages["index"] += showcase_im_gauche(url_img = "assets/img/activite.jpg",
                                       titre = "Le cadre",
                                       texte = """Envie de vous d??gourdir les jambes, de passer un bon moment ?</br>
la plaine de jeux de Bressols vous permettra de profiter d'un terrain de p??tanque ombrag?? accol?? ?? la Terrasse.</br>
Vous trouverez aussi au sein d'un parc ombrag?? des tables, bancs, 'un skate-park, des terrains de foot et de rugby, d'un parcours de sant??, d'une aire de jeux pour enfants, de spots de p??che, d'une aire de camping car et de sanitaires.""")

#pages["index"] += showcase_im_droite(url_img = "assets/img/emporter.jpg",
#                                       titre = "A emporter",
#                                       texte = """Vous pouvez profiter de nos produits ?? emporter dans une box pique nique, ?? consommer ou vous le souhaitez""")

pages["index"] += showcase_im_droite(url_img = "assets/img/ouverture.jpg",
                                       titre = "Ouverture",
                                       texte = """
La Guinguette sera ouverte jusqu'?? la fin des beaux jours :</br>
Du  Dimanche au mercredi de 9h ?? minuit</br>
Du Jeudi au Samedi 9h ?? 2h</br>
L'ouverture d??pends des conditions m??t??os, suivez les r??seaux sociaux pour en savoir plus...</br>
Des parkings gratuits sont a votre disposition tout autour de la plaine de jeux.""")

pages["index"] += showcase_fin

pages["index"] += googlemap


#######################################################################
# page cadre ##########################################################
#######################################################################
# pages["cadre"] = banniere(titre = "Au sein de la Guinguette vous profiterez de :",
                          # texte = """
# <i class="bi bi-play"></i>Terrains de p??tanque</br>
# <i class="bi bi-play"></i>Table de ping-pong</br>
# <i class="bi bi-play"></i>Baby-foot</br>
# <i class="bi bi-play"></i>Jeux de fl??chettes</br>
# <i class="bi bi-play"></i>Molky</br>""")

# pages["cadre"] += carousel(nom = "car1",
                       # images = ["assets/img/cadre/petanque.jpg","assets/img/cadre/pingpong.jpg","assets/img/cadre/babyfoot.jpg","assets/img/cadre/petanque2.jpg","assets/img/cadre/flechette.jpg"])

# pages["cadre"] += banniere(titre = "A cot?? de chez nous vous trouverez :",
                          # texte = """
# <i class="bi bi-play"></i>Espace ombrag?? avec tables, bancs et barbecue</br>
# <i class="bi bi-play"></i>Parcours de sant??</br>
# <i class="bi bi-play"></i>Aire de jeux pour enfants</br>
# <i class="bi bi-play"></i>Skatepark</br>
# <i class="bi bi-play"></i>Terrains de foot et de rugby</br>
# <i class="bi bi-play"></i>Spots de p??che</br>
# <i class="bi bi-play"></i>Aire de Camping-car</br>
# <i class="bi bi-play"></i>Sanitaires</br>""")

# pages["cadre"] += carousel(nom = "car2",
                       # images = ["assets/img/cadre/picnic.jpg", "assets/img/cadre/enfants.jpg", "assets/img/cadre/skate.jpg", "assets/img/cadre/football.jpg", "assets/img/cadre/rugby.jpg", "assets/img/cadre/peche.jpg", "assets/img/cadre/campingcar.jpg"])


#######################################################################
# page boissons #######################################################
#######################################################################
compteur = 0
#################################################
pages["boissons"] = titre("Nos Bi??res Pression")
pages["boissons"] += showcase_debut
for produit in carte.biere_pression:
    compteur += 1
    nom_pr = produit["nom"] + " - " + str(produit["prix1"]) + "??? - " + produit["contenant1"] + " de " + produit["qtt1"]
    description_pr = produit["description"] + " - Disponible en " + produit["contenant2"] + " de " + produit["qtt2"] + " ?? " + str(produit["prix2"]) + "???"
    if compteur % 2 == 1:
        pages["boissons"] += showcase_im_droite(url_img = produit["image"],
                                          titre = nom_pr,
                                          texte = description_pr)
    else:
        pages["boissons"] += showcase_im_gauche(url_img = produit["image"],
                                          titre = nom_pr,
                                          texte = description_pr)
pages["boissons"] += showcase_fin

#################################################
pages["boissons"] += titre("Nos Bi??res Bouteille")
pages["boissons"] += showcase_debut
for produit in carte.biere_bouteille:
    compteur += 1
    nom_pr = produit["nom"] + " - " + str(produit["prix1"]) + "???"
    description_pr = produit["description"] + " - " + produit["contenant1"] + " de " + produit["qtt1"]
    if compteur % 2 == 1:
        pages["boissons"] += showcase_im_droite(url_img = produit["image"],
                                          titre = nom_pr,
                                          texte = description_pr)
    else:
        pages["boissons"] += showcase_im_gauche(url_img = produit["image"],
                                          titre = nom_pr,
                                          texte = description_pr)
pages["boissons"] += showcase_fin

#################################################
pages["boissons"] += titre("Nos Vins")
pages["boissons"] += showcase_debut
for produit in carte.vin:
    compteur += 1
    nom_pr = produit["nom"] + " - " + str(produit["prix1"]) + "??? - " + produit["contenant1"] + " de " + produit["qtt1"]
    description_pr = produit["description"] + " - Disponible en " + produit["contenant2"] + " de " + produit["qtt2"] + " ?? " + str(produit["prix2"]) + "???"
    if compteur % 2 == 1:
        pages["boissons"] += showcase_im_droite(url_img = produit["image"],
                                          titre = nom_pr,
                                          texte = description_pr)
    else:
        pages["boissons"] += showcase_im_gauche(url_img = produit["image"],
                                          titre = nom_pr,
                                          texte = description_pr)
pages["boissons"] += showcase_fin


#################################################
pages["boissons"] += titre("Nos Boissons Sans Alcool")
pages["boissons"] += showcase_debut
for produit in carte.soft:
    compteur += 1
    nom_pr = produit["nom"] + " - " + str(produit["prix1"]) + "??? - " + produit["contenant1"] + " de " + produit["qtt1"]
    description_pr = produit["description"] + " - Disponible en " + produit["contenant2"] + " de " + produit["qtt2"] + " ?? " + str(produit["prix2"]) + "???"
    if compteur % 2 == 1:
        pages["boissons"] += showcase_im_droite(url_img = produit["image"],
                                          titre = nom_pr,
                                          texte = description_pr)
    else:
        pages["boissons"] += showcase_im_gauche(url_img = produit["image"],
                                          titre = nom_pr,
                                          texte = description_pr)
pages["boissons"] += showcase_fin

#######################################################################
# page restauration ###################################################
#######################################################################
compteur = 0
#################################################
pages["restauration"] = titre("Nos Planches")
pages["restauration"] += showcase_debut
for produit in carte.planches:
    compteur += 1
    nom_pr = produit["nom"] + " - " + str(produit["prix1"]) + "???"
    description_pr = produit["description"] + " - " + produit["qtt1"]
    if compteur % 2 == 1:
        pages["restauration"] += showcase_im_droite(url_img = produit["image"],
                                          titre = nom_pr,
                                          texte = description_pr)
    else:
        pages["restauration"] += showcase_im_gauche(url_img = produit["image"],
                                          titre = nom_pr,
                                          texte = description_pr)
pages["restauration"] += showcase_fin

#################################################
pages["restauration"] += titre("Nos Glaces")
pages["restauration"] += showcase_debut
for produit in carte.glace:
    compteur += 1
    nom_pr = produit["nom"] + " - " + str(produit["prix1"]) + "???" + " - " + str(produit["qtt1"]) + " " + str(produit["contenant1"])
    description_pr = produit["description"]
    if compteur % 2 == 1:
        pages["restauration"] += showcase_im_droite(url_img = produit["image"],
                                          titre = nom_pr,
                                          texte = description_pr)
    else:
        pages["restauration"] += showcase_im_gauche(url_img = produit["image"],
                                          titre = nom_pr,
                                          texte = description_pr)
pages["restauration"] += showcase_fin

#######################################################################
# page acces ##########################################################
#######################################################################
pages["acces"] = banniere(titre = "Acc??s",
                          texte = """
Nous sommes situ??s ?? 40 km de Toulouse</br>
et 8 km de Montauban centre</br>
Nous retrouver avec <a href="waze://?ll=43.966835,1.341984"><img src="assets/img/acces/waze.png" alt="" width="50" height="50"></a></br>
<a href="https://umap.openstreetmap.fr/fr/map/acces-la-terrasse_721036">Voir le plan en plein ??cran</a>""")

pages["acces"] += osmacces

pages["acces"] += banniere(titre = "Localisation",
                          texte = """
environnement proche</br>
<a href="https://umap.openstreetmap.fr/fr/map/la-terrasse-82_721008">Voir le plan en plein ??cran</a>""")

pages["acces"] += osmlocalisation

#######################################################################
# MAIN ################################################################
#######################################################################
for pa in pages:
    fichier = pa + ".html"
    with open(fichier, "w") as f:
        if pa == "index":
            f.write(headerhtml("Accueil"))
        else:
            f.write(headerhtml(pa.capitalize()))
        f.write(pages[pa])
        f.write(footerhtml)
