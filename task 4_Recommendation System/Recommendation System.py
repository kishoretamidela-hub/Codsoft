import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

music_data = {
    "Song": [
        "Shape of You",
        "Perfect",
        "Believer",
        "Thunder",
        "Radioactive",
        "Blinding Lights",
        "Starboy",
        "Levitating",
        "Bad Habits",
        "Closer",
        "Faded",
        "Alone",
        "On My Way",
        "Hymn for the Weekend",
        "Paradise"
    ],

    "Artist": [
        "Ed Sheeran",
        "Ed Sheeran",
        "Imagine Dragons",
        "Imagine Dragons",
        "Imagine Dragons",
        "The Weeknd",
        "The Weeknd",
        "Dua Lipa",
        "Ed Sheeran",
        "Chainsmokers",
        "Alan Walker",
        "Alan Walker",
        "Alan Walker",
        "Coldplay",
        "Coldplay"
    ],

    "Genre": [
        "Pop",
        "Pop",
        "Rock",
        "Rock",
        "Rock",
        "Pop",
        "Pop",
        "Pop",
        "Pop",
        "EDM",
        "EDM",
        "EDM",
        "EDM",
        "Pop",
        "Pop"
    ],

    "Album": [
        "Divide",
        "Divide",
        "Evolve",
        "Evolve",
        "Night Visions",
        "After Hours",
        "Starboy",
        "Future Nostalgia",
        "Equals",
        "Collage",
        "Different World",
        "Different World",
        "Different World",
        "A Head Full of Dreams",
        "Mylo Xyloto"
    ]
}

df = pd.DataFrame(music_data)

df["Features"] = (
    df["Artist"] + " " +
    df["Genre"] + " " +
    df["Album"]
)

vectorizer = TfidfVectorizer(stop_words="english")
feature_matrix = vectorizer.fit_transform(df["Features"])

similarity = cosine_similarity(feature_matrix)

def recommend(song_name):

    if song_name not in df["Song"].values:
        print("\nSong not found.")
        return

    index = df[df["Song"] == song_name].index[0]

    similarity_scores = list(enumerate(similarity[index]))

    sorted_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print("\nRecommended Songs\n")

    count = 0

    for i in sorted_scores:

        song_index = i[0]

        if song_index == index:
            continue

        print("--------------------------------")
        print("Song   :", df.iloc[song_index]["Song"])
        print("Artist :", df.iloc[song_index]["Artist"])
        print("Genre  :", df.iloc[song_index]["Genre"])
        print("Album  :", df.iloc[song_index]["Album"])
        print("--------------------------------")

        count += 1

        if count == 5:
            break

print("=" * 40)
print("      MUSIC RECOMMENDATION")
print("=" * 40)

print("\nAvailable Songs\n")

for i in df["Song"]:
    print("-", i)

print()

song = input("Enter Song Name : ")

recommend(song)

print("\nThank You!")