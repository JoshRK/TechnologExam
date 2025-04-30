from database import collection_vinyles, collection_dvds

collection_vinyles.delete_many({})
collection_dvds.delete_many({})

collection_vinyles.insert_many([
    {
        "titre": "Beat Street",
        "artiste": "Bob Marley",
        "immatriculation": "BM/180/POP/1234"
    },
    {
        "titre": "Flow Supreme",
        "artiste": "Freddie Mercury",
        "immatriculation": "FM/240/RAP/2357"
    }
])

collection_dvds.insert_one({
    "titre": "Silk Sounds",
    "artiste": "Alicia Keys",
    "immatriculation": "AK/210/RNB/4589"
})

print("Base de données initialisée.")
