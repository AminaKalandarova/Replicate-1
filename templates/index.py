import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("C:\\Users\\amina\\Replicate-1\\song-dataset.csv", low_memory=False) [:10000]

df = df.drop_duplicates(subset="Song Name")

df = df.dropna(axis=0)

df = df.drop(df.columns[3:], axis=1)

df["Artist Name"]=df["Artist Name"].str.replace(" ","")

df["data"] = df.apply(lambda value: " ".join(value.astype("str")), axis=1)


vectorizer = CountVectorizer()
vectorized = vectorizer.fit_transform(df["data"])
similarities = cosine_similarity(vectorized)

df_tmp=pd.DataFrame(similarities, columns=df["Song Name"], index=df["Song Name"]).reset_index()

true = True
while true:
    print ("Get your top 10 recommended songs")
    print ("                             ")
    print ("This will generate the 10 songs from the database that are similar to the song you entered.")
    
    while True:
        input_song = input ("Please enter a name of the song you like: ")
        if input_song in df_tmp.columns:
            recommendation = df_tmp.nlargest(11, input_song)["Song Name"]
            break
            
        else:
            print("Sorry, this song is not in our database. Try another one!")
        
    print("Check out these songs: \n")
    for song in recommendation.values[1:]:
        print(song)
        
    print("\n")
    while True:
        next_command = input("Do you want to generate again for the next song? [yes, no] ")
        
    
        if next_command == "yes":
            break
            
        elif next_command == "no":
            true = False
            break
            
        else: 
            print("Please type 'yes' or 'no'")