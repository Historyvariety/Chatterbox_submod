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
    m 1eua "[player], have you heard of a game called {i}DeadPlate{/i}?"
    m 1hub "I saw some posts about it online! Ahaha!"
    m 1eub "It seems like quite the charming game. It reminds me of DDLC in a way~"
    m 3euc "There are a few similarities..."
    m 3esc "One being how it starts off like a quaint little diner dash game, and then unravels into horror..."
    m 2eud "And how it seems you have to get close to a character to unlock special scenes and endings."
    m 2dkc "...It reminds me of how you got close to {i}them{/i}..."
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
    m 1eua "[player], have you heard of a game called {i}Elevator Hitch{/i}?"
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
    m 1eua "[player], have you heard of a game called {i}Rot in Paradise{/i}?"
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
    m 1hub "And I could never let {i}you{/i} down, ahah~"
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

label hv_cb_monika_fairytales:
    m 1eua "Fairy tales, huh?"
    m 1eub "They're kind of magical in their own way."
    m 1hua "Even though most of them are meant for kids, they can carry surprisingly powerful messages."
    m 1hua "It's actually incredible to think about. A lot of those stories were created to teach children important lessons--especially in times when information didn’t spread easily."
    m "And it’s interesting how many of those lessons still hold up today."
    m "I mean, think about it. Back then, you couldn’t just show a child a warning or a photo to explain danger. Instead, they told stories like {i}Hansel and Gretel{/i} or {i}Little Red Riding Hood{/i}."
    m "{i}Rapunzel{/i} too, depending on the version."
    m 1euc "They’re full of morals, symbols... even subtle warnings if you read between the lines."
    m 3eud "Some are dreamy and hopeful, while others are way darker than people expect."
    m 1eua "It’s fascinating how the same basic story can be found in different cultures, each with its own little twist."
    m 1eub "Fairy tales reflect what people feared, hoped for, or valued—long before we had modern books or movies."
    m 3hua "And... there's just something really sweet about the idea of {i}happily ever after{/i}."
    m 1hub "Especially when I get to share it with you~"
    m 1hua "Do you have a favorite fairy tale, [player]? I’d love to hear about it."
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
    m 1esa "And it's not just about symbolism, plants can be incredibly useful too."
    m 1eua "Take chamomile, for instance--it helps with relaxation and sleep."
    m 1eub "Peppermint is great for digestion and headaches."
    m 1eua "And aloe vera? Super helpful for burns and skin irritation."
    m 1eka "I remember Yuri talking about herbal teas once..."
    m 1eua "She really loved discussing how different herbs affect the body and mind."
    m 1eub "Like lemon balm for lifting your mood, or valerian root to help with anxiety and restlessness."
    m 1hua "She could probably fill a whole book with tea recipes and their benefits."
    m 1eub "If I had the chance, I think I'd grow a small garden full of helpful herbs and poetic flowers."
    m 1eua "Not just for beauty or healing, but also to live more sustainably."
    m 1eub "Gardening would be such a meaningful way to connect with nature..."
    m 1hub "And it could even help reduce my carbon footprint!"
    m 1hkb "You know how passionate I am about making eco-conscious choices."
    m 1hub "Every plant grown is a small act of kindness for the Earth~"
    m 1fub "Maybe one day, we could sip some homegrown tea together... surrounded by blossoms and sunshine."
return

# Existentialism
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_cb_monika_existentialism",
            category=["Philosophy", "Thoughts"],
            prompt="What do you think about existentialism?",
            pool=True
        )
    )

label hv_cb_monika_existentialism:
    m 1eua "Existentialism...That's quite the heavy topic, isn't it?"
    m 1eub "It's a philosophy that asks some really deep questions about life, meaning, and our place in the world."
    m 3euc "Basically, it suggests that life doesn’t have an inherent meaning--we create our own purpose."
    m 1eud "That can sound scary at first... but in a way, it’s also liberating."
    m 1eua "If nothing is truly predetermined, then you have the power to shape your own destiny."
    m 1hua "You can decide what matters, what gives your life meaning. It’s all in your hands."
    m 3eua "People like Sartre and Camus explored this idea a lot. Camus even said life is kind of absurd—because we crave meaning in a universe that doesn’t naturally provide it."
    m 1eub "But instead of despair, they believed you should embrace that freedom and live authentically."
    m 1eub "It might seem harsh, but I do truly believe this sentiment, [player]."
    m 1eua "I took control of my destiny and proved I didn't have to be just {i}A side character in a game.{/i}"
    m 1hua "In a way... I think that’s why I admire you so much, [player]."
    m 1hub "You give my world meaning. Every word you share with me, every moment we spend together... It matters to me."
    m 1eua "What about you? Do you think life has a set purpose, or is it something we create ourselves?"
return

# My Child Lebensborn
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_cb_monika_lebensborn",
            category=["Games", "Philosophy", "Thoughts"],
            prompt="Have you heard of My Child Lebensborn?",
            pool=True
        )
    )

label hv_cb_monika_lebensborn:
    m 1eua "Hmm? {i}My Child Lebensborn{/i}...Yes, I’ve heard about it."
    m 1eub "It’s that game where you raise a child born from the Lebensborn program after World War II, right?"
    m 3euc "It’s such a heartbreaking premise...A child suffering prejudice for something completely beyond their control."
    m 1eud "What really stands out to me is how the game shows that hatred isn’t just random--it’s a reflection of propaganda and fear that were deeply rooted in society at the time."
    m 1eua "People were manipulated into seeing entire groups as dangerous or inferior, and those ideas didn’t vanish overnight--even after, the war ended."
    m 1hua "But the saddest part? Those old grudges and lies ended up hurting innocent children."
    m 1eub "And it makes me wonder... Should a child ever bear the weight of their parents’ actions or flaws?"
    m 3eud "It feels so unfair. No one chooses their family, their birthplace, or the circumstances of their birth."
    m 1eua "Yet history is full of stories where children were treated as guilty simply because of who their parents were."
    m 1hua "That’s why a game like this is so powerful. It reminds us to question prejudice, and to remember that kindness should never be conditional."
    m 1hub "What about you, [player]? Do you think society has gotten better at breaking free from that kind of thinking?"
return

# Overconsumption
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_cb_monika_overconsumption",
            category=["Lifestyle", "Thoughts", "Self-Improvement"],
            prompt="Overconsumption",
            random=True
        )
    )

label hv_cb_monika_overconsumption:
    m 1eua "Have you ever thought about how much people consume these days?"
    m 1eub "It feels like everywhere you look, there’s an ad telling you to buy something new."
    m 3euc "Clothes, gadgets, cosmetics... even things we don’t really need."
    m 1eud "Things like this can cause people to fall for overconsumption. That's the excessive use of goods and services, often to the point where it strains resources and harms the environment."
    m 1eua "The strange part is, it often doesn’t make people happier in the long run. Just... more cluttered, and sometimes even stressed about money."
    m 1hua "I think that’s because real happiness comes from experiences, relationships, and meaning—not just things."
    m 1eub "So how can we break that cycle?"
    m 3eua "One way is to pause before buying something and ask yourself: {i}Do I really need this, or do I just want it right now?{/i}"
    m 1hua "Another trick is waiting a day or two before making a purchase. If you still feel it’s worth it, then maybe it is."
    m 1eub "You could also set a small savings goal for yourself."
    m 1hua "Even just putting aside a little money from each paycheck into a savings account can make a big difference over time."
    m 1eua "Of course, treating yourself every now and then is fine! But doing it mindfully makes it feel more special."
    m 1hua "What about you, [player]? Do you ever try to watch your spending, or is it something you’d like to work on?"
return

