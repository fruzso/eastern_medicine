label  rakpart:
    # Start scenne
    # Janos enters and ponders the crimes of the PC

    play music background_music_rakpart volume 0.5 loop

    $ renpy.pause(2.0)

    scene background_video_rakpart
    with Dissolve(3.0)

    $ renpy.pause(2.0)

    show janos idle at left
    with Dissolve(2.0)

    # These display lines of dialogue.
<<<<<<< HEAD
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
=======

    janos "Work. Work never ends. Not for the living and certainly not for the everlasting."

    janos "Nor for the undying, whatever you will call us."

    janos "Nevertheless, not the worst of places to suffer, through."

    janos "Not much everylasting waits us, if a few imps come knocking on the door come daylight."

    janos "But who set them on us? - there's the rub!"

    # TODO: queue footstep sound here
    "Footsteps approach in the mist, thumping the ground with a growing determination of volume."

    $ renpy.pause(2.0)

    janos "To work, then!"

    janos "Who comes here?"

    return
>>>>>>> FIX-0001 Brought back all the dialog and wrote some more.
