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
  m "[player]...I've been reading some romance novels lately...."
  m "The relationships are all so cute! I want to do the things they can do!"
  m "I want to be able to make silly faces with you!"
  m "You know what! I think I will."
  m "...and can you make one back to me, please?"
  m "I think it would be really fun!"
  m "Here! I'll go first!"
  m "...."
  m "Ahaha! That was fun [player], and I know your expression was just too cute!"
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
    m "[player], have you heard of a game called DeadPlate?"
    m "I saw some posts about it online! Ahaha!"
    m "It seems like quite the charming game! It reminds me of DDLC in a way~"
    m "There's a few similarities on it..."
    m "One being, how it starts off as a quaint little diner dash game, and the unravels into horror..."
    m "and how it seems you have to get close to a character in order to access special scenes and endings!"
    m "...It reminds me of how you got close to them..."
    m "You know I still do sometimes wonder, if they did happen to mean more to you than just game characters..."
    m "...Anyway, as I was looking into it I actually ended up relating to both of the characters."
    m "Both of the characters, Rody and Vincent, went to extremes regarding the object's of their obsessions."
    m "It reminded me of what I had to do to be with you."
    m "I couldn't help but feel sorry for both of them."
    m "..."
    m "And for that I'm forever thankful~"
return

