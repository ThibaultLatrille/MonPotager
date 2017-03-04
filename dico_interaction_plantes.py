# -*- coding: utf-8 -*-

interaction_plante = [
    (1, 2, 1),  # carotte-poireau
    (1, 3, 1),  # carotte-ail
    (1, 13, 1),  # carotte-oignon
    (1, 49, 1),  # carotte-échalote
    (1, 28, 1),  # carotte-ciboulette
    (1, 18, 1),  # carotte-betterave
    (1, 7, 1),  # carotte-pois
    (1, 21, 1),  # carotte-radis
    (1, 20, 1),  # carotte-laitue
    (1, 50, 1),  # carotte-roquette
    (1, 5, 1),  # carotte-panais
    (1, 6, 1),  # carotte-tomate
    (1, 4, 1),  # carotte-haricot
    (1, 50, 1),  # carotte-salsifis
    (1, 52, 1),  # carotte-piment
    (1, 53, 1),  # carotte-lin
    (1, 54, 1),  # carotte-romarin
    (1, 55, 1),  # carotte-sauge
    (1, 56, 1),  # carotte-absinthe
    (1, 57, 1),  # carotte-coriandre
    (1, 25, -1),  # carotte-aneth
    (1, 58, -1),  # carotte-maïs
    (1, 64, -1),  # carotte-bette
    (1, 46, 2),  # carotte-carabe
    (1, 59, -1),  # carotte cultivée-carotte sauvage
    (59, 60, 1),  # carotte sauvage-choux
    (2, 1, 1),  # poireau-carotte
    (2, 17, 1),  # poireau-céleri
    (2, 61, 1),  # poireau-asperge
    (2, 20, 1),  # poireau-laitue
    (2, 9, 1),  # poireau-mâche
    (2, 6, 1),  # poireau-tomate
    (2, 23, 1),  # poireau-fenouil
    (2, 62, 1),  # poireau-artichaut
    (2, 31, 1),  # poireau-moutarde
    (2, 63, 1),  # poireau-cresson
    (2, 64, -1),  # poireau-bette
    (2, 18, -1),  # poireau-betterave
    (2, 60, -1),  # poireau-choux
    (2, 4, -1),  # poireau-haricot
    (2, 26, -1),  # poireau-persil
    (2, 7, -1),  # poireau-pois
    (2, 24, 1),  # poireau-fraisier
    (3, 65, 1),  # ail-pêcher
    (3, 66, 1),  # ail-pommier
    (3, 67, 1),  # ail-poirier
    (3, 68, 1),  # ail-prunier
    (3, 69, 1),  # ail-chicorée
    (3, 70, 1),  # ail-pissenlit
    (3, 71, 1),  # ail-topinambour
    (3, 6, 1),  # ail-tomate
    (3, 24, 1),  # ail-fraisier
    (3, 72, 1),  # ail-framboisier
    (3, 73, 1),  # ail-rosier
    (3, 60, -1),  # ail-chou
    (3, 12, -1),  # ail-pomme de terre
    (3, 4, -1),  # ail-haricot
    (3, 7, -1),  # ail-pois
    (3, 37, -1),  # ail-souci
    (3, 62, -1),  # ail-artichaut
    (3, 61, -1),  # ail-asperge
    (4, 58, 1),  # haricot-maïs
    (4, 74, 1),  # haricot-potiron
    (4, 60, 1),  # haricot-choux
    (4, 75, 1),  # haricot-melon
    (4, 76, 1),  # haricot-pastèque
    (4, 1, 1),  # haricot-carotte
    (4, 17, 1),  # haricot-céleri
    (4, 77, 1),  # haricot-concombre
    (4, 12, 1),  # haricot-pomme de terre
    (4, 78, 1),  # haricot-épinard
    (4, 20, 1),  # haricot-laitue
    (4, 36, 1),  # haricot-bourrache
    (4, 79, 1),  # haricot-capucine
    (4, 27, 1),  # haricot-sarriette annuelle
    (4, 81, 1),  # haricot-tournesol
    (4, 56, 1),  # haricot-absinthe
    (4, 2, -1),  # haricot-poireau
    (4, 3, -1),  # haricot-ail
    (4, 49, -1),  # haricot-échalote
    (4, 28, -1),  # haricot-ciboulette
    (4, 13, -1),  # haricot-oignon
    (4, 23, -1),  # haricot-fenouil
    (4, 7, -1),  # haricot-pois
    (4, 22, -1),  # haricot-courgette
    (4, 82, -1),  # haricot-kiwi
    (5, 21, 1),  # panais-radis
    (5, 18, 1),  # panais-betterave
    (5, 15, 1),  # panais-chou rave
    (5, 13, 1),  # panais-oignon
    (5, 20, -1),  # panais-laitue
    (6, 83, 1),  # tomate-rosier d'inde
    (6, 38, 1),  # tomate-oeillets d'Inde
    (6, 85, 1),  # tomate-cosmos
    (6, 86, 1),  # tomate-camomille allemande
    (6, 60, 1),  # tomate-choux
    (6, 87, 1),  # tomate-géranium
    (6, 88, 1),  # tomate-inule visqueuse
    (6, 76, 1),  # tomate-pastèque
    (6, 10, 1),  # tomate-concombre
    (6, 73, 1),  # tomate-rosier
    (6, 1, 1),  # tomate-carotte
    (6, 78, 1),  # tomate-épinard
    (6, 4, 1),  # tomate-haricot
    (6, 13, 1),  # tomate-oignon
    (6, 26, 1),  # tomate-persil
    (6, 2, 1),  # tomate-poireau
    (6, 20, 1),  # tomate-laitue
    (6, 12, -1),  # tomate-pomme de terre
    (6, 81, -1),  # tomate-tournesol
    (6, 44, -1),  # tomate-mildiou
    (12, 44, -1),  # pomme de terre-mildiou
    (6, 18, -1),  # tomate-betterave
    (6, 23, -1),  # tomate-fenouil
    (6, 24, -1),  # tomate-fraisier
    (89, 42, -3),  # ricin-nématodes
    (89, 90, -3),  # ricin-doryphores
    (7, 89, 1),  # pois-ricin
    (7, 12, 1),  # pois-pomme de terre
    (7, 57, 1),  # pois-coriandre
    (7, 27, 1),  # pois-sarriette
    (7, 13, -1),  # pois-oignon
    (7, 3, -1),  # pois-ail
    (7, 49, -1),  # pois-échalote
    (7, 2, -1),  # pois-poireau
    (7, 26, -1),  # pois-persil
    (8, 6, 1),  # poivron-tomate
    (8, 1, 1),  # poivron-carotte
    (8, 60, 1),  # poivron-choux
    (9, 91, -1),  # mâche-amarante
    (9, 82, -1),  # mâche-kiwi
    (9, 60, -1),  # mâche-choux
    (9, 2, 1),  # mâche-poireau
    (9, 13, 1),  # mâche-oignon
    (9, 24, 1),  # mâche-fraisier
    (9, 35, 1),  # mâche-trèfle
    (9, 74, 1),  # mâche-potiron
    (10, 6, 1),  # tomate-concombre
    (12, 82, 1),  # pomme de terre-kiwi
    (12, 61, 1),  # pomme de terre-asperge
    (12, 86, 1),  # pomme de terre-camomille allemande
    (86, 45, 2),  # camomille allemande-coccinelles
    (86, 42, -3),  # camomille allemande-nématodes
    (12, 79, 1),  # pomme de terre-capucine
    (12, 17, 1),  # pomme de terre-céleri
    (12, 92, 1),  # pomme de terre-chanvre
    (12, 60, 1),  # pomme de terre-choux
    (12, 93, 1),  # pomme de terre-ciboulette chinoise
    (12, 57, 1),  # pomme de terre-coriandre
    (12, 77, 1),  # pomme de terre-fève
    (12, 94, 1),  # pomme de terre-féverole
    (12, 4, 1),  # pomme de terre-haricot
    (12, 95, 1),  # pomme de terre-morelle de balbis
    (12, 7, 1),  # pomme de terre-pois
    (12, 21, 1),  # pomme de terre-radis
    (12, 37, 1),  # pomme de terre-souci
    (95, 90, -3),  # morelle de balbis-doryphores
    (95, 42, -3),  # morelle de balbis-nématodes
    (21, 63, 1),  # radis-cresson
    (21, 96, 1),  # radis-genêt
    (21, 29, 1),  # radis-cerfeuil
    (21, 5, 1),  # radis-panais
    (21, 1, 1),  # radis-carotte
    (21, 7, 1),  # radis-pois
    (21, 10, 1),  # radis-concombre
    (21, 11, 1),  # radis-cornichon
    (21, 78, 1),  # radis-épinard
    (21, 4, 1),  # radis-haricot
    (21, 17, 1),  # radis-céleri-rave
    (21, 12, 1),  # radis-pomme de terre
    (21, 6, 1),  # radis-tomate
    (21, 13, 1),  # radis-oignon
    (21, 28, -1),  # radis-ciboulette
    (21, 60, -1),  # radis-choux
    (13, 1, 1),  # oignon-carotte
    (13, 20, 1),  # oignon-laitue
    (13, 9, 1),  # oignon-mâche
    (13, 21, 1),  # oignon-radis
    (13, 35, 1),  # oignon-trèfle
    (13, 4, -1),  # oignon-haricot
    (13, 7, -1),  # oignon-pois
    (13, 82, -1),  # oignon-kiwi
    (13, 41, -3),  # oignon-pucerons
    (60, 69, -1),  # choux-chicorée
    (60, 24, -1),  # choux-fraisier
    (60, 2, -1),  # choux-poireau
    (60, 21, -1),  # choux-radis
    (60, 58, -1),  # choux-maïs
    (60, 9, -1),  # choux-mâche
    (60, 23, -1),  # choux-fenouil
    (60, 63, -1),  # choux-cresson
    (60, 22, -1),  # choux-courgette
    (60, 97, -1),  # choux-origan
    (60, 52, -1),  # choux-piment
    (60, 25, 1),  # choux-aneth
    (60, 17, 1),  # choux-céleri
    (60, 4, 1),  # choux-haricot
    (60, 31, 1),  # choux-moutarde
    (60, 54, 1),  # choux-romarin
    (60, 6, 1),  # choux-tomate
    (60, 56, 1),  # choux-absinthe
    (60, 85, 1),  # choux-cosmos
    (60, 55, 1),  # choux-sauge officinale
    (60, 98, 1),  # choux-thym
    (60, 20, 1),  # choux-laitue
    (60, 78, 1),  # choux-épinard
    (60, 38, 1),  # choux-oeillet d'inde
    (60, 79, 1),  # choux-capucine
    (60, 12, 1),  # choux-pomme de terre
    (60, 77, 1),  # choux-fève
    (60, 7, 1),  # choux-pois
    (60, 33, 1),  # choux-mélisse
    (60, 57, 1),  # choux-coriandre
    (60, 74, 1),  # choux-potiron
    (60, 69, 1),  # choux-chicorée
    (60, 29, 1),  # choux-cerfeuil
    (60, 99, 1),  # choux-cumin
    (60, 86, 1),  # choux-camomille allemande
    (60, 64, 1),  # choux-bette
    (60, 30, 1),  # choux-basilic
    (60, 62, 1),  # choux-artichaut
    (60, 59, 1),  # choux-carotte sauvage
    (60, 100, 1),  # choux-coquelicot
    (60, 5, 1),  # choux-panais
    (60, 35, 1),  # choux-trèfle blanc
    (60, 101, 1),  # choux-phacélie
    (60, 102, 1),  # choux-matricaire inodore
    (60, 48, 1),  # choux-achillée millefeuille
    (60, 103, 1),  # choux-ray-grass d'Italie
    (60, 104, 1),  # choux-sarrasin
    (17, 60, 1),  # céleri-choux
    (17, 2, 1),  # céleri-poireau
    (17, 23, 1),  # céleri-fenouil
    (17, 6, 1),  # céleri-tomate
    (17, 4, 1),  # céleri-haricot
    (17, 7, 1),  # céleri-pois
    (17, 64, 1),  # céleri-bette
    (17, 18, 1),  # céleri-betterave
    (17, 22, 1),  # céleri-courgette
    (17, 105, 1),  # céleri-courges
    (17, 74, 1),  # céleri-potiron
    (17, 58, -1),  # céleri-maïs
    (17, 26, -1),  # céleri-persil
    (17, 20, -1),  # céleri-laitue
    (17, 106, -1),  # céleri-angélique
    (18, 20, 1),  # betterave-laitue
    (18, 17, 1),  # betterave-céleri
    (18, 57, 1),  # betterave-coriandre
    (18, 5, 1),  # betterave-panais
    (18, 6, -1),  # betterave-tomate
    (18, 106, -1),  # betterave-angélique
    (18, 61, -1),  # betterave-asperge
    (18, 78, -1),  # betterave-épinard
    (18, 2, -1),  # betterave-poireau
    (20, 60, 1),  # laitue-choux
    (20, 1, 1),  # laitue-carotte
    (20, 13, 1),  # laitue-oignon
    (20, 7, 1),  # laitue-pois
    (20, 19, 1),  # laitue-cardon
    (20, 18, 1),  # laitue-betterave
    (20, 105, 1),  # laitue-courges
    (20, 77, 1),  # laitue-fève
    (20, 24, 1),  # laitue-fraisier
    (20, 75, 1),  # laitue-melon
    (20, 4, 1),  # laitue-haricot
    (20, 107, 1),  # laitue-navet
    (20, 2, 1),  # laitue-poireau
    (20, 62, 1),  # laitue-artichaut
    (20, 29, 1),  # laitue-cerfeuil
    (20, 25, 1),  # laitue-aneth
    (20, 53, 1),  # laitue-lin
    (20, 26, -1),  # laitue-persil
    (20, 17, -1),  # laitue-céleri
    (20, 81, -1),  # laitue-tournesol
    (20, 5, -1),  # laitue-panais
    (58, 22, -1),  # courgette-maïs
    (22, 4, -1),  # courgette-haricot
    (23, 17, 1),  # fenouil-céleri
    (23, 2, 1),  # fenouil-poireau
    (23, 30, 1),  # fenouil-basilic
    (23, 6, -1),  # fenouil-tomate
    (23, 56, -1),  # fenouil-absinthe
    (23, 10, -1),  # fenouil-concombre
    (23, 52, -1),  # fenouil-piment
    (23, 78, -1),  # fenouil-épinard
    (23, 4, -1),  # fenouil-haricot
    (23, 105, -1),  # fenouil-courges
    (23, 37, -1),  # fenouil-souci
    (23, 107, -1),  # fenouil-navet
    (23, 60, -1),  # fenouil-choux
    (23, 57, -1),  # fenouil-coriandre
    (23, 99, -1),  # fenouil-cumin
    (23, 109, 2),  # fenouil-araignées
    (23, 110, 2),  # fenouil-syrphes
    (23, 111, 2),  # fenouil-papillons
    (23, 41, -3),  # fenouil-pucerons
    (23, 112, -3),  # fenouil-lièvres
    (49, 60, -1),  # échalote-choux
    (49, 4, -1),  # échalote-haricot
    (49, 7, -1),  # échalote-pois
    (49, 1, 1),  # échalote-carotte
    (50, 18, 1),  # roquette-betterave
    (50, 1, 1),  # roquette-carotte
    (50, 69, 1),  # roquette-chicorée
    # (51,,), # SALSIFIS INFOS PEU SURES
    # (52,,), # PIMENT INFOS PEU SURES
    (18, 58, -1),  # maïs-betterave
    (58, 4, 1),  # maïs-haricot
    (58, 7, 1),  # maïs-pois
    (58, 74, 1),  # maïs-potiron
    (58, 58, 1),  # maïs-achillée millefeuille
    (20, 58, -1),  # maïs-laitue
    (58, 13, -1),  # maïs-oignon
    (58, 1, -1),  # maïs-carotte
    (58, 17, -1),  # maïs-céleri
    (58, 60, -1),  # maïs-choux
    (58, 41, -3),  # maïs-pucerons
    (61, 61, -1),  # asperge-asperge AUTOINTERACTION
    (61, 12, 1),  # asperge-pomme de terre
    (61, 10, 1),  # asperge-concombre
    (61, 26, 1),  # asperge-persil
    (61, 6, 1),  # asperge-tomate
    (61, 11, 1),  # asperge-cornichon
    (61, 2, 1),  # asperge-poireau
    (61, 7, 1),  # asperge-pois
    (61, 105, 1),  # asperge-courge
    (61, 30, 1),  # asperge-basilic
    (61, 83, 1),  # asperge-rose d'Inde
    (61, 79, 1),  # asperge-capucine
    (61, 32, -1),  # asperge-menthe
    (61, 18, -1),  # asperge-betterave
    (61, 64, -1),  # asperge-bette
    (61, 69, -1),  # asperge-chicorée
    (61, 13, -1),  # asperge-oignon
    (61, 3, -1),  # asperge-ail
    (61, 28, -1),  # asperge-ciboulette
    (62, 60, 1),  # artichaut-chou
    (62, 20, 1),  # artichaut-laitue
    (62, 78, 1),  # artichaut-épinard
    (62, 26, 1),  # artichaut-persil
    (62, 79, 1),  # artichaut-capucine
    (62, 2, 1),  # artichaut-poireau
    (62, 3, -1),  # artichaut-ail
    (62, 114, 2),  # artichaut-bourdons
    (63, 2, 1),  # cresson-poireau
    (63, 21, 1),  # cresson-radis
    (63, 60, -1),  # cresson-choux
    (63, 116, -3),  # cresson-campagnols
    (63, 41, -3),  # cresson-pucerons
    (63, 117, -3),  # cresson-chenilles
    (63, 118, -3),  # cresson-fourmis
    (63, 115, -3),  # cresson-escargots
    # (64,,1), #PEU D'INFOS : MAUVAISE COMPAGNE EN GENERAL
    (69, 78, 1),  # chicorée-épinard
    (69, 50, 1),  # chicorée-roquette
    (69, 37, 1),  # chicorée-soucis
    (69, 60, -1),  # chicorée-choux
    (69, 61, -1),  # chicorée-asperge
    (69, 107, -1),  # chicorée-navet
    (71, 78, 1),  # topinambour-épinard   A NOTER QUE C'EST UNE MAUVAISE COMPAGNE
    (74, 4, 1),  # potiron-haricot
    (74, 58, 1),  # potiron-maïs
    (74, 61, 1),  # potiron-asperge
    (74, 17, 1),  # potiron-céleri
    (74, 60, 1),  # potiron-choux
    (74, 20, 1),  # potiron-laitue
    (74, 9, 1),  # potiron-mâche
    (74, 7, 1),  # potiron-pois
    (74, 13, 1),  # potiron-oignon
    (74, 30, 1),  # potiron-basilic
    (74, 28, 1),  # potiron-ciboulette
    (74, 57, 1),  # potiron-coriandre
    (74, 97, 1),  # potiron-origan
    (74, 79, 1),  # potiron-capucine
    (74, 34, 1),  # potiron-tanaisie
    (74, 81, 1),  # potiron-tournesol
    (74, 21, -1),  # potiron-radis
    (74, 23, -1),  # potiron-fenouil
    (105, 4, 1),  # courges-haricot
    (105, 61, 1),  # courges-asperge
    (105, 17, 1),  # courges-céleri
    (105, 60, 1),  # courges-choux
    (105, 20, 1),  # courges-laitue
    (105, 9, 1),  # courges-mâche
    (105, 7, 1),  # courges-pois
    (105, 13, 1),  # courges-oignon
    (105, 30, 1),  # courges-basilic
    (105, 28, 1),  # courges-ciboulette
    (105, 57, 1),  # courges-coriandre
    (105, 97, 1),  # courges-origan
    (105, 79, 1),  # courges-capucine
    (105, 34, 1),  # courges-tanaisie
    (105, 81, 1),  # courges-tournesol
    (105, 21, -1),  # courges-radis
    (105, 23, -1),  # courges-fenouil
    (77, 60, 1),  # fève-choux
    (77, 12, 1),  # fève-pomme de terre
    (77, 58, 1),  # fève-maïs
    (77, 20, 1),  # fève-laitue
    (77, 27, 1),  # fève-sarriette annuelle
    (77, 30, 1),  # fève-basilic
    (77, 13, -1),  # fève-oignon
    (78, 78, -1),  # épinard-épinard AUTOINTERACTION
    (78, 60, 1),  # épinard-choux
    (78, 73, 1),  # épinard-rosier
    (78, 62, 1),  # épinard-artichaut
    (78, 69, 1),  # épinard-chicorée
    (78, 24, 1),  # épinard-fraisier
    (78, 4, 1),  # épinard-haricot
    (78, 107, 1),  # épinard-navet
    (78, 51, 1),  # épinard-salsifis
    (78, 21, 1),  # épinard-radis
    # (94,,1), #fèverole PAS GRAND CHOSE; BIEN POUR ROTATIONS
    (107, 78, 1),  # navet-épinard
    (107, 24, 1),  # navet-fraisier
    (107, 82, -1),  # navet-kiwi
    (107, 27, -1),  # navet-sarriette
    (107, 23, -1),  # navet-fenouil
    (107, 69, -1),  # navet-chicorée
    (113, 4, 1),  # patate douce-haricot
    (113, 8, -1),  # patate douce-poivrons
    (113, 52, -1),  # patate douce-piment
    (24, 2, 1),  # fraisier-poireau
    (24, 3, 1),  # fraisier-ail
    (24, 28, 1),  # fraisier-ciboulette
    (24, 13, 1),  # fraisier-oignon
    (24, 65, 1),  # fraisier-pêcher
    (24, 60, -1),  # fraisier-choux
    (65, 3, 1),  # pêcher-ail
    (65, 28, 1),  # pêcher-ciboulette
    (65, 119, 1),  # pêcher-raifort
    (65, 24, 1),  # pêcher-fraisier
    (65, 120, 1),  # pêcher-chénopode blanc
    (65, 121, 1),  # pêcher-verge d'or
    (65, 34, 1),  # pêcher-tanaisie
    (65, 56, 1),  # pêcher-absinthe
    (65, 123, -1),  # pêcher-érable
    (65, 124, -1),  # pêcher-orme
    (65, 122, -1),  # pêcher-noisetier
    (65, 125, -1),  # pêcher-fusain d'Europe
    (66, 101, 1),  # pommier-phacélie
    (66, 129, 1),  # pommier-panicaut
    (66, 86, 1),  # pommier-camomille
    (66, 128, 1),  # pommier-potentille
    (66, 35, 1),  # pommier-trèfle
    (66, 79, 1),  # pommier-capucine
    (66, 126, 1),  # pommier-nerprun
    (66, 127, 1),  # pommier-noyer
    (66, 66, -1),  # pommier-pommier AUTOINTERACTION
    (66, 130, -1),  # pommier-baguenaudier
    (67, 35, 1),  # poirier-trèfle
    (67, 126, 1),  # poirier-nerprun alaterne
    (67, 131, -1),  # poirier-genévrier
    (67, 67, 1),  # poirier-poirier AUTOINTERACTION POUR POLLINISATION
    (68, 72, 1),  # prunier-framboisier
    (68, 132, 1),  # prunier-cerisier
    (68, 125, -1),  # prunier-fusain
    (68, 123, -1),  # prunier-érable
    (68, 124, -1),  # prunier-orme
    (68, 122, -1),  # prunier-noisetier
    (72, 37, 1),  # framboisier-souci
    (72, 3, 1),  # framboisier-ail
    (72, 68, 1),  # framboisier-prunier
    (72, 48, 1),  # framboisier-achillée millefeuille
    (72, 133, 1),  # framboisier-rue
    (72, 34, 1),  # framboisier-tanaisie
    (72, 134, -1),  # framboisier-myrtille
    (72, 135, -1),  # framboisier-ronce
    (75, 20, 1),  # melon-laitue
    (75, 30, 1),  # melon-basilic
    (76, 4, 1),  # pastèque-haricot
    (76, 6, 1),  # pastèque-tomate
    (76, 60, 1),  # pastèque-choux
    (82, 12, 1),  # kiwi-pomme de terre
    (82, 58, -1),  # kiwi-maïs
    (82, 4, -1),  # kiwi-haricot
    (82, 9, -1),  # kiwi-mâche
    (82, 107, -1),  # kiwi-navet
    (82, 13, -1),  # kiwi-oignon
    (122, 110, 2),  # noisetier-syrphes
    # (127,,1), #NOYER: ROLE INCOMPATIBLE AVERE
    (132, 119, 1),  # cerisier-raifort
    (132, 133, 1),  # cerisier-rue
    (25, 60, 1),  # aneth-choux
    (25, 10, 1),  # aneth-concombre
    (25, 11, 1),  # aneth-cornichon
    (25, 64, 1),  # aneth-bette
    (25, 20, 1),  # aneth-laitue
    (25, 13, 1),  # aneth-oignon
    (25, 1, -1),  # aneth-carotte
    (25, 41, -3),  # aneth-pucerons
    (26, 6, 1),  # persil-tomate
    (26, 13, 1),  # persil-oignon
    (26, 62, 1),  # persil-artichaut
    (26, 61, 1),  # persil-asperge
    (26, 17, -1),  # persil-céleri
    (26, 2, -1),  # persil-poireau
    (26, 7, -1),  # persil-pois
    (26, 20, -1),  # persil-laitue
    (27, 7, 1),  # sarriette-pois
    (27, 77, 1),  # sarriette-fève
    (27, 4, 1),  # sarriette-haricot
    (27, 55, -1),  # sarriette-sauge
    (27, 41, -3),  # sarriette-pucerons
    (28, 1, 1),  # ciboulette-carotte
    (28, 66, 1),  # ciboulette-pommier
    (28, 65, 1),  # ciboulette-pêcher
    (28, 136, 1),  # ciboulette-groseillier
    (28, 83, 1),  # ciboulette-rosier
    (28, 137, 1),  # ciboulette-cassis
    (28, 24, 1),  # ciboulette-fraisier
    (28, 10, 1),  # ciboulette-concombre
    (28, 105, 1),  # ciboulette-courge
    (28, 61, -1),  # ciboulette-asperge
    (28, 21, -1),  # ciboulette-radis
    (28, 4, -1),  # ciboulette-haricot
    (29, 21, 1),  # cerfeuil-radis
    (29, 20, 1),  # cerfeuil-laitue
    (29, 60, 1),  # cerfeuil-choux
    (29, 69, 1),  # cerfeuil-chicorée
    (29, 118, -3),  # cerfeuil-fourmis
    (29, 138, -3),  # cerfeuil-limaces
    (29, 115, -3),  # cerfeuil-escargots
    (29, 41, -3),  # cerfeuil-pucerons
    (30, 6, 1),  # basilic-tomate
    (30, 52, 1),  # basilic-piment
    (30, 10, 1),  # basilic-concombre
    (30, 11, 1),  # basilic-cornichon
    (30, 105, 1),  # basilic-courge
    (30, 75, 1),  # basilic-melon
    (30, 60, 1),  # basilic-choux
    (30, 77, 1),  # basilic-fève
    (30, 22, 1),  # basilic-courgette
    (30, 23, 1),  # basilic-fenouil
    (30, 61, 1),  # basilic-asperge
    (30, 133, -1),  # basilic-rue
    (30, 56, -1),  # basilic-absinthe
    (30, 42, -3),  # basilic-nématodes
    (30, 41, -3),  # basilic-pucerons
    (137, 28, 1),  # cassis-ciboulette
    (137, 56, 1),  # cassis-absinthe
    # (137,,1), #cassis-haricot FAVORABLE SI HARICOT NAIN, DEFAV SI HARICOT A RAMES
    (137, 34, 1),  # cassis-tanaisie
    (137, 1, 1),  # cassis-carotte
    (137, 13, 1),  # cassis-oignon
    (137, 107, 1),  # cassis-navet
    (137, 58, -1),  # cassis-maïs
    (136, 28, 1),  # groseillier-ciboulette
    (136, 56, 1),  # groseillier-absinthe
    # (136,,1), #groseillier-haricot FAVORABLE SI HARICOT NAIN, DEFAV SI HARICOT A RAMES
    (136, 34, 1),  # groseillier-tanaisie
    (136, 1, 1),  # groseillier-carotte
    (136, 13, 1),  # groseillier-oignon
    (136, 107, 1),  # groseillier-navet
    (136, 58, -1),  # groseillier-maïs
    (31, 60, 1),  # moutarde-choux
    (31, 20, 1),  # moutarde-laitue
    (31, 81, -1),  # moutarde-tournesol
    (31, 110, 2),  # moutarde-syrphes
    (32, 66, 1),  # menthe-pommier
    (32, 67, 1),  # menthe-poirier
    (32, 86, 1),  # menthe-camomille
    (32, 23, -1),  # menthe-fenouil
    (32, 61, -1),  # menthe-asperge
    (32, 59, -1),  # menthe-carotte sauvage
    (32, 114, 2),  # menthe-bourdon
    (32, 45, 2),  # menthe-coccinelles
    (32, 111, 2),  # menthe-papillons
    (32, 41, -3),  # menthe-pucerons
    (33, 60, 1),  # mélisse-choux
    (33, 55, -1),  # mélisse-sauge
    (33, 139, -1),  # mélisse-lavande
    (54, 60, 1),  # romarin-choux
    (54, 1, 1),  # romarin-carotte
    (54, 48, 1),  # romarin-achillée millefeuille
    (54, 55, -1),  # romarin-sauge
    (55, 60, 1),  # sauge-choux
    (55, 98, -1),  # sauge-thym
    (55, 54, -1),  # sauge-romarin
    (55, 33, -1),  # sauge-mélisse
    (55, 27, -1),  # sauge-sarriette
    (55, 57, -1),  # sauge-coriandre
    (55, 56, -1),  # sauge-absinthe
    (55, 60, 1),  # absinthe-choux
    (55, 107, 1),  # absinthe-navet
    (55, 4, 1),  # absinthe-haricot
    (55, 1, 1),  # absinthe-carotte
    (55, 21, 1),  # absinthe-radis
    (55, 136, 1),  # absinthe-groseillier
    (55, 140, 1),  # absinthe-agrumes
    (140, 139, 1),  # agrumes-lavande
    (140, 34, 1),  # agrumes-tanaisie
    (140, 56, 1),  # agrumes-absinthe
    (140, 38, 1),  # agrumes-oeillet
    (140, 83, 1),  # agrumes-rosier d'inde
    (57, 60, 1),  # coriandre-choux
    (57, 1, 1),  # coriandre-carotte
    (57, 7, 1),  # coriandre-pois
    (57, 18, 1),  # coriandre-betterave
    (57, 10, 1),  # coriandre-concombre
    (57, 12, 1),  # coriandre-pomme de terre
    (57, 141, 1),  # coriandre-anis
    (57, 23, -1),  # coriandre-fenouil
    (57, 55, -1),  # coriandre-sauge
    (57, 41, -3),  # coriandre-pucerons
    (141, 57, 1),  # anis-coriandre
    (141, 56, -1),  # anis-absinthe
    (27, 7, 1),  # sarriette-pois
    (27, 4, 1),  # sarriette-haricot
    (27, 77, 1),  # sarriette-fève
    (27, 55, -1),  # sarriette-sauge
    (27, 107, -1),  # sarriette-navet
    (27, 21, -1),  # sarriette-radis
    (93, 6, 1),  # ciboulette chinoise-tomate
    (93, 12, 1),  # ciboulette chinoise-pomme de terre
    (97, 105, 1),  # origan-courge
    (97, 10, 1),  # origan-concombre
    (97, 52, 1),  # origan-piment
    (97, 142, 1),  # origan-vigne
    (97, 60, -1),  # origan-choux
    (142, 97, 1),  # vigne-origan
    (142, 65, 1),  # vigne-pêcher
    (142, 66, 1),  # vigne-pommier
    (142, 73, 1),  # vigne-rosier
    (142, 35, 1),  # vigne-trèfle
    (142, 143, -1),  # vigne-laurier sauce
    (98, 60, 1),  # thym-choux
    (98, 73, 1),  # thym-rosier
    (98, 24, 1),  # thym-fraisier
    (98, 55, -1),  # thym-sauge
    (98, 39, -3),  # thym-limaces
    (98, 115, -3),  # thym-escargots
    (98, 41, -3),  # thym-pucerons
    (99, 60, 1),  # cumin-choux
    (99, 7, 1),  # cumin-pois
    (99, 23, 1),  # cumin-fenouil
    (99, 56, 1),  # cumin-absinthe
    (99, 6, 1),  # cumin-tomate
    (133, 132, 1),  # rue-cerisier
    (133, 73, 1),  # rue-rosier
    (133, 72, 1),  # rue-framboisier
    (133, 144, -3),  # rue-rats
    (133, 39, -3),  # rue-limaces
    (133, 41, -3),  # rue-pucerons
    (133, 42, -3),  # rue-nématodes
    (133, 30, -1),  # rue-basilic
    (133, 86, -1),  # rue-camomille
    (133, 48, -1),  # rue-achillée millefeuille
    (34, 65, 1),  # tanaisie-pêcher
    (34, 73, 1),  # tanaisie-rosier
    (34, 41, -3),  # tanaisie-pucerons
    (34, 110, 2),  # tanaisie-syrphes
    (34, 45, 2),  # tanaisie-coccinelles
    (35, 60, 1),  # trèfle-choux
    (35, 24, 1),  # trèfle-fraisier
    (35, 9, 1),  # trèfle-mâche
    (35, 67, 1),  # trèfle-poirier
    (35, 58, 1),  # trèfle-maïs
    (35, 66, 1),  # trèfle-pommier
    (35, 142, 1),  # trèfle-vigne
    (35, 136, -1),  # trèfle-groseillier
    (36, 110, 2),  # bourrache-syrphes
    (36, 114, 2),  # bourrache-bourdons
    (36, 138, -3),  # bourrache-limaces
    (36, 24, 1),  # bourrache-fraisiers
    (36, 4, 1),  # bourrache-haricots
    (37, 24, 1),  # soucis-fraisier
    (37, 69, 1),  # soucis-chicorée
    (37, 4, 1),  # soucis-haricot
    (37, 12, 1),  # soucis-pomme de terre
    (37, 6, 1),  # soucis-tomate
    (37, 73, 1),  # soucis-rosier
    (37, 23, -1),  # soucis-fenouil
    (37, 3, -1),  # soucis-ail
    (37, 104, -1),  # soucis-sarrasin
    (37, 72, 1),  # soucis-framboisier
    (37, 42, -3),  # soucis-nématodes
    (37, 45, 2),  # soucis-coccinelles
    (37, 145, 2),  # soucis-punaises
    (48, 72, 1),  # achillée millefeuille-framboisier
    (48, 54, 1),  # achillée millefeuille-romarin
    (48, 58, 1),  # achillée millefeuille-maïs
    (48, 133, -1),  # achillée millefeuille-rue
    (59, 60, 1),  # carotte sauvage-choux
    (59, 1, -1),  # carotte sauvage-carotte
    (70, 3, 1),  # pissenlit-ail
    (73, 139, 1),  # rosier-lavande
    (73, 26, 1),  # rosier-persil
    (73, 133, 1),  # rosier-rue
    (73, 34, 1),  # rosier-tanaisie
    (73, 37, 1),  # rosier-soucis
    (73, 98, 1),  # rosier-thym
    (73, 6, 1),  # rosier-tomates
    (73, 78, 1),  # rosier-épinard
    (73, 3, 1),  # rosier-ail
    (73, 28, 1),  # rosier-ciboulette
    (73, 13, 1),  # rosier-oignon
    (73, 49, 1),  # rosier-échalote
    (74, 66, 1),  # capucine-pommier
    (74, 21, 1),  # capucine-radis
    (74, 146, 1),  # capucine-brocoli
    (74, 4, 1),  # capucine-haricot
    (74, 62, 1),  # capucine-artichaut
    (81, 105, 1),  # tournesol-courge
    (81, 4, 1),  # tournesol-haricot
    (81, 58, 1),  # tournesol-mais
    (81, 21, -1),  # tournesol-radis
    (81, 31, -1),  # tournesol-moutarde
    (81, 6, -1),  # tournesol-tomate
    (81, 20, -1),  # tournesol-laitue
    (81, 10, -1),  # tournesol-concombre
    # (,,1), #brocoli- PAS DANS LE LEFRANCOIS et THOREZ
    (85, 60, 1),  # cosmos-choux
    (85, 6, 1),  # cosmos-tomates
    (85, 42, -3),  # cosmos-nématodes
    (85, 109, 2),  # cosmos-araignées
    (85, 45, 2),  # cosmos-coccinelles
    (86, 60, 1),  # camomille allemande-choux
    (86, 13, 1),  # camomille allemande-oignons
    (86, 7, 1),  # camomille allemande-pois
    (86, 12, 1),  # camomille allemande-pomme de terre
    (86, 133, -1),  # camomille allemande-rue
    (86, 41, -1),  # camomille allemande-pucerons
    (87, 145, 2),  # géranium-punaises
    (88, 147, 1),  # inule-olivier
    (88, 145, 2),  # inule-punaises
    (89, 42, -3),  # ricin-nématodes
    (89, 41, -3),  # ricin-pucerons
    (89, 90, -3),  # ricin-doryphores
    (91, 46, 2),  # amarante-carabes
    (91, 9, -1),  # amarante-mâche
    (91, 46, 2),  # amarante-carabes
    (92, 148, -3),  # chanvre-courtilières
    (95, 12, 1),  # morelle de balbis-pomme de terre
    (95, 42, -3),  # morelle de balbis-nématodes
    (95, 90, -3),  # morelle de balbis-doryphores
    (96, 21, 1),  # genêt-radis
    (96, 40, -3),  # genet-altises
    (101, 149, 1),  # phacélie-abeilles
    (101, 114, 1),  # phacélie-bourdons
    (101, 41, -3),  # phacélie-pucerons
    (101, 42, -3),  # phacélie-nématodes
    (101, 145, 2),  # phacélie-punaises
    (101, 45, 2),  # phacélie-coccinelles
    (101, 110, 2),  # phacélie-syrphes
    (101, 37, 1),  # phacélie-soucis
    (106, 150, 2),  # angélique-chrysope
    (106, 45, 2),  # angélique-coccinelles
    (106, 25, -1),  # angélique-aneth
    (106, 17, -1),  # angélique-céleri
    (106, 18, -1),  # angélique-betterave
    (128, 66, -1),  # potentille-pommier
    (139, 73, 1),  # lavande-rosier
    (139, 140, 1),  # lavande-agrumes
    (139, 118, -3),  # lavande-fourmis
    (139, 41, -3),  # lavande-pucerons
    (139, 33, -1),  # lavande-mélisse
    (56, 39, -3),  # absinthe-limaces
    (56, 40, -3),  # absinthe-altises
    (6, 40, -3),  # tomate-altises
    (151, 40, -3),  # sureau-altises
    (54, 40, -3),  # romarin-altises
    (20, 40, -3),  # laitue-altises
    (79, 41, -3),  # capucine-pucerons
    (63, 41, -3),  # cresson-pucerons
    (139, 41, -3),  # lavande-pucerons
    (35, 41, -3),  # trèfle blanc-pucerons
    (38, 41, -3),  # oeillets d'inde-pucerons
    (116, 69, -2),  # campagnols-chicorée
    (116, 70, -2),  # campagnols-pissenlit
    (1, 116, -2),  # campagnols-carotte
    (5, 116, -2),  # campagnols-panais
    (3, 116, -3),  # ail-campagnols
    (152, 116, -3),  # narcisse-campagnols
    (154, 116, -3),  # buis-campagnols
    (155, 116, -3),  # noyer-campagnols
    (153, 116, -3),  # mélilot-campagnols
    (139, 118, -3),  # lavande-fourmis
    (156, 118, -3),  # marjolaine-fourmis
    (34, 118, -3),  # tanaisie-fourmis
    (151, 118, -3),  # sureau-fourmis
    (6, 118, -3),  # tomates-fourmis
    (153, 110, 2),  # mélilot-syrphes
    (156, 52, 1),  # marjolaine-piment
    (156, 52, 1),  # marjolaine-piment
    (109, 41, -3),  # araignées-pucerons
    (110, 41, -3),  # syrphes-pucerons
    (150, 41, -3),  # chrysopes-pucerons
    (53, 1, 1),  # lin-carotte
    (53, 20, 1),  # lin-laitue
    (104, 110, 2),  # sarrasin-syrphes
    (104, 111, 2),  # sarrasin-papillons
    (124, 41, 2),  # orme-pucerons
    (125, 45, 2),  # fusain-coccinelles
    (125, 150, 2),  # fusain-chrysopes
    (130, 66, -1),  # baguenaudier-pommier
    (131, 45, 2),  # genévrier-coccinelles
    (143, 142, -1),  # laurier-sauce-vigne
    (143, 26, 1),  # laurier-sauce-persil
    (143, 29, -1),  # laurier-sauce-cerfeuil
    (151, 116, -3),  # sureau-campagnols
    (155, 6, -1),  # noyer-tomate
    (155, 137, -1),  # noyer-cassis
    (155, 60, -1),  # noyer-choux
    (155, 158, -1),  # noyer-rhubarbe
    (155, 12, -1),  # noyer-pomme de terre
    (155, 110, 2),  # noyer-syrphes
    (157, 110, 2),  # noisetier-syrphes
    (159, 145, 2),  # ortie-punaises
    (159, 45, 2),  # ortie-coccinelles
    (159, 46, 2),  # ortie-carabes
    (66, 41, -2),  # pucerons-pommiers
    (73, 41, -2),  # pucerons-rosiers
    (60, 40, -2),  # altises-choux
    (14, 40, -2),  # altises-chou fleur
    (15, 40, -2),  # altises-chou rave
    (16, 40, -2),  # altises-chou rouge
    (21, 40, -2),  # altises-radis
    (107, 40, -2),  # altises-navet
    (31, 40, -2),  # altises-moutarde
    (24, 42, -2),  # nematodes-fraisier
    (62, 42, -2),  # nematodes-artichaut
    (1, 42, -2),  # nematodes-carotte
    (7, 42, -2),  # nematodes-pois
    (78, 42, -2),  # nematodes-epinard
    (18, 42, -2),  # nematodes-betterave
    (60, 42, -2),  # nematodes-
    (14, 42, -2),  # nematodes-
    (15, 42, -2),  # nematodes-
    (16, 42, -2),  # nematodes-
    (12, 90, -2),  # doryphores-pomme de terre
    (46, 138, -2),  # carabe-limaces
    (109, 41, -2),  # araignee-pucerons
    (110, 41, -2),  # araignee-pucerons
    (6, 160, -3),  # tomate-mouche de la carotte
    (2, 160, -3),  # poireau-mouche de la carotte
    (1, 160, -2)  # carotte - mouche de la carotte
]
