#!/bin/usr/python3
import mysql.connector


def main():
    mydb = mysql.connector.connect(
        host="localhost",
        user="DamienQ",
        passwd="Suikenmaster.26",
        database="Geokeys",
    )
    mycursor = mydb.cursor()
    id_cle = (input("Saisir id de la clé à déplacer : "),)
    while True:

        print(
            "\nTapez Z pour monter \nTapez S pour descendre \nTapez Q pour aller à gauche\n"
            "Tapez D pour aller à droite\n Tapez X pour quitter")
        saisie = str.lower(input("Entrée :"))
        if saisie == "z":
            modifier_position_haut(mydb, mycursor, id_cle)
        if saisie == "q":
            modifier_position_gauche(mydb, mycursor, id_cle)
        if saisie == "s":
            modifier_position_bas(mydb, mycursor, id_cle)
        if saisie == "d":
            modifier_position_droite(mydb, mycursor, id_cle)
        if saisie == "X":
            break

        elif saisie != "z" and saisie != "q" and saisie != "s" and saisie != "d" and saisie != "x":
            print("Saisie invalide !")
    return mycursor, mydb, id_cle


def modifier_position_droite(mydb, mycursor, id_cle):

    # On selectionne la latitude présente dans la BDD en ciblant avec l'id de la clé
    sql = "SELECT Latitude FROM Cles WHERE id = %s;"
    val = id_cle
    mycursor.execute(sql, val)  # require a tuple == ( xx , )
    for x in mycursor:
        print(x[0])
        latitude = x[0]  # On extrait la latitude dans une variable

    # On incremente la valeur de la latitude
    sql_2 = "UPDATE Cles SET Latitude = %s WHERE id = %s;"
    latitude += 0.001
    val_2 = (latitude, val[0])
    mycursor.execute(sql_2, val_2)
    mydb.commit()
    print("+1 en latitude")
    for x in mycursor:
        print(x[0])


def modifier_position_gauche(mydb, mycursor, id_cle):
    # On selectionne la latitude présente dans la BDD en ciblant avec l'id de la clé
    sql = "SELECT Latitude FROM Cles WHERE id = %s;"
    val = id_cle
    mycursor.execute(sql, val)  # require a tuple == ( xx , )
    for x in mycursor:
        print(x[0])
        latitude = x[0]  # On extrait la latitude dans une variable

    # On décremente la valeur de la latitude
    sql_2 = "UPDATE Cles SET Latitude = %s WHERE id = %s;"
    latitude -= 0.001
    val_2 = (latitude, val[0])
    mycursor.execute(sql_2, val_2)
    mydb.commit()
    print("-1 en latitude")


def modifier_position_haut(mydb, mycursor, id_cle):
    # On selectionne la longitude présente dans la BDD en ciblant avec l'id de la clé
    sql = "SELECT Longitude FROM Cles WHERE id = %s;"
    val = id_cle
    mycursor.execute(sql, val)  # require a tuple == ( xx , )
    for x in mycursor:
        print(x[0])
        longitude = x[0]  # On extrait la longitude dans une variable

    # On incremente la valeur de la longitude
    sql_2 = "UPDATE Cles SET Longitude = %s WHERE id = %s;"
    longitude += 0.001
    val_2 = (longitude, val[0])
    mycursor.execute(sql_2, val_2)
    mydb.commit()
    print("+1 en longitude")


def modifier_position_bas(mydb, mycursor, id_cle):
    # On selectionne la longitude présente dans la BDD en ciblant avec l'id de la clé
    sql = "SELECT Longitude FROM Cles WHERE id = %s;"
    val = id_cle
    mycursor.execute(sql, val)  # require a tuple == ( xx , )
    for x in mycursor:
        print(x[0])
        longitude = x[0]  # On extrait la latitude dans une variable

    # On décremente la valeur de la longitude
    sql_2 = "UPDATE Cles SET Longitude = %s WHERE id = %s;"
    longitude -= 0.001
    val_2 = (longitude, val[0])
    mycursor.execute(sql_2, val_2)
    mydb.commit()
    print("-1 en longitude")


main()
