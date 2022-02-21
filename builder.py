#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
                        <li class="nav-item"><a class="nav-link" href="cadre.html">Cadre</a></li>
                        <li class="nav-item"><a class="nav-link" href="boissons.html">Boissons</a></li>
			            <li class="nav-item"><a class="nav-link" href="restauration.html">Restauration</a></li>
                        <li class="nav-item"><a class="nav-link" href="acces.html">Accès</a></li>
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
                            <li class="list-inline-item me-4">
                                <a href="#!"><i class="bi-twitter fs-1" style="color: #b7975a;"></i></a>
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
                                       texte = "La Terrasse vous accueille dans un décor naturel et élégant sur les berges du Tarn. Envie de passer un moment en famille, entre amis, en extérieur, en buvant un verre en musique autour d’une planche dans un cadre magnifique. </br> Alors rejoignez nous pour une parenthèse dans votre quotidien.")
                                       
pages["index"] += showcase_im_gauche(url_img = "assets/img/boissons.jpg",
                                       titre = "Les boissons",
                                       texte = """<b>Selon votre envie du moment et avec modération, nous vous proposons :</b></br>
<i class="bi bi-play"></i>Pressions et bières locales</br>
<i class="bi bi-play"></i>Vin de la région</br>
<i class="bi bi-play"></i>Des cocktails</br>
<i class="bi bi-play"></i>Les classiques spiritueux : Rhum, Whisky, Tequila etc...</br>
<i class="bi bi-play"></i>Des boissons sans alcool : jus de fruits, cocktails etc...</br>""")

pages["index"] += showcase_im_droite(url_img = "assets/img/restauration.jpg",
                                       titre = "La restauration",
                                       texte = """<b>Boire, c’est sympa, mais manger des produits locaux, c’est pas mal non plus…</br>
Nous vous proposons :</br></b>
<i class="bi bi-play"></i>Planche de charcuterie.</br>
<i class="bi bi-play"></i>Planche de fromage.</br>
<i class="bi bi-play"></i>Planche de toast.</br>
<i class="bi bi-play"></i>Planche de fruit.</br>
<i class="bi bi-play"></i>Maxi planche.</br>
Les planches sont accompagnées de bâtonnets de crudités de saison et de sauce maison.""")

pages["index"] += showcase_im_gauche(url_img = "assets/img/activite.jpg",
                                       titre = "Les activités",
                                       texte = """Envie de vous dégourdir les jambes, de défier vos proches, de passer un bon moment ?</br>
Nous mettons à votre disposition des terrains de pétanque, baby-foot, fléchettes, molky, ping-pong...</br>
Vous pourrez aussi profiter, aux abords de la guinguette de tables et bancs au sein d'un parc ombragé, d'un skate-park, de terrains de foot et de rugby, d'un parcours de santé…""")

pages["index"] += showcase_im_droite(url_img = "assets/img/emporter.jpg",
                                       titre = "A emporter",
                                       texte = """Vous pouvez profiter de nos produits à emporter dans une box pique nique, à consommer ou vous le souhaitez""")

pages["index"] += showcase_im_gauche(url_img = "assets/img/ouverture.jpg",
                                       titre = "Ouverture",
                                       texte = """
La Guinguette sera ouverte :</br>
Du 1er Juin au 30 Septembre</br>
Du Mercredi au Dimanche</br>
De 16h00 à 02h00</br>
L'ouverture dépends des conditions météos, en savoir plus...</br>
Un parking gratuit est a disposition.""")

pages["index"] += showcase_fin

pages["index"] += googlemap


#######################################################################
# page cadre ##########################################################
#######################################################################
pages["cadre"] = banniere(titre = "Au sein de la Guinguette vous profiterez de :",
                          texte = """
<i class="bi bi-play"></i>Terrains de pétanque</br>
<i class="bi bi-play"></i>Table de ping-pong</br>
<i class="bi bi-play"></i>Baby-foot</br>
<i class="bi bi-play"></i>eux de fléchettes</br>
<i class="bi bi-play"></i>Molky</br>""")

pages["cadre"] += carousel(nom = "car1",
                       images = ["assets/img/cadre/petanque.jpg","assets/img/cadre/pingpong.jpg","assets/img/cadre/babyfoot.jpg","assets/img/cadre/petanque2.jpg","assets/img/cadre/flechette.jpg"])

pages["cadre"] += banniere(titre = "A coté de chez nous vous trouverez :",
                          texte = """
<i class="bi bi-play"></i>Espace ombragé avec tables, bancs et barbecue</br>
<i class="bi bi-play"></i>Parcours de santé</br>
<i class="bi bi-play"></i>Aire de jeux pour enfants</br>
<i class="bi bi-play"></i>Skatepark</br>
<i class="bi bi-play"></i>Terrains de foot et de rugby</br>
<i class="bi bi-play"></i>Spots de pêche</br>
<i class="bi bi-play"></i>Aire de Camping-car</br>
<i class="bi bi-play"></i>Sanitaires</br>""")

pages["cadre"] += carousel(nom = "car2",
                       images = ["assets/img/cadre/picnic.jpg", "assets/img/cadre/enfants.jpg", "assets/img/cadre/skate.jpg", "assets/img/cadre/football.jpg", "assets/img/cadre/rugby.jpg", "assets/img/cadre/peche.jpg", "assets/img/cadre/campingcar.jpg"])


#######################################################################
# page boissons #######################################################
#######################################################################
pages["boissons"] = titre("Nos Boissons Alcoolisées")
pages["boissons"] += showcase_debut 
pages["boissons"] += showcase_im_droite(url_img = "assets/img/ambiance.jpg",
                                          titre = "Les bières",
                                          texte = "Produites localement")
pages["boissons"] += showcase_im_gauche(url_img = "assets/img/ambiance.jpg",
                                          titre = "Les whiskies",
                                          texte = "Selon votre envie..")
pages["boissons"] += showcase_fin
pages["boissons"] += titre("Nos Boissons Sans Alcool")
pages["boissons"] += showcase_debut 
pages["boissons"] += showcase_im_droite(url_img = "assets/img/ambiance.jpg",
                                          titre = "Les jus",
                                          texte = "Produites localement")
pages["boissons"] += showcase_im_gauche(url_img = "assets/img/ambiance.jpg",
                                          titre = "Les citronades",
                                          texte = "Selon votre envie..")
pages["boissons"] += showcase_fin


#######################################################################
# page restauration ###################################################
#######################################################################
pages["restauration"] = titre("Nos Planches")
pages["restauration"] += showcase_debut 
pages["restauration"] += showcase_im_droite(url_img = "assets/img/ambiance.jpg",
                                          titre = "fromage",
                                          texte = "Produites localement")
pages["restauration"] += showcase_im_gauche(url_img = "assets/img/ambiance.jpg",
                                          titre = "charcuterie",
                                          texte = "Selon votre envie..")
pages["restauration"] += showcase_im_droite(url_img = "assets/img/ambiance.jpg",
                                          titre = "toast",
                                          texte = "Produites localement")
pages["restauration"] += showcase_im_gauche(url_img = "assets/img/ambiance.jpg",
                                          titre = "royale",
                                          texte = "à partager.")
pages["restauration"] += showcase_fin
pages["restauration"] += titre("Nos glaces")
pages["restauration"] += showcase_debut 
pages["restauration"] += showcase_im_droite(url_img = "assets/img/ambiance.jpg",
                                          titre = "chocolat",
                                          texte = "Produites localement")
pages["restauration"] += showcase_im_gauche(url_img = "assets/img/ambiance.jpg",
                                          titre = "vanille",
                                          texte = "Selon votre envie..")
pages["restauration"] += showcase_fin

#######################################################################
# page acces ##########################################################
#######################################################################
pages["acces"] = banniere(titre = "Accès",
                          texte = """
Nous sommes situés à 40 km de Toulouse</br>
et 8 km de Montauban centre</br>
Nous retrouver avec <a href="https://www.waze.com/fr/live-map/directions?to=ll.43.966835%2C1.341984"><img src="assets/img/acces/waze.png" alt="" width="50" height="50"></a></br>
<a href="https://umap.openstreetmap.fr/fr/map/acces-la-terrasse_721036">Voir le plan en plein écran</a>""")

pages["acces"] += osmacces

pages["acces"] += banniere(titre = "Localisation",
                          texte = """
environnement proche</br>
<a href="https://umap.openstreetmap.fr/fr/map/la-terrasse-82_721008">Voir le plan en plein écran</a>""")

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
