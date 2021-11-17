# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define janos = Character("janos")

define audio.background_music_rakpart = "music/background_music_rakpart.mp3"

image background_video_rakpart = Movie(play = "video/movie_rakpart.webm", mask = None)
image background_video_black_wheel_filled = Movie(play = "video/movie_character_selection_filled.webm")
image background_video_black_wheel_empty = Movie(play = "video/moive_character_seelction_empty.webm", mask = None)



# The game starts here.
label start:
    # This is the selection of the entire game, where every scene connects and is callled

    call rakpart_begining

    call character_selection

    call defeat_mid_interogation

    return


label  rakpart_begining:
    # Start scenne
    # Janos enters and ponders the crimes of the PC
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

    return

label character_selection:
    # Rakpart darkness
    # PLOTPOINTS: Character selction and customization

    scene background_video_black_wheel_filled
    with Dissolve(3.0)

    menu choose_character:
        "Choose your character"
        "Almos":
            "something"
            python:
                import character_creation
                character_creation.something()
            #block of code to run
        "Cayanne":
            "something2"
            #block of code to run

    return
        

label hospital:
    # A memmory of the Hospital
    # PLOTPOINTS: We learn about the stolen blood and the PC's relation to Cecila

    return

label heaven:
    # A memory of the PC's heaven
    # PLOTPOINTS: Fight with the S.I. Agents

    return

label carpark:
    # A memory of the Carpark
    # PLOTPOINTS: the mentors letter

    return
    
label defeat_mid_interogation:
    # Game over

    scene background_video_black_wheel_empty
    with dissolve(3.0) #TODO for some reasion this here is not callable

    centered "Janos grabs you swiftly"
    "His motions are too quick even for your eye to follow"
    "And the molecules of your bodym only boudn together by the Dark Fathers curse perpetuated through the ages begin to give."
    
    # This ends the game.
    return