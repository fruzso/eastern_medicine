label hospital:
    # A memmory of the Hospital
    # PLOTPOINTS: We learn about the stolen blood and the PC's relation to Cecila

    scene backgorund_video_hospital
    with Dissolve(3.0)

    "/The memory of St. Margit's hospital comes back, maybe even more clearly than you would like/"

    with Pause(3.0)

    show pc idle at right
    pc "The hospital was particulary quiet that evening."
    hide pc

    show janos idle at left
    janos "Were you a frequent visitor?"

    "/He fiddles around his notes./"

    "/But does not share his discoveries with you./"
    hide janos

    show pc idle at right
    pc "It seems that you already have the answer somewhere there, written down."
    hide pc

    show janos idle at left
    janos "I often find that a verbal account of the subject illuminates the salient points of the affair in comparision to which text simply pales."
    hide janos

    pc "illuminates the salient points..."

    return