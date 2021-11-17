# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define janos = Character("janos")

define audio.background_music_rakpart = "music/background_music_rakpart.mp3"

image background_video_rakpart = Movie(play = "video/movie_rakpart.webm", mask = None)
image background_video_black_wheel_empty = Movie(play = "moive_character_seelction_empty.webm"))



# The game starts here.

label start:
    # Start scenne
    # Janos enters and ponders the crimes of the PC
    # Show a background. This uses a placeholder by default, but you can

    play music background_music_rakpart volume 0.5 loop
    scene background_video_rakpart
    with Dissolve(3.0)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show janos idle

    # These display lines of dialogue.

    janos "Ominous shit"

    janos "Choose one"

    menu pick_a_drug:
        "Pick a drug, my darling PC!"
        "Now!"
        "I said, now"
        "Cocaine":
            "You choose cocaine"
            $ high_on_cocaine = True
        "Weed":
            "You choose weed"
            $ high_on_cocaine = False

    menu what_next:
        "What now"
        "lose money":
            "you lost money"
        "go to party" if high_on_cocaine:
            "Having FUUUUN"
          

    # This ends the game.

    return

label defeat_mid_interogation:
    # Game over

    scene background_video_black_wheel_empty
    with dissolve(3.0)

    "Janos grabs you swiftly"
    "His motions are too quick even for your eye to follow"
    "And the molecules of your bodym only boudn together by the Dark Fathers curse perpetuated through the ages begin to give."

    return



