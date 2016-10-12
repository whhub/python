things = ['a', 'b', 'c', 'd']
print(things[1])

things[1] = 'z'
print(things[1])

print(things)


stuff = {'name': 'Zed', 'age': 36, 'height': 6*12+2}
print(stuff['name'])
print(stuff['age'])
print(stuff['height'])
stuff['city'] = 'San Francisco'
print(stuff['city'])

stuff[1] = "Wow"
stuff[2] = 'Neato'

print(stuff)

del stuff['city']
del stuff[1]
del stuff[2]

print(stuff)


class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_birthday = Song(["Happy birthday to you", "I don't want to ge sued", "So I'll stop right here"])

bulls_on_parade = Song(["They rally around the family", "With pockets full of shells"])

happy_birthday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

