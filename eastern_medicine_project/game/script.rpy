# The Main script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define janos = Character("Janos")
define cecila = Character("Cecilia") # not used yet
define agent = Character("Agent") # not used yet

# Audio
define audio.background_music_rakpart = "music/background_music_rakpart.mp3"
define audio.background_music_interrogation = "music/background_music_interrogation.mp3"
define audio.background_music_hospital = "music/background_music_hospital.mp3"
# TODO:AUDIO car scene
define audio.background_music_haven1 = "music/background_music_haven_1.mp3"
define audio.background_music_haven2 = "music/background_music_haven_2.mp3"
define audio.background_music_haven = "music/background_music_haven_possible.mp3"
define audio.background_music_victory = "music/background_music_victory.mp3"


# dialogue settings
define gui.dialogue_xpos = 250
define gui.dialogue_ypos = 125

# namebox settings
define gui.name_xalign = 0.5
define gui.name_yalign = 0.5
define gui.name_xpos = 250
define gui.name_ypos = 10
define gui.namebox_width = 300
define gui.namebox_height = 125

image background_video_rakpart = Movie(play = "video/movie_rakpart.webm", mask = None)
image background_video_interogation = Movie(play = "video/movie_interogation.webm", mask = None)
image background_video_black_wheel_filled = Movie(play = "video/movie_character_selection_filled.webm")
image background_video_black_wheel_empty = Movie(play = "video/moive_character_seelction_empty.webm", mask = None)
image backgorund_video_hospital = Movie(play = "video/movie_hospital.webm", mask = None)
image background_video_carpark = Movie(play = "video/movie_carpark.webm", mask = None)
image background_video_haven = Movie(play = "video/movie_haven.webm", mask = None)

# The game starts here.
label start:
    # This is the selection of the entire game, where every scene connects and is callled
    
    call variables # Non-story label
    # call test

    call rakpart

    call character_selection

    call interogation_1

    call hospital

    call interogation_2

    call haven

    call interogation_3

    call carpark

    call interogation_4

    call victory 

    call epilogue

    scene black
    with fade
    return    

label variables:
    # Only programatic content, nothing to show
    # Game mechanics:
    $ janos_strikes = 0

    # Story events:
    # False by default and only switched if chosen 
    $ story_selling_blood = False
    $ story_violent_arrival = False
    $ story_si_vision = False