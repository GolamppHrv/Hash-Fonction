<?php

// saisi des donnees a hacher
    $donnee=readHach('saisissez la valeur a hacher : ');

//creation de la fonction d'hachage
function hachage($donnee) {
       $hache = hash('sha256', $donnee);
       return $hache;
    }


$DonneeHachee = hachage($donnee);
 echo "valeur : " . $donnee .PHP_EOL;     
echo "Hachage : " . $DonneeHachee;

//creation de la fonction pour entreer les donnees
function readHach($valeur){
    $entree=readline($valeur);
    readline_add_history($entree);
    return $entree;
}




