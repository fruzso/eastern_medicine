label interogation_1:
    # The main scene of the game, where the player returns many times
    # PLOTPOINTS: 

    scene black
    with fade

    #TODO:AUDIO add interogation opening sounds, footsteps, door

    pause(10.0) #TODO:AUDIO correct the pause time to fit the music, or make it that the next action only happens once the sound finished

    scene background_video_interogation
    with Dissolve(3.0)

    pause(3.0)

    show janos idle at left

    janos "Take a seat!"

    "/You take the only chair singled out in the middle of the damp room./"

    hide janos

    menu seating_choice:

        "Sit down":
            $ pc_seated = True

            show pc idle at right

            pc "Well, if this is the best the house can offer, I don't mind if I do."

            "/You sit down and take your time to adjust in the chair/"

            pc "Never mind the squeks and the wait."

            hide pc

            show Janos idle at left

            janos "Are you sitting comfortably?"

            hide janos

            show pc idle at right

            pc "You could say that."

            hide pc

        "Remain standing":
            $ pc_seated = False

            show pc idle

            pc "Thanks, but no thanks. I prefere to stand."

            "/You remain standing./"
            
            show janos idle at left

            janos "Suit yourself. But we are going to be here for some time."
    
    if not pc_seated:
        show janos idle at left

    janos "Let's begin. Shall we?!"

    show pc idle at right

    pc "By all means. We don't wanna' be here all night, do we?"

    hide pc

    show janos idle at left

    janos "The young are always so hasty, and trouble follows posthaste"

    hide janos

    show pc idle at right

    pc "Where the fuck did you learn to speak?"

    hide janos

    show pc idle at right

    janos """
    When would reveal a bit more, perhaps. Yet again, you are not here to ask questions.

    Not the smart ones anyway.
    """

    hide janos

    show pc idle at right

    pc "Have we started on the tourture yet?"

    hide pc

    show janos idle at left

    janos """
    You would know, I assure you. In any case there is a point to your persistence.
    
    Where were you on the 20th of August?
    """

    hide janos

    menu august_20:
        "Tell a lie":
            #TODO:AUDIO que in fireworks

            show pc idle at right

            pc """
            It was a particulary bright evening, I remember it well.
            
            I was atop a corporate tower - forgive me, I forget which money-hungry conglomerate was it this time.
            
            But I tell you something, you cannot beat the view these fat cats afford their peons.
            
            There I was, taking in the night sky, and the sparkling dimonds on it.
            """
            
            hide pc

            show janos idle at left

            janos "Knowing your kind, I am surprised that you do not put in a word for a national holiday every day."

            hide janos

            show pc idle at right
            
            pc "What a dismal idea. Nothing could devalue the experience anymore."

            hide pc

        "Tell the truth":

            show pc idle at right

            pc "I was in the hospital."

            hide pc

            show janos idle at left

            janos "The hospital?"

            hide janos
        
            show pc idle at right

            pc "I didn't go there to see the doctor."

            hide pc

            show janos idle at left

            janos "But you did go there to see someone!"

            hide janos

            show pc idle at right

            pc "yes."

            hide pc

            return