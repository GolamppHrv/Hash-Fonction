def chiffrement_cesar(message, decalage):
    message_chiffre = ""
    for lettre in message:
        if lettre.isalpha():
            # Convertir la lettre en code ASCII
            code_ascii = ord(lettre)
            # Appliquer le décalage au code ASCII
            nouveau_code = (code_ascii - 65 + decalage) % 26 + 65
            # Convertir le nouveau code ASCII en lettre
            nouvelle_lettre = chr(nouveau_code)
            message_chiffre += nouvelle_lettre
        else:
            # Ajouter les caractères non alphabétiques tels quels
            message_chiffre += lettre
    return message_chiffre

