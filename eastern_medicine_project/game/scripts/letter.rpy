screen letter(choice):
    # letter image
    add "images/letter.png" yalign 0.5 xalign 0.5

    # text
    vbox xsize 900 ysize 600 yalign 0.55 xalign 0.5:
        text "My darling fellow fiend," color "#000000ff" 
        text "I am afraid this letter will find you in dire distress, yet its principal purpose is to assure you that you no longer have to shiver for your safetz. Our fahters’ blood has protected you for more than a century now and the rest is about to become easier and easier. " color "#000000ff" 
        text "As you kids say: XOXO" color "#000000ff" 
        text "And remember: we are attractive but we may just repel some. " color "#000000ff"
    
    # Buttons
    textbutton "BACK" xalign 0.5 yalign 0.9:
        text_size 40
        text_color "#FFFFFF"
        text_hover_color "#3230bb"
        action Jump(choice)


