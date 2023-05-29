import ldde

l = ldde.Ldde()
l.insert_initial("A")
l.insert_initial("B")
l.insert_end("B")
l.remove_initial()
l.remove_end()
l.show()

