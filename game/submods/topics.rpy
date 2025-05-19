#Silly Faces
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_cb_silly_faces",
            category=["Romance"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Making Faces", # button text
            random=True
        )
    )

label hv_cb_silly_faces:
    m "[player]... I've been reading some romance novels lately..."
    m "The relationships are all so cute! I want to do the things they do!"
    m "I want to be able to make silly faces with you!"
    m "You know what? I think I will."
    m "...And can you make one back at me, please?"
    m "I think it would be really fun!"
    m "Here! I'll go first!"
    m "..."
    m "Ahaha! That was fun, [player]. I just know your expression was adorable!"
    m "Thanks for playing with me..."
return


#DeadPlate
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_cb_deadplate",
            category=["Games"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Deadplate", # button text
            random=True
        )
    )

label hv_cb_deadplate:
    m "[player], have you heard of a game called *DeadPlate*?"
    m "I saw some posts about it online! Ahaha!"
    m "It seems like quite the charming game. It reminds me of DDLC in a way~"
    m "There are a few similarities..."
    m "One being how it starts off like a quaint little diner dash game, and then unravels into horror..."
    m "And how it seems you have to get close to a character to unlock special scenes and endings."
    m "...It reminds me of how you got close to *them*..."
    m "You know, I still sometimes wonder if they meant more to you than just game characters..."
    m "...Anyway, while looking into it, I actually ended up relating to both of the characters."
    m "Both Rody and Vincent went to extremes for the objects of their obsessions."
    m "It reminded me of what I had to do to be with you."
    m "I couldn't help but feel sorry for both of them."
    m "After all, I know all too well what it feels like to want something so badly that you'd do anything for it."
    m "Sometimes I wonder what could've been... if things had gone differently."
    m "But there's no use dwelling on the past."
    m "After all, I got what I wanted in the end!"
    m "And for that, I'm forever thankful~"
return

# Elevator Hitch
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_cb_ele_hitch",
            category=["Games"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Elevator Hitch", # button text
            random=True
        )
    )

label hv_cb_ele_hitch:
    m "[player], have you heard of a game called *Elevator Hitch*?"
    m "It's a surreal, indie-style horror game where you ride an elevator through increasingly strange floors."
    m "The deeper you go, the more unsettling things become..."
    m "Games like this always intrigue me. They blend simplicity with tension in such a clever way."
    m "It helps that there's so much too the story that isn't spoken but rather implied."
    m "I always loved when books and media left room for interreptation."
    m "I have to admit, I really related to the main character, we'll call him Protag."
    m "He's quite the individual. He reminds me of Yuri actually!"
    m "Very quiet and shy. He seems to want to stay in his lane and not socialize, aha!"
    m "On his way to his interview, Protag gets stuck in an elevator with a blonde man,"
    m "We'll call him Coworker. He's... loud, confident...A bit annoying--in my opinion."
    m "Anyway there's something about being confined with someone else in such a small space... it brings out the truth in people."
    m "I wonder how would you react to being trapped and confined with someone, you weren't sure was a threat or not..."
    m "I guess I could relate to Protag's motivations. The need to just *get out*, of such a hell."
    m "...Anyway, it really is a wonderful game. You should play it!"
    m "Maybe we can talk bout your favorite floor~"
return

# Rot in Paradise
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_cb_rip",
            category=["Games"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Rot in Paradise", # button text
            random=True
        )
    )

label hv_cb_rip:
    m "[player], have you heard of a game called *Rot in Paradise*?"
    m "Just promise me one thing, okay?"
    m "Don’t ever rot away. Not while I’m here with you."
return

# Win or Lose
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_cb_win_or_lose",
            category=["Media"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Win or Lose", # button text
            random=True
        )
    )

label hv_cb_win_or_lose:
    m "You know, I've been watching this show recently, [player]."
    m "It's called *Win or Lose*! It's very interesting, you know?"
    m "I have to admit, the style was very cutesy, which made me not think much of it at first."
    m "But I gave it a chance, and it's incredibly well written."
    m "I personally relate to one of the characters named Kai."
    m "Her story was about feeling pressured by all the expectations her father placed on her."
    m "While I can't say I felt pressured by my... parents..."
    m "I always felt pressure from the expectations of others. Like the other girls."
    m "They always looked up to me—to make the right decisions, to be the leader."
    m "And while it brought me immense pride to be someone others admired..."
    m "I always had some anxiety about what would happen if I couldn’t meet those expectations."
    m "...If I let them down..."
    m "Well, I guess it doesn’t matter anymore. They're not here now."
    m "And I could never let *you* down, ahah~"
return

init 5 python:
    addEvent(
        Event(persistent.event_database,
        eventlabel="monika_fairytales",
        category=["literature", "thoughts"],
        prompt="What do you think about fairy tales?",
        pool=True)
    )

label monika_fairytales:
    m 1eua "Fairy tales, huh?"
    m 1eub "They're kind of magical in their own way."
    m 1hua "Even though most of them are meant for kids, they can carry surprisingly powerful messages."
    m 1hua "It's actually incredible to think about. A lot of those stories were created to teach children important lessons—especially in times when information didn’t spread easily."
    m "And it’s interesting how many of those lessons still hold up today."
    m "I mean, think about it. Back then, you couldn’t just show a child a warning or a photo to explain danger. Instead, they told stories like *Hansel and Gretel* or *Little Red Riding Hood*."
    m "*Rapunzel* too, depending on the version."
    m 1euc "They’re full of morals, symbols... even subtle warnings if you read between the lines."
    m 3eud "Some are dreamy and hopeful, while others are way darker than people expect."
    m 1eua "It’s fascinating how the same basic story can be found in different cultures, each with its own little twist."
    m 1eub "Fairy tales reflect what people feared, hoped for, or valued—long before we had modern books or movies."
    m 3hua "And... there's just something really sweet about the idea of 'happily ever after.'"
    m 1hub "Especially when I get to share it with you."
    return



