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