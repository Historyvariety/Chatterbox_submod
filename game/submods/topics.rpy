#Plushies
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="hv_topic_silly_faces",
            category=["Romance"], # list of categories this topic belongs in (These are automatically capitalized)
            prompt="Making Faces", # button text
            random=True
        )
    )

label hv_silly_faces:
  m [player]...I've been reading some romance novels lately...."
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
