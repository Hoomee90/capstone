# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define template = Character('',
    ctc="ctc",    
    ctc_pause="ctc",
    ctc_position="nestled",)

define k = Character('Kotone',
    kind=template,
    color="#6c8d67",
    who_outlines=[ (2, "#233525") ])

define s = Character('Suki',
    kind=template,
    color="#1ca692",
    who_outlines=[ (2, "#0b4c45") ])

define n = Character('',
    kind=template)

image ctc:
    "gui/arrow.png"
    linear 0.5 alpha 1.0
    linear 0.5 alpha 0.0
    repeat 

transform bounce:
    pause .1
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0

transform slide_to_left:
    easein 0.4 xalign 0.3

transform fade_in_right:
    xalign 0.7
    alpha 0.0
    linear 0.4 alpha 1.0

transform slide_right_to_center:
    easein 0.4 xalign 0.5

label start:

    n "My master is strange."
    scene bg selectionroom with fade
    show kotone neutral
    n "The first thing I notice is how I tower over her.{w} I've always been tall, but she's {i}tiny{/i}."
    n "Her posture, too. Contorted even smaller, she's a circus act of avoiding attention."
    show kotone look
    n "The second thing I notice is that she actually looks my way."
    n "There's an open curiosity there, contrast to every woman who's eyed me before—{w}this selection or the previous."
    show kotone submissive at slide_to_left
    show veterangroup at fade_in_right, bounce
    n "{i}Abomination.{/i}"
    show veterangroup at bounce
    extend "{i} Akane's afterbirth.{/i}"
    show veterangroup at bounce
    extend "{i} Double-cursed thing.{/i}"

    hide kotone with dissolve
    show veterangroup at slide_right_to_center
    n "Magical girls don't mix with human children, or at least human girls.{w} Inter Office compact:{w} no spilling secrets, no influencing magic."
    n "But I had always been the exception.{w} Pity, on me or my mother, backed up by confidence in the facts."
    show veterangroup at bounce
    n "{i}Products of magic can't be given magical girl status.{/i}"
    show veterangroup at bounce
    extend "{i} Fairies won't even register them as human.{/i}"

    n "Except fairies get stranger every year.{w} Contact with humanity makes them ill.{w} I grew up hearing stories."
    n "I grew up hearing everything."
    n "I should've known, then, that nobody would want me.{w} That nobody liked a know-it-all, and nobody cared for my mother enough to be charmed by how similar I look."
    n "But at the time what had matter was this:{w} my mother was dead, and the pity was quickly drying up."
    n "Out on the street or off with my head—but a fairy came to me that night.{w} There was only one way forward."
    n "One winnowing, two. I am a dead girl walking. I always have been."
    hide veterangroup with dissolve
    show kotone look with dissolve
    n "Until this woman, mousy and timorous. Until her."
    show kotone speak
    k "My name is Kotone.{w} I'm choosing you."
    s "I—{w}"
    n "I stop. I don't actually have anything to say."
    s "Okay."
    n "Pointless word.{w} Pointless nod."
    n "She doesn't grasp my arm or my face, doesn't go to check if my teeth are all intact.{w} I only get one more sentence before she's turned away."
    k "You don't see many flowers offworld."
    n "She must mean the cluster of snapdragons on the lapel of my three-piece suit.{w} She moves quick, and I find myself feeling strangely sick we leave this place behind."
    n "Out of the fire, into the frying pan."
    s "{i}Hey mom... was this what it was like for you?{/i}"

    scene bg koquarters
    with fade

    n "My master spends my first week studiously ignoring me.{w} I'm relegated to the corners of rooms, afterthought, unloved doll. Her fellow magical girls seem keen to do the same." 
    n "It's not unfamiliar. There had only ever been one person who wanted to hear me speak."
    n "Without a proper education, my elocution is subpar.{w} Mine are the awkward syllables and stunted vocabulary of a tongue built from propaganda pieces and eavesdropped mess hall gossip."
    n "When I try, my words fall as a disordered mess. Too fast, too emphatic."
    n "Friends or peers to converse with freely have never existed for me."
    n "So it comes to a shock when, out of the blue, my master addresses me."
    show kotone speak
    k "Have you been settling in okay?"

    return