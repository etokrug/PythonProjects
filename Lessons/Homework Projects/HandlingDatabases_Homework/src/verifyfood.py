import mysql.connector
from database import login_info

db = mysql.connector.Connect(**login_info)
cursor = db.cursor()

cursor.execute("select id from animal")
animalIds = set()
for animalId in cursor.fetchall():
    animalIds.add(animalId[0])

cursor.execute("select anid from food")
foodIds = set()
for foodId in cursor.fetchall():
    foodIds.add(foodId[0])

if animalIds == foodIds:
    print("Every animal has a food choice")
elif not animalIds.issuperset(foodIds):
    print("""There are more animals that have food than exist.
    Please check your animal lists and update or correct them.""")
else:
    hungryAnimals = animalIds.difference(foodIds)
    hungryIdList = []
    hungryList = []
    for hungryAnimalId in hungryAnimals:
        hungryIdList.append(hungryAnimalId)
    for hungryAnimalId in hungryIdList:
        cursor.execute("select name, family from animal where id={0};".format(hungryAnimalId))
        hungryName = cursor.fetchall()[0]
        hungryList.append(hungryName)
    for animal in hungryList:
        name, family = animal
        print(name, " the ", family, " is hungry, please provide a food in the database that they eat.")  