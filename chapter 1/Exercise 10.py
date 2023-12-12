#Dictionary  containing films details
films =[
    {
        "Title": "Avengers: Endgame",
        "Director": "Anthony Russo Joe Russo" ,
        "year": "2019",
        "Genre": "Action/sci-fi",
        "Rating": "4.7"
    },

    {
        "Title": "Titanic",
        "Director": "James Cameron" ,
        "year": "1997",
        "Genre": "Drama/Meldodrama",
        "Rating": "4.7"
    }
]

#loop to display films details 
for film in films:
    print ("Film Details:")
    for key, value in film.items():
        print(f"{key}: {value}")
        print("\n")