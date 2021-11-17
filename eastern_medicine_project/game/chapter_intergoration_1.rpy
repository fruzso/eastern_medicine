label interogation_1:
    # The main scene of the game, where the player returns many times
    # PLOTPOINTS: 

    scene black
    with Dissolve(1.0)

    #TODO: add interogation opening sounds, footsteps, door

    $ renpy.pause(10.0) #TODO: correct the pause time to fit the music, or make it that the next action only happens once the sound finished

    scene background_video_interogation
    with Dissolve(3.0)

    $ renpy.pause(3.0)

    show janos idle at left

    janos "Take a seat!"

    "You the only chair singled out in the middle of the damp room"

    hide janos

    menu seating_choice:

        "Sit down":
            show pc idle at right

            pc "well, if this is the best the house can offer, I don't mind if I do."

            "You sit down and take your time to adjust in the chair"

            "Never mind the squeks and the wait."

        "Remain standing":
            show pc idle

            pc "Thanks, but no thanks. I prefere to stand."
            
            show janos idle

            janos "Suit yourself. But we are going to be here for some time."
    
    janos "Let's begin, shall we?!"

    pc "By all means. We don't wanna' be here all night, do we?"

    janos "The young are always so hasty, and trouble follows posthaste"

    pc "Where the fuck did you learn to speak?"

    janos "When would reveal a bit more, perhaps. Yet again, you are not here to ask questions."

    janos "Not the smart ones anyway."

    pc "Have we started on the tourture yet?"

    janos "You would know, I assure you. In any case there is a point to your persistence."

    janos "Where were you on the 20th of August?"

    menu august_20:
        "Tell a lie":
            pc "It was a particulary bright evening, I remember it well."
            pc "I was atop a corporate tower - forgive me, I forget which money-hungry conglomerate was it this time."
            pc "But I tell you something, you cannot beat the view these fat cats afford their peons." #TODO: que in fireworks
            pc "There I was, taking in the night sky, and the sparkling dimonds on it"
            janos "Knowing your kind, I am surprised that you do not put in a word for a national holiday every day."
            pc "What a dismal idea. Nothing could devalue the experience anymore."

        "Tell the truth":
            pc "I was in the hospital."
            janos "The hospital?"
            pc "I didn't go there to see the doctor."
            janos "But you did go there to see someone!"
            pc "yes."
            return