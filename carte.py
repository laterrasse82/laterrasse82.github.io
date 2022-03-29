#!/usr/bin/env python3
# -*- coding: utf-8 -*-

bieres_pression = [{"nom":"Ratz blanche",
            "description":"bla bla bla",
            "prix":"4.5€",
            "qtt":"25cl",
            "image":"assets/img/no_img.jpg"
                },
            {"nom":"Ratz blonde",
            "description":"bla bla bla",
            "prix":"4.5€",
            "qtt":"25cl",
            "image":"assets/img/no_img.jpg"
                },
            {"nom":"Ratz IPA",
            "description":"bla bla bla",
            "prix":"4.5€",
            "qtt":"25cl",
            "image":"assets/img/no_img.jpg"
                }
]

bieres_bouteille = [{"nom":"Ratz blanche",
            "description":"bla bla bla",
            "prix":"4.5€",
            "qtt":"33cl",
            "image":"assets/img/no_img.jpg"
                },
            {"nom":"Ratz blonde",
            "description":"bla bla bla",
            "prix":"4.5€",
            "qtt":"33cl",
            "image":"assets/img/no_img.jpg"
                },
            {"nom":"Ratz IPA",
            "description":"bla bla bla",
            "prix":"4.5€",
            "qtt":"33cl",
            "image":"assets/img/no_img.jpg"
                },
            {"nom":"Ocale blanche",
            "description":"bla bla bla",
            "prix":"4.5€",
            "qtt":"33cl",
            "image":"assets/img/no_img.jpg"
                },
            {"nom":"Ocale blonde",
            "description":"bla bla bla",
            "prix":"4.5€",
            "qtt":"33cl",
            "image":"assets/img/no_img.jpg"
                },
            {"nom":"Ocale IPA",
            "description":"bla bla bla",
            "prix":"4.5€",
            "qtt":"33cl",
            "image":"assets/img/no_img.jpg"
                },
            {"nom":"producteur C blanche",
            "description":"bla bla bla",
            "prix":"4.5€",
            "qtt":"33cl",
            "image":"assets/img/no_img.jpg"
                },
            {"nom":"producteur C blonde",
            "description":"bla bla bla",
            "prix":"4.5€",
            "qtt":"33cl",
            "image":"assets/img/no_img.jpg"
                },
            {"nom":"producteur C IPA",
            "description":"bla bla bla",
            "prix":"4.5€",
            "qtt":"33cl",
            "image":"assets/img/no_img.jpg"
                }
]

vin = [{"nom":"vin rouge A",
            "description":"bla bla bla",
            "prix_verre":"4€",
            "prix_bouteille":"18€",
            "qtt_verre":"12cl",
            "qtt_bouteille":"75cl",
            "image":"assets/img/no_img.jpg"
                },
        {"nom":"vin rouge B",
            "description":"bla bla bla",
            "prix_verre":"3.5€",
            "prix_bouteille":"15€",
            "qtt_verre":"12cl",
            "qtt_bouteille":"75cl",
            "image":"assets/img/no_img.jpg"
                },
        {"nom":"vin blanc A",
            "description":"bla bla bla",
            "prix_verre":"4€",
            "prix_bouteille":"18€",
            "qtt_verre":"12cl",
            "qtt_bouteille":"75cl",
            "image":"assets/img/no_img.jpg"
                },
        {"nom":"vin blanc B",
            "description":"bla bla bla",
            "prix_verre":"3.5€",
            "prix_bouteille":"15€",
            "qtt_verre":"12cl",
            "qtt_bouteille":"75cl",
            "image":"assets/img/no_img.jpg"
                },
        {"nom":"vin rosé A",
            "description":"bla bla bla",
            "prix_verre":"4€",
            "prix_bouteille":"18€",
            "qtt_verre":"12cl",
            "qtt_bouteille":"75cl",
            "image":"assets/img/no_img.jpg"
                },
        {"nom":"vin rosé B",
            "description":"bla bla bla",
            "prix_verre":"3.5€",
            "prix_bouteille":"15€",
            "qtt_verre":"12cl",
            "qtt_bouteille":"75cl",
            "image":"assets/img/no_img.jpg"
                }        
]

coktail = [{"nom":"Mojito",
            "description":"bla bla bla",
            "prix":"8€",
            "qtt":"25cl",
            "image":"assets/img/no_img.jpg"
                },
            {"nom":"Apérol Spritz",
            "description":"bla bla bla",
            "prix":"8€",
            "qtt":"25cl",
            "image":"assets/img/no_img.jpg"
                },
            {"nom":"Moscow Mule",
            "description":"bla bla bla",
            "prix":"8€",
            "qtt":"25cl",
            "image":"assets/img/no_img.jpg"
                }
]

sans_alcool = [{"nom":"jus de pomme",
            "description":"bla bla bla",
            "prix_verre":"2€",
            "prix_bouteille":"5€",
            "qtt_verre":"20cl",
            "qtt_bouteille":"75cl",
            "image":"assets/img/no_img.jpg"
                },
        {"nom":"jus de poire",
            "description":"bla bla bla",
            "prix_verre":"2€",
            "prix_bouteille":"5€",
            "qtt_verre":"20cl",
            "qtt_bouteille":"75cl",
            "image":"assets/img/no_img.jpg"
                },
        {"nom":"eau aromatisée maison",
            "description":"bla bla bla",
            "prix_verre":"1€",
            "prix_bouteille":"3€",
            "qtt_verre":"20cl",
            "qtt_bouteille":"75cl",
            "image":"assets/img/no_img.jpg"
                },
        {"nom":"limouna maison",
            "description":"bla bla bla",
            "prix_verre":"3€",
            "prix_bouteille":"8€",
            "qtt_verre":"20cl",
            "qtt_bouteille":"75cl",
            "image":"assets/img/no_img.jpg"
                },
        {"nom":"eau gazeuse",
            "description":"bla bla bla",
            "prix_verre":"2€",
            "prix_bouteille":"5€",
            "qtt_verre":"20cl",
            "qtt_bouteille":"75cl",
            "image":"assets/img/no_img.jpg"
                },
        {"nom":"thé glacé maison",
            "description":"bla bla bla",
            "prix_verre":"3€",
            "prix_bouteille":"8€",
            "qtt_verre":"20cl",
            "qtt_bouteille":"75cl",
            "image":"assets/img/no_img.jpg"
                }
]

glace = [{"nom":"3 boules, parfums au choix",
            "description":"Chocolat, Vanille, Fraise, Mangue, Rhum Raisin</br>1€ la boule supplémentaire",
            "prix":"3€",
            "image":"assets/img/no_img.jpg"
                }
]

planches = [{"nom":"Charcuterie",
            "description":"bla bla bla",
            "prix":"15€",
            "qtt":"250g",
            "image":"assets/img/no_img.jpg"
                },
            {"nom":"Fromage",
            "description":"bla bla bla",
            "prix":"15€",
            "qtt":"250g",
            "image":"assets/img/no_img.jpg"
                },
            {"nom":"Tartine",
            "description":"bla bla bla",
            "prix":"8€",
            "qtt":"250g",
            "image":"assets/img/no_img.jpg"
                },
            {"nom":"Crudités",
            "description":"bla bla bla",
            "prix":"8€",
            "qtt":"250g",
            "image":"assets/img/no_img.jpg"
                },
            {"nom":"Fruits",
            "description":"bla bla bla",
            "prix":"8€",
            "qtt":"250g",
            "image":"assets/img/no_img.jpg"
                },
            {"nom":"Fruits secs",
            "description":"bla bla bla",
            "prix":"4€",
            "qtt":"250g",
            "image":"assets/img/no_img.jpg"
                }
]

