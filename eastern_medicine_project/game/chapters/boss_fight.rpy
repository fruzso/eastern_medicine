label fight_pc_start:  
    # Outside pc started fights come here
    # play music background_music_run_and_fight volume 0.5 loop
    $ renpy.music.play(audio.background_music_run_and_bossfight, relative_volume=1.0, loop=True, if_changed=True)

    menu:
        "He might not think I have the audacity to strike an annointed sheriff."
        "Strike him {image=dice}":
            call pc_hits_1
            call janos_hits_1 # calls fight interlude 1 or defeat

        "Confuse his mind {image=dice}" if pc_sheet.DOMINATE >= 2 and pc_sheet.OBFUSCATE >= 2:
            call dementation # Or call Victory
            call pc_hits_1
            call janos_hits_1  # calls fight interlude 1 or defeat

label pc_hits_1:
    centered "You try to get a jump on him. {image=dice}"

    # Roll fight
    $ roll_janos = Roll(janos_sheet.DEXTERITY + janos_sheet.BRAWL, janos_sheet.hunger, difficulty=0)
    $ roll_janos.roll()
    $ roll_pc = Roll(pc_sheet.DEXTERITY + pc_sheet.BRAWL, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
    $ roll_pc.roll()

    if roll_pc.is_success:
        centered """Your muscles cleverly obey your command as courses through your nervous system,
        
        manifests in powerful blow
        
        and connects with Janos' already disfigured face."""

        $ janos_sheet.lose_health(roll_pc.margin_of_success)
        call check_janos_alive

    else:
        show pc idle at right
        pc "Shit!"
        hide pc

        centered "He evades your attack, looking fierce and out for blood."  
    return
    
label dementation:
    # Rousecheck
    if not pc_sheet.rouse_check():
        call change_dynamic_stats("worse")

    # Roll Dementation
    $ roll_janos = Roll(janos_sheet.INTELLIGENCE + janos_sheet.COMPOSURE, janos_sheet.hunger, difficulty=0)
    $ roll_janos.roll()
    $ roll_pc = Roll(pc_sheet.MANIPULATION + pc_sheet.DOMINATE, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
    $ roll_pc.roll()

    if roll_pc.is_success:
        show pc idle at right
        pc """Quite a sheriff you are. Ventured as far as the basement of the most famous building in the city.

        You didn't know what you will find.

        I guess you already presented to the prince that you know ALL about what happend.

        And now, having listened to my account, you haven't got the foggiest."""
        hide pc

        centered "You see rage building up in the nosferatu."

        centered "You are hitting the right spots, just need to apply a bit mor epressure."

        show pc idle at right
        pc """
        Trapped in a time you don't really understand. With a language most jsut despise.

        Serving as the tzimische's lapdog. And nothing more.
        """
        hide pc

        show janos idle at right
        janos "Stop. You have no idea what you are talking about."
        hide janos

        centered "You know this is just a feeble attempt to shield his mind."

        show pc idle at right
        pc "You know how to stop this."
        hide pc

        centered "You get up and walk out of the door, leaving a petrified Janos behind."

        call victory

    else:
        show pc idle at right
        pc "Quite a sheriff you are. Ventured as far as the..."
        hide pc

        centered "He cuts you off mid-sentence."

        show janos idle at right
        janos "I am not gonna stand here and listen to your demented mind."
        hide janos

        return

label janos_hits_1:
    #play music background_music_run_and_fight volume 0.5 loop
    $ renpy.music.play(audio.background_music_run_and_bossfight, relative_volume=1.0, loop=True, if_changed=True)

    show janos idle at center
    centered """With incredible speed Janos launches forward,
    
    his claws, and fangs are out, and they are deadly as fuck. {image=dice}"""
    hide janos

    $ roll_janos = Roll(janos_sheet.DEXTERITY + janos_sheet.BRAWL + janos_sheet.CELERITY, janos_sheet.hunger, difficulty=0)
    $ roll_janos.roll()
    $ roll_pc = Roll(pc_sheet.DEXTERITY + pc_sheet.ATHLETICS + pc_sheet.CELERITY, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
    $ roll_pc.roll()

    if roll_pc.is_success:
        show pc idle at center
        centered """He is qucik

        But you are quciker.

        Your body flows around his in one fluid motion of aesthethics.

        And you take pleasure in knowing he's going to hit the wall.

        So it happens

        with a loud splash of supernatural tissue and vitae.
        """
        hide pc

        show janos idle at right
        janos "You will pay for this, little miscreant!"
        hide janos
        
        $ janos_sheet.lose_health(roll_pc.margin_of_success)
        call check_janos_alive

    else:
        centered """He is definitely quicker.

        No question about it.

        And you will have a nasty scar to testify to the fact.
        """
        $ pc_sheet.lose_health(abs(roll_pc.margin_of_success))
        call change_dynamic_stats("worse")

    call fight_interlude_1

label fight_interlude_1:
    $ age_difference = janos_sheet.AGE - pc_sheet.AGE
    show janos idle at right
    janos """Have you considered that it is utter foolishness what you are trying to accomplish here.
    
    I am [age_difference] years your elder.

    And the sheriff of this bloody town.

    There is no remotely beneficial outcome for you."""
    hide janos

    menu:
        "Yield":
            show pc idle at right
            pc """Stooop! 
            
            You are right, I cannot hope to achieve anything here."""
            hide pc

            show janos idle at right
            janos "I am glad you chose to see reason.
            
            This will be better for all parties concerned."
            hide janos

            centered """He steps closer
            
            and within the blink of an eye his fangs dig deep into your neck."""

            call violent_defeat

        "Fight on":
            centered "You choose to fight on."
            # Roll fight
            $ roll_janos = Roll(janos_sheet.DEXTERITY + janos_sheet.BRAWL, janos_sheet.hunger, difficulty=0)
            $ roll_janos.roll()
            $ roll_pc = Roll(pc_sheet.DEXTERITY + pc_sheet.BRAWL, pc_sheet.hunger, difficulty=roll_janos.margin_of_success)
            $ roll_pc.roll()

            if roll_pc.is_success:
                centered """Your muscles tense up as you try to tear through his body."""

                $ janos_sheet.lose_health(roll_pc.margin_of_success)
                call check_janos_alive

            else:
                show janos idle at right
                janos "You inisignificant idiot!"
                hide janos

                centered """He pulls a short wooden stake out from under his coat and stabs your leg with it.
                
                You clearly feel the destruction he brought upon you."""

                $ pc_sheet.lose_health(abs(roll_pc.margin_of_success))
                call change_dynamic_stats("worse")
    call closure

label closure:
    if pc_sheet.health > janos_sheet.health:
        centered """Against all his efforts you have a clever and tactical reply.
        
        He may be stronger and older, but his hubris blinds him.
        
        And you are always there to seize the opportunities, however small they be.
        """
        # PC wins
        $ janos_sheet.lose_health(janos_sheet.health) # Janos loses as his remaining health
        call check_janos_alive # calls victory always

    else:
        centered """For all your effort, the clever and tactical moves and everything you can bring to the table
        
        nothing seems to counter the fact that he is stroner and more importantly older than you.
       
        It was a mistake to fight him.
        
        A fatal one.
        """
        # Janos wins
        call violent_defeat 