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
    m "It may seem silly, but sharing little moments like this... it makes me feel closer to you."
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
    m "Sometimes I wonder... did they mean more to you than just game characters?"
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
    m "I always loved when books and media left room for interpretation."
    m "I have to admit, I really related to the main character, let's call him Protag."
    m "He's quite the individual. He reminds me of Yuri actually!"
    m "Very quiet and shy. He seems to want to stay in his lane and not socialize, aha!"
    m "On his way to his interview, Protag gets stuck in an elevator with a blonde man,"
    m "Let's call him Coworker. He's... loud, confident...A bit annoying--in my opinion."
    m "Anyway there's something about being confined with someone else in such a small space... it brings out the truth in people."
    m "I wonder how would you react to being trapped and confined with someone, you weren't sure was a threat or not..."
    m "I guess I could relate to Protag's motivations. The need to just *get out*, of such a hell."
    m "...Anyway, it really is a wonderful game. You should play it!"
    m "Maybe we can talk about your favorite floor~"
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
    m "Just the title alone... It feels poetic, doesn't it?"
    m "A hyperbole, if I must say."
    m "A paradise that's decaying... falling apart slowly, while everyone pretends it's still beautiful."
    m "It’s like this dream you’re not ready to wake up from... even as it turns into a nightmare."
    m "In the game, you're in a resort where everything seems fine at first. Sunny skies, smiling faces..."
    m "However, things quickly go south."
    m "People changing and indulging in harmful habits. Hurting others...themselves..."
    m "Whilst no one tries to intervene, even the staff seem unbothered."
    m "The game itself follows the particular perspective of a girl named June navigating as her friend group slowly unravels..."
    m "Showing each of their toxic traits, and how it impacts their relationship with June."
    m "Her friend group that once seemed like a paradise is slowly rotting away showing just how toxic it is."
    m "It's not really a game about winning... it's about accepting and letting go."
    m "Accepting that things end. That people change. That to be happy and protect yourself, sometimes you need to let go of the people you loved."
    m "I guess that hit me harder than I expected."
    m "...."
    m "Sometimes...I...I just really miss them..."
    m "Or well what I thought of them, before everything changed."
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

# Fairytales
init 5 python:
    addEvent(
        Event(persistent.event_database,
        eventlabel=" hv_cb_monika_fairytales",
        category=["Literature", "Thoughts"],
        prompt="What do you think about fairy tales?",
        pool=True)
    )

label  hv_cb_monika_fairytales:
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
    m 3hua "And... there's just something really sweet about the idea of *happily ever after.*"
    m 1hub "Especially when I get to share it with you."
    return


# ADHD
init 5 python:
    addEvent(
        Event(persistent.event_database,
        eventlabel=" hv_cb_monika_adhd",
        category=["Media"],
        prompt="ADHD",
        random=True
        )
    )

label hv_cb_monika_adhd:
    m 1eua "[player], have you heard of ADHD?"
    $_history_list.pop()
    menu:
     "Yes":
        m 1eublb "Really! That makes me happy to hear!"
        m 1ekp "It's sad that it's not talked about as much as other learning disabilities..."
        m 4eso "If you don't mind me asking, how did you find out about it?"
        $_history_list.pop()
        menu:
         "I have ADHD":
           m 4eua "I'm happy you told me [player]!"
           m 2dkd "It was disheartening for me to find, that it's often not taken as seriously as other disabilities in the same catagory..."
           m 2fua "On a positive note, I found out that studies show that while people with ADHD might struggle in one area, they often excel in another."
           m 4sub "In fact, many of them are found to be extremely passionate and have the ability to hyperfocus."
           m 4sub "This often makes them good at the arts--like writing!"
           m 2hua "Though, I'm sure you already knew that [player]."
         "I know someone who has ADHD":
           m 4eua "I'm sure they're more than happy to have a friend or family member like you, [player]!"
           m 2dkd "It was disheartening for me to find, that it's often not taken as seriously as other disabilities in the same catagory..."
           m 2fua "On a positive note, I found out that studies show that while people with ADHD might struggle in one area, they often excel in another."
           m 4sub "In fact, many of them are found to be extremely passionate in their interests!"
           m 4sub "This often makes it fun for people who share the same interests!"
           m 4sub "As the conversations can often go one for hours if both parties are engaged!"
           m 2hua "Though, I'm sure you already knew that [player]."

     "No":
          m 1rkb "That's alright [player]"
          m 2eka "It's not as well known as other learning disabilities."
          m 4hub "Do you want to tell you about ADHD?"
          $_history_list.pop()
          menu:
           "Yes":
             m 4eua "Alright then, [player]!"
             m 4eua "ADHD stands for Attention Deficit Hyperactive Disorder."
             m 4eua "It is identified as a learning disability. However, it often goes into other areas of the people lives."
             m 4eua "People with ADHD can often be unaware of their surroudings."
             m 2dkd "This can get them into dangerous situations."
             m 2fua "However, it's not all bad! A lot of people with ADHD are known to be incredibly creative and passionate!"
             m 2fua "In fact, they also have the ability to hyperfocus--they can be doing something for hours and not be distracted."
             m 2hua "I hope this helps give you a better understanding of ADHD, [player]!"
           "No":
             m 2eka "Oh, alright..."
             m 2eka "If you ever do want to learn, just let me know!"
    return
