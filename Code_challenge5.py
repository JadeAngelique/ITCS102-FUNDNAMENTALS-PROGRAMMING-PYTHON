print("Welcome to Manga Recommender")
print("Answer a few questions so that I can assist you in finding the right Manga for you")

genre = input("What's your preferred genre? (Romance, Drama, Adventure): ").lower()
length = input("What's your preferred length? (short, medium, long): ").lower()
decade = input("What's your preferred year? (2000s, 2010s): ").lower()

if genre == "romance":
    if length == "short":
        if decade == "2000s":
            print("Here are the top 5 suggestions:5 Centimeters per Second, Ef A Tale of Memories, Lovely Complex, REC, Hanbun no Tsuki ga Noboru Sora")
        elif decade == "2010s":
            print("Here are the top 5 suggestions:Tsuki ga Kirei, My Little Monster, Ao Haru Ride, Plastic Memories, Say I Love You")
    elif length == "medium":
        if decade == "2000s":
            print("Here are the top 5 suggestions:Lovely Complex, Honey and Clover, Nodame Cantabile, Clannad, Spice and Wolf")
        elif decade == "2010s":
            print("Here are the top 5 suggestions:Toradora, Golden Time, Your Lie in April, Nagi no Asukara, Chuunibyou demo Koi ga Shitai")
    elif length == "long":
        if decade == "2000s":
            print("Here are the top 5 suggestions:True Tears, Fruits Basket, School Rumble, Ai Yori Aoshi, Initial D")
        elif decade == "2010s":
            print("Here are the top 5 suggestions:White Album 2, Chihayafuru, Kamisama Kiss, Kaichou wa Maid Sama, Snow White with the Red Hair")

elif genre == "drama":
    if length == "short":
        if decade == "2000s":
            print("Here are the top 5 suggestions:Ergo Proxy, Paranoia Agent, Mushishi, Texhnolyze, Ghost Hunt")
        elif decade == "2010s":
            print("AHere are the top 5 suggestions:nohana The Flower We Saw That Day, Mawaru Penguindrum, Usagi Drop, Barakamon, Shigatsu wa Kimi no Uso")
    elif length == "medium":
        if decade == "2000s":
            print("Here are the top 5 suggestions:Paranoia Agent, Mushishi, Serial Experiments Lain, RahXephon, Ergo Proxy")
        elif decade == "2010s":
            print("Here are the top 5 suggestions:Psycho Pass, Steins Gate, Kids on the Slope, Nagi no Asukara, The Tatami Galaxy")
    elif length == "long":
        if decade == "2000s":
            print("Here are the top 5 suggestions:Monster, Code Geass, Fullmetal Alchemist Brotherhood, Bleach, Death Note")
        elif decade == "2010s":
            print("Here are the top 5 suggestions:Attack on Titan, Psycho Pass 2, JoJo Bizarre Adventure, Hunter x Hunter 2011, Black Bullet")

elif genre == "adventure":
    if length == "short":
        if decade == "2000s":
            print("Samurai Champloo, Wolfs Rain, Berserk (1997 2000s continuation), Kinos Journey, Scrapped Princess")
        elif decade == "2010s":
            print("Here are the top 5 suggestions:Made in Abyss, The Girl Who Leapt Through Time, Erased, Children of the Whales, Katanagatari")
    elif length == "medium":
        if decade == "2000s":
            print("Here are the top 5 suggestions:Fullmetal Alchemist, Naruto Shippuden, Witch Hunter Robin, Wolfs Rain, Trinity Blood")
        elif decade == "2010s":
            print("Here are the top 5 suggestions:Magi The Kingdom of Magic, Attack on Titan, Noragami, Log Horizon, Sword Art Online II")
    elif length == "long":
        if decade == "2000s":
            print("Here are the top 5 suggestions:One Piece, Naruto, Bleach, Hunter x Hunter, Fairy Tail")
        elif decade == "2010s":
            print("Here are the top 5 suggestions:Sword Art Online, Attack on Titan, One Piece (continued), Fairy Tail (continued), Black Clover")

else:
    print("Sorry, genre not recognized. Please choose from Romance, Drama, or Adventure.")



