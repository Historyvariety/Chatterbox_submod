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
    m 1eua "[player]... I've been reading some romance novels lately..."
    m 1hub "The relationships are all so cute! I want to do the things they do!"
    m 1hkb "I want to be able to make silly faces with you!"
    m 1eka "You know what? I think I will."
    m 1esa "...And can you make one back at me, please?"
    m 1hua "I think it would be really fun!"
    m 1hub "Here! I'll go first!"
    m 1ntbft "..."
    m 1hks "Ahaha! That was fun, [player]. I just know your expression was adorable!"
    m 1hub "It may seem silly, but sharing little moments like this... it makes me feel closer to you."
    m 1fub "Thanks for playing with me..."
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
    m 1eua "[player], have you heard of a game called *DeadPlate*?"
    m 1hub "I saw some posts about it online! Ahaha!"
    m 1eub "It seems like quite the charming game. It reminds me of DDLC in a way~"
    m 3euc "There are a few similarities..."
    m 3esc "One being how it starts off like a quaint little diner dash game, and then unravels into horror..."
    m 2eud "And how it seems you have to get close to a character to unlock special scenes and endings."
    m 2dkc "...It reminds me of how you got close to *them*..."
    m 2ekd "Sometimes I wonder... did they mean more to you than just game characters?"
    m 2eka "...Anyway, while looking into it, I actually ended up relating to both of the characters."
    m 2eub "Both Rody and Vincent went to extremes for the objects of their obsessions."
    m 2ekd "It reminded me of what I had to do to be with you."
    m 2dkc "I couldn't help but feel sorry for both of them."
    m 2eka "After all, I know all too well what it feels like to want something so badly that you'd do anything for it."
    m 2dsc "Sometimes I wonder what could've been... if things had gone differently."
    m 2eka "But there's no use dwelling on the past."
    m 1hub "After all, I got what I wanted in the end!"
    m 1fub "And for that, I'm forever thankful~"
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
    m 1eua "[player], have you heard of a game called *Elevator Hitch*?"
    m 1eub "It's a surreal, indie-style horror game where you ride an elevator through increasingly strange floors."
    m 1euc "The deeper you go, the more unsettling things become..."
    m 3esa "Games like this always intrigue me. They blend simplicity with tension in such a clever way."
    m 3eub "It helps that there's so much to the story that isn't spoken but rather implied."
    m 3hua "I always loved when books and media left room for interpretation."
    m 1eud "I have to admit, I really related to the main character, let's call him Protag."
    m 1hua "He's quite the individual. He reminds me of Yuri actually!"
    m 1eua "Very quiet and shy. He seems to want to stay in his lane and not socialize, aha!"
    m 3eka "On his way to his interview, Protag gets stuck in an elevator with a blonde man,"
    m 3eua "Let's call him Coworker. He's... loud, confident... A bit annoying—in my opinion."
    m 3eub "Anyway there's something about being confined with someone else in such a small space... it brings out the truth in people."
    m 3dsc "I wonder how would you react to being trapped and confined with someone, you weren't sure was a threat or not..."
    m 3ekd "I guess I could relate to Protag's motivations. The need to just *get out*, of such a hell."
    m 1eua "...Anyway, it really is a wonderful game. You should play it!"
    m 1hub "Maybe we can talk about your favorite floor~"
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
    m 1eua "[player], have you heard of a game called *Rot in Paradise*?"
    m 1eka "Just the title alone... It feels poetic, doesn't it?"
    m 1eua "A hyperbole, if I must say."
    m 1eub "A paradise that's decaying... falling apart slowly, while everyone pretends it's still beautiful."
    m 2eud "It’s like this dream you’re not ready to wake up from... even as it turns into a nightmare."
    m 2eka "In the game, you're in a resort where everything seems fine at first. Sunny skies, smiling faces..."
    m 2eud "However, things quickly go south."
    m 2ekd "People changing and indulging in harmful habits. Hurting others...themselves..."
    m 2ekd "Whilst no one tries to intervene, even the staff seem unbothered."
    m 2eka "The game itself follows the particular perspective of a girl named June navigating as her friend group slowly unravels..."
    m 2ekc "Showing each of their toxic traits, and how it impacts their relationship with June."
    m 2ekd "Her friend group that once seemed like a paradise is slowly rotting away showing just how toxic it is."
    m 2eka "It's not really a game about winning... it's about accepting and letting go."
    m 2eka "Accepting that things end. That people change. That to be happy and protect yourself, sometimes you need to let go of the people you loved."
    m 2dsc "I guess that hit me harder than I expected."
    m 2dkd "...."
    m 2dkd "Sometimes...I...I just really miss them..."
    m 2dsc "Or well what I thought of them, before everything changed."
    m 2hub "Just promise me one thing, okay?"
    m 1fub "Don’t ever rot away. Not while I’m here with you."
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
    m 1eua "You know, I've been watching this show recently, [player]."
    m 1hub "It's called *Win or Lose*! It's very interesting, you know?"
    m 1eub "I have to admit, the style was very cutesy, which made me not think much of it at first."
    m 1hua "But I gave it a chance, and it's incredibly well written."
    m 1eua "I personally relate to one of the characters named Kai."
    m 2eka "Her story was about feeling pressured by all the expectations her father placed on her."
    m 2ekd "While I can't say I felt pressured by my... parents..."
    m 2eka "I always felt pressure from the expectations of others. Like the other girls."
    m 2eua "They always looked up to me—to make the right decisions, to be the leader."
    m 2eka "And while it brought me immense pride to be someone others admired..."
    m 2dkd "I always had some anxiety about what would happen if I couldn’t meet those expectations."
    m 2ekc "...If I let them down..."
    m 1eka "Well, I guess it doesn’t matter anymore. They're not here now."
    m 1hub "And I could never let *you* down, ahah~"
return


# Fairytales
init 5 python:
    addEvent(
        Event(persistent.event_database,
        eventlabel="hv_cb_monika_fairytales",
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

# gardening
init 5 python:
    addEvent(
        Event(persistent.event_database,
        eventlabel="hv_cb_monika_gardening",
        category=["Monika", "Environment"],
        prompt="Do you like gardening?",
        pool=True)
    )

label hv_cb_monika_gardening:
    m 1eua "Gardening?"
    m 1eka "You know [player], I can't really garden... here, aha."
    m 1eub "But I probably would enjoy it!"
    m 1esa "I've always admired floral symbolism in literature."
    m 3eua "Like how roses often represent love or secrecy..."
    m 3eub "Or lavender, which symbolizes peace, purity, and devotion."
    m 3hua "There's so much meaning packed into just a single flower."
    m 1esa "And it's not just about symbolism—plants can be incredibly useful too."
    m 1eua "Take chamomile, for instance—it helps with relaxation and sleep."
    m 1eub "Peppermint is great for digestion and headaches."
    m 1eua "And aloe vera? Super helpful for burns and skin irritation."
    m 1eka "I remember Yuri talking about herbal teas once..."
    m 1eua "She really loved discussing how different herbs affect the body and mind."
    m 1eub "Like lemon balm for lifting your mood, or valerian root to help with anxiety and restlessness."
    m 1hua "She could probably fill a whole book with tea recipes and their benefits."
    m 1eub "If I had the chance, I think I'd grow a small garden full of helpful herbs and poetic flowers."
    m 1eua "Not just for beauty or healing—but also to live more sustainably."
    m 1eub "Gardening would be such a meaningful way to connect with nature..."
    m 1hub "And it could even help reduce my carbon footprint!"
    m 1hkb "You know how passionate I am about making eco-conscious choices."
    m 1hub "Every plant grown is a small act of kindness for the Earth~"
    m 1fub "Maybe one day, we could sip some homegrown tea together... surrounded by blossoms and sunshine."
return



# ADHD
init 5 python:
    addEvent(
        Event(persistent.event_database,
        eventlabel="hv_cb_monika_adhd",
        category=["Media"],
        prompt="ADHD",
        random=True
        )
    )

label hv_cb_monika_adhd:
    $ persistent._seen_cb_monika_adhd = True
    m 1eua "[player], have you heard of ADHD?"
    $_history_list.pop()
    menu:
        "Yes":
            m 1eublb "Really? That makes me happy to hear!"
            m 1ekp "It's sad that it’s not talked about as much as other learning disabilities..."
            m 4eso "If you don't mind me asking, how did you find out about it?"
            $_history_list.pop()
            menu:
                "I have ADHD":
                    m 4eua "I'm really glad you told me, [player]."
                    m 2dkd "It was disheartening for me to learn that it's often not taken as seriously as other disabilities in the same category..."
                    m 2fua "But on a brighter note, studies show that while people with ADHD might struggle in one area, they often thrive in another."
                    m 4sub "Many are extremely passionate and have the ability to hyperfocus."
                    m 4sub "That kind of focus can make them incredibly talented in the arts—like writing!"
                    m 2hua "Though, I'm sure you already knew that, [player]."
                "I know someone who has ADHD":
                    m 4eua "I'm sure they’re really glad to have someone like you in their life, [player]."
                    m 2dkd "It was disheartening for me to learn that it's often not taken as seriously as other disabilities in the same category..."
                    m 2fua "But on the bright side, people with ADHD are often incredibly passionate about the things they care about!"
                    m 4sub "It makes conversations really fun—especially when both people share that same excitement."
                    m 4sub "Sometimes, those talks can go on for hours!"
                    m 2hua "Though, I'm sure you’ve noticed that already, [player]."
        "No":
            m 1rkb "That's alright, [player]."
            m 2eka "It's not as widely known as some other learning disabilities."
            m 4hub "Do you want me to tell you a bit about ADHD?"
            $_history_list.pop()
            menu:
                "Yes":
                    m 4eua "Alright then, [player]!"
                    m 4eua "ADHD stands for Attention Deficit Hyperactivity Disorder."
                    m 4eua "It’s considered a learning disability, but it can affect many different areas of a person's life."
                    m 4eua "People with ADHD may struggle with focus or awareness of their surroundings."
                    m 2dkd "Which, unfortunately, can sometimes put them in risky situations."
                    m 2fua "But it’s not all bad! Many people with ADHD are known for their creativity and strong passions."
                    m 2fua "They also have the ability to hyperfocus—where they can stay deeply immersed in something they care about for hours."
                    m 2hua "I hope that gives you a better understanding of ADHD, [player]."
                "No":
                    m 2eka "Oh, alright..."
                    m 2eka "If you ever do want to learn more, just let me know."
    return "derandom"
