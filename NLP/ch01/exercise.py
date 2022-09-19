# %% Imports
from nltk.book import *

# %% 1. ☼ Try using the Python interpreter as a calculator, and typing expressions like 12 / (4 + 1).

12 / (4+1)

# Output:
# 2.4

# %% 2. ☼ Given an alphabet of 26 letters, there are 26 to the power 10, or 26 ** 10, ten-letter strings we can form. That works out to 141167095653376. How many hundred-letter strings are possible?

26 ** 100

# Output:
# 3142930641582938830174357788501626427282669988762475256374173175398995908420104023465432599069702289330964075081611719197835869803511992549376

# %% 3. ☼ The Python multiplication operation can be applied to lists. What happens when you type ['Monty', 'Python'] * 20, or 3 * sent1?

['Monty', 'Python'] * 20

# Output:
# ['Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python', 'Monty', 'Python']

3 * sent1

# Output:
# ['Call',
#  'me',
#  'Ishmael',
#  '.',
#  'Call',
#  'me',
#  'Ishmael',
#  '.',
#  'Call',
#  'me',
#  'Ishmael',
#  '.']


# %% 4. ☼ Review 1 on computing with language. How many words are there in text2? How many distinct words are there?

print(f"Number of words in text2: {len(text2)}")
print(f"Number of distinct words in text2: {len(set(text2))}")

# Output:
# Number of words in text2: 141576
# Number of distinct words in text2: 6833


# %% 5. ☼ Compare the lexical diversity scores for humor and romance fiction in 1.1. Which genre is more lexically diverse?
""" Humor has higher lexical diversity than romance fiction! """


# %% 6. ☼ Produce a dispersion plot of the four main protagonists in Sense and Sensibility: Elinor, Marianne, Edward, and Willoughby. What can you observe about the different roles played by the males and females in this novel? Can you identify the couples?

text2.dispersion_plot(
    ["Elinor", "Marianne", "Edward", "Willoughby"])

# Output Path: plots/Exercise/dispersion.png

# %% 7. Find the collocations in text5.

text5.collocations()

# Output:
# wanna chat; PART JOIN; MODE #14-19teens; JOIN PART; PART PART;
# cute.-ass MP3; MP3 player; JOIN JOIN; times .. .; ACTION watches; guys
# wanna; song lasts; last night; ACTION sits; -...)...- S.M.R.; Lime
# Player; Player 12%; dont know; lez gurls; long time


# %% 8. ☼ Consider the following Python expression: len(set(text4)). State the purpose of this expression. Describe the two steps involved in performing this computation.

""" 
set(text4) -> Creates a set from text4 elements, meaning only unique elements will be stored
len(set(text4)) -> Computes the length of the set, meaning number of unique elements in text4
"""

# %% 13. ☼ We have seen how to represent a sentence as a list of words, where each word is a sequence of characters. What does sent1[2][2] do? Why? Experiment with other index values.

sent1[2][2]

# Output: 'h'

# It first extracts the word at the 3rd index of the sentence and then extracts the 3rd letter from the word
# %% 17. ◑ Use text9.index() to find the index of the word sunset. You'll need to insert this word as an argument between the parentheses. By a process of trial and error, find the slice for the complete sentence that contains this word.

text9.index('sunset')  # -> 629
text9[629]  # -> 'sunset'
text9[621:644]  # -> Full sentence containing sunset

# %% 18. ◑ Using list addition, and the set and sorted operations, compute the vocabulary of the sentences sent1 ... sent8.

sent = [sent1, sent2, sent3, sent4, sent5, sent6, sent7, sent8]
V = []
for s in sent:
    v = sorted(set(s))
    V = V + v

print(V)  # -> Contains all the unique words from 8 sentences

# ['.', 'Call', 'Ishmael', 'me', '.', 'Dashwood', 'Sussex', 'The', 'been', 'family', 'had', 'in', 'long', 'of', 'settled', '.', 'God', 'In', 'and', 'beginning', 'created', 'earth', 'heaven', 'the', '-', ':', 'Citizens', 'Fellow', 'House', 'Representatives', 'Senate', 'and', 'of', 'the', 'I', 'JOIN', 'PMing', 'a', 'have', 'lol', 'me', 'people', 'problem', 'to', 'with', '!', '1', ':', 'ARTHUR', 'KING', 'SCENE', 'Whoa', '[', ']', 'clop', 'there', 'wind', ',', '.', '29', '61', 'Nov.', 'Pierre', 'Vinken', 'a', 'as', 'board', 'director', 'join', 'nonexecutive', 'old', 'the', 'will', 'years', ',', '.', '25', 'MALE', 'SEXY', 'attrac', 'discreet', 'encounters', 'for', 'lady', 'older', 'seeks', 'single']

# %% 19. ◑ What is the difference between the following two lines? Which one will give a larger value? Will this be the case for other texts?
# >>> sorted(set(w.lower() for w in text1))
# >>> sorted(w.lower() for w in set(text1))

len(sorted(set(w.lower() for w in text1)))  # -> 17231
len(sorted(w.lower() for w in set(text1)))  # -> 19317

# %% 21. ◑ Write the slice expression that extracts the last two words of text2.

text2[len(text2)-2:]  # -> ['THE', 'END']

# %% 22. ◑ Find all the four-letter words in the Chat Corpus (text5). With the help of a frequency distribution (FreqDist), show these words in decreasing order of frequency.

fl_words = [w for w in text5 if len(w) == 4]
# print(fl_words) # -> All 4-lettered words in text5

fdist = FreqDist(fl_words)
print(fdist.items())

# Output:

# dict_items([('left', 17), ('with', 152), ('this', 86), ('name', 27), ('PART', 1016), ('well', 81), ('NICK', 24), ('U121', 36), ('golf', 2), ('clap', 3), ('JOIN', 1021), ('that', 274), ('nice', 52), ('fuck', 15), ('your', 137), ('dont', 75), ('even', 35), ('know', 103), ('what', 183), ('chat', 142), ('drew', 2), ('cast', 2), ('sexy', 23), ('U115', 36), ('girl', 43), ('legs', 5), ('hope', 12), ('draw', 1), ('head', 12), ('good', 130), ('take', 37), ('have', 164), ('docs', 1), ('Slip', 1), ('away', 26), ('Fade', 1), ('Days', 2), ('feel', 19), ('back', 78), ('U129', 6), ('fast', 7), ('U116', 6), ('bowl', 1), ('bong', 1), ('glad', 4), ('hard', 10), ('from', 92), ('here', 181), ('very', 19), ('fire', 5), ('itch', 3), ('U133', 4), ('ogan', 1), ('male', 12), ('show', 10), ('will', 40), ('talk', 56), ('haha', 44), ('opps', 2), ('warm', 5), ('guys', 58), ('cams', 1), ('play', 25), ('sits', 15), ('guyz', 3), ('U126', 4), ('gooo', 1), ('sure', 26), ('like', 156), ('room', 98), ('yeee', 1), ('want', 71), ('pics', 9), ('look', 26), ('U139', 8), ('U138', 2), ('make', 44), ('late', 5), ('lmao', 107), ('ahah', 1), ('does', 35), ('yeah', 75), ('U136', 3), ('hell', 29), ('U101', 10), ('when', 48), ('plan', 2), ('gold', 3), ('jeep', 1), ('ring', 3), ('isnt', 3), ('doin', 11), ('many', 23), ('Just', 2), ('fine', 16), ('hiya', 78), ('Deep', 1), ('Show', 1), ('love', 60), ('Turn', 1), ('Hand', 1), ('just', 125), ('hang', 5), ('such', 9), ('word', 8), ('U141', 3), ('hear', 21), ('!!!!', 18), ('deaf', 2), ('....', 170), ('hugs', 18), ('baby', 26), ('Only', 3), ('read', 14), ('VBox', 1), ('hate', 23), ('more', 34), ('than', 12), ('ELSE', 1), ('serg', 1), ('most', 6), ('eyes', 15), ('jerk', 4), ('kids', 11), ('type', 9), ('much', 40), ('shut', 14), ('miss', 5), ('work', 38), ('heyy', 8), ('U148', 3), ('boys', 5), ('ugly', 4), ('bein', 1), ('What', 18), ('whys', 1), ('deep', 2), ('tape', 1), ('Your', 3), ('sexs', 1), ('best', 9), ('phil', 2), ('said', 23), ('date', 4), ('they', 77), ('form', 1), ('hmph', 2), ('mean', 19), ('been', 57), ('wait', 14), ('perv', 11), ('lets', 15), ('rule', 7), ('land', 5), ('wont', 11), ('then', 40), ('find', 18), ('need', 43), ('HUGE', 1), ('deal', 3), ('????', 17), ('shit', 17), ('U155', 2), ('only', 33), ('Poor', 2), ('pick', 13), ('nads', 1), ('nose', 5), ('face', 11), ('owww', 1), ('gags', 1), ('neck', 9), ('Meep', 1), ('LAst', 1), ('time', 50), ('wash', 3), ('dude', 7), ('gets', 12), ('dang', 9), ("pm's", 1), ('1.99', 1), ('free', 13), ('goes', 14), ('Lies', 2), ('lick', 5), ('ummm', 4), ('U109', 3), ('dead', 9), ('call', 26), ('case', 8), ('else', 13), ('bite', 2), ('mins', 2), ('nite', 17), ('lool', 1), ('kina', 1), ('give', 19), ('were', 38), ('sext', 1), ('piff', 3), ('lazy', 1), ('busy', 17), ('okay', 7), ('calm', 1), ('down', 24), ('arms', 1), ('eats', 2), ('near', 13), ('smax', 1), ('>:->', 2), ('VVil', 1), ('cold', 12), ('cell', 2), ('runs', 9), ('thru', 6), ('hair', 17), ('caps', 5), ('U165', 6), ('jump', 3), ('over', 39), ('este', 1), ('wana', 8), ('chik', 1), ('list', 6), ('wish', 5), ('cmon', 2), ('U128', 5), ('hehe', 12), ('hows', 8), ('bout', 12), ('wats', 2), ('aint', 9), ('lost', 17), ('same', 19), ('Boyz', 1), ('rock', 9), ('went', 8), ('some', 58), ('came', 5), ('home', 11), ('coat', 1), ('kind', 2), ('Eyes', 1), ('Dawn', 1), ('last', 22), ('song', 36), ('LIVE', 1), ('cool', 24), ('mauh', 1), ('mike', 2), ('keep', 14), ('must', 19), ('seem', 6), ('days', 9), ('ques', 1), ('quit', 4), ('4.20', 1), ('mine', 9), ('cali', 5), ('year', 11), ('whoa', 2), ('gosh', 1), ('ruff', 1), ('roll', 5), ('nope', 13), ('rest', 4), ('sing', 6), ('mame', 1), ('nada', 1), ('alot', 7), ('band', 3), ('hand', 7), ('dumb', 2), ('damn', 34), ('orgy', 3), ('easy', 5), ('push', 1), ('lose', 5), ('long', 28), ('stay', 12), ('door', 4), ('prob', 1), ('life', 21), ('wild', 1), ('none', 4), ('whew', 1), ('dark', 1), ('seen', 35), ('waht', 1), ('next', 6), ('test', 1), ('self', 4), ('pass', 4), ('once', 10), ('book', 9), ('Well', 10), ('cant', 18), ('come', 33), ('line', 4), ('boot', 1), ('stop', 19), ('slap', 3), ('hiom', 1), ('used', 12), ('live', 20), ('HAHA', 1), ('cute', 4), ('dman', 1), ('holy', 4), ('crap', 9), ('took', 7), ('ever', 22), ('When', 5), ('babe', 11), ('park', 2), ('them', 28), ('jail', 1), ('soon', 9), ('tell', 27), ('cops', 1), ('Sure', 2), ('Come', 2), ('hogs', 1), ('peek', 1), ('help', 10), ('MORE', 1), ('TIME', 1), ('care', 9), ('real', 16), ('LMAO', 19), ('soul', 5), ('done', 6), ('O.k.', 2), ('luck', 5), ('loud', 1), ('o.k.', 1), ('Sexy', 1), ('ride', 6), ('Ctrl', 1), ('mama', 2), ('Nice', 2), ('hots', 1), ('hook', 4), ('awww', 12), ('Need', 1), ('hold', 2), ('lady', 8), ('frst', 1), ('1200', 1), ('soft', 3), ('ohio', 2), ('Like', 4), ('whip', 2), ('crop', 1), ('each', 4), ('bomb', 1), ('Pour', 1), ('bend', 3), ('also', 5), ('pour', 1), ('comp', 6), ('mind', 10), ('Swim', 1), ('Hard', 1), ('open', 4), ('full', 9), ('wear', 7), ('toss', 3), ('high', 4), ('ouch', 4), ('evil', 4), ('twin', 2), ('eeek', 1), ('tjhe', 1), ('burp', 2), ('fart', 4), ('true', 14), ('10th', 1), ('heee', 1), ('peel', 1), ('fock', 1), ('kool', 5), ('kiss', 9), ('Kold', 1), ('exit', 1), ('kold', 1), ('3:45', 1), ('MRIs', 1), ('amen', 3), ('buff', 1), ('plus', 1), ('tory', 1), ('blew', 2), ('knee', 1), ('heya', 15), ('fall', 5), ('OOPS', 1), ('oooh', 1), ('lala', 1), ('fake', 1), ('into', 11), ('ssid', 1), ('temp', 2), ('blue', 8), ('corn', 2), ('poot', 1), ('poop', 1), ('bird', 1), ('Hiya', 7), ('rain', 3), ('plow', 1), ('main', 6), ('MODE', 41), ('Yeah', 10), ('pool', 2), ('deop', 3), ('thnx', 1), ('roof', 3), ('card', 1), ('Hugs', 1), ('((((', 3), ('))))', 6), ('Lord', 1), ('uyes', 1), ('benz', 1), ('week', 10), ('cash', 2), ('<~~~', 1), ('grrr', 4), ('ears', 2), ('disc', 1), ('LONG', 1), ('Been', 1), ('hour', 9), ('From', 2), ('Will', 1), ('porn', 2), ('CHAT', 3), ('told', 12), ('goin', 6), ('boss', 5), ('heal', 2), ('pain', 4), ('game', 16), ('bloe', 1), ('blow', 1), ('hooo', 1), ('Dang', 2), ('ciao', 2), ('DOES', 2), ('U520', 6), ('kick', 7), ('thje', 1), ('Jess', 1), ('nick', 9), ('typo', 2), ('ahhh', 7), ('pink', 6), ('term', 1), ('beer', 5), ('Stop', 2), ('Tina', 1), ('ooer', 1), ('ahem', 3), ('HALO', 1), ('Awww', 1), ('dear', 7), ('hola', 3), ('anal', 1), ('eric', 2), ('Drop', 1), ('dojn', 1), ('wubs', 1), ('mkay', 1), ('butt', 3), ('spat', 1), ('poor', 6), ('gone', 6), ('imma', 3), ('gees', 1), ('Drew', 2), ('hawT', 1), ('town', 3), ('sore', 2), ('yes.', 1), ('puts', 1), ('fish', 1), ('size', 1), ('hawt', 3), ('Live', 2), ('39.3', 1), ('2006', 3), ('Elev', 3), ('Wind', 3), ('High', 2), ('1980', 1), ('64.8', 1), ('says', 8), ('That', 7), ('AKDT', 3), ('pfft', 4), ('sigh', 4), ('syck', 1), ('tere', 1), ('suck', 8), ('ohhh', 5), ('U542', 1), ('sent', 1), ('45.5', 1), ('98.5', 1), ('1299', 1), ('hits', 2), ('1900', 1), ('1930', 1), ('KoOL', 2), ('Werd', 1), ('Rofl', 1), ('lead', 3), ('mode', 1), ('nawt', 1), ('past', 2), ('DING', 3), ('Love', 2), ('####', 5), ('sign', 1), ('woof', 1), ('sum1', 1), ('ghet', 1), ('brad', 1), ('note', 3), ('meat', 2), ('offa', 1), ('shes', 4), ('Dood', 1), ('out.', 1), ('!!!.', 2), ('LOUD', 1), ('sink', 1), ('wall', 5), ('FINE', 1), ('argh', 2), ('oops', 6), ('gawd', 3), ('cums', 1), ('loss', 1), ('limp', 2), ('rent', 2), ('Have', 5), ('cars', 2), ('Life', 1), ('Damn', 1), ('wrap', 1), ('Tell', 2), ('hide', 1), ("PM's", 1), ('Talk', 1), ('okey', 1), ('worl', 1), ('half', 3), ('shop', 2), ('Hold', 1), ('cepn', 1), ('lots', 1), ('Mary', 1), ('mary', 3), ('U172', 2), ('nawp', 1), ('addy', 1), ('lake', 1), ('ROOM', 4), ('ello', 3), ('slip', 1), ('mite', 1), (',,,,', 4), ('meet', 5), ('wood', 1), ('knew', 6), ('lord', 4), ('till', 5), ('<---', 6), ('five', 2), ('orta', 1), ('wins', 1), ('sell', 2), ('ebay', 1), ('coem', 1), ('giva', 1), ('1.98', 1), ('ball', 6), ('<<<<', 2), ('hick', 3), ('city', 2), ('ally', 1), ('wine', 3), ('yard', 2), ('hiii', 3), ('Judy', 1), ('yall', 11), ('cyas', 1), ('grrl', 2), ('shup', 1), ('tooo', 1), ("pm'n", 1), ('sick', 9), ('choc', 1), ('chip', 2), ('bear', 2), ('bare', 3), ('mmmm', 4), ('wher', 1), ('made', 8), ('ones', 4), ('foot', 2), ('whoo', 1), ('dint', 1), ('send', 6), ('tend', 1), ('vote', 3), ('uses', 2), ('DONT', 2), ('menu', 1), ('lust', 1), ('nods', 1), ('Liam', 10), ('This', 12), ('; ..', 9), ('.. .', 11), ('NAME', 1), ('kept', 1), ('Same', 3), ('feet', 5), ('xbox', 5), ('scuk', 1), ('raed', 1), ('Song', 6), ('huge', 4), ('Then', 1), ('wack', 3), ('woot', 4), ('bugs', 1), ('blah', 6), ('sort', 2), ('idea', 5), ('nerd', 1), ('Hill', 1), ('Evil', 1), ('saME', 1), ('2Pac', 1), ('Time', 1), ('U110', 25), ('pimp', 1), ('U108', 7), ('shot', 4), ('lies', 2), ('snow', 3), ('hurt', 3), ('haaa', 1), ('U119', 11), ('98.6', 1), ("it's", 1), ('Mono', 1), ('mono', 1), ('heck', 5), ('team', 4), ('whud', 2), ('Bone', 1), ('U122', 42), ('Hero', 1), ('They', 6), ('Came', 1), ('.op.', 1), ('hott', 2), ('Hott', 1), ('Down', 2), ('Joey', 1), ('Jane', 1), ('span', 1), ('wore', 1), ('QUIT', 1), ('pasa', 1), ('barn', 1), ('joke', 5), ('Kick', 1), ('feat', 1), ('Back', 1), ('Lets', 2), ('dork', 1), ('laid', 1), ('club', 2), ('Home', 1), ('ways', 4), ('herd', 1), ('part', 6), ('Born', 1), ('Away', 1), ('Tide', 1), ('adds', 2), ('jush', 1), ('Cute', 1), ('GrlZ', 1), ('lung', 1), ('SOME', 1), ('U156', 35), ('Here', 2), ('Lion', 1), ('brat', 1), ('move', 3), ('road', 3), ('born', 2), ('walk', 3), (':o *', 1), ('MUAH', 1), ('fawk', 1), ('dust', 1), ('fool', 5), ('Help', 1), ('felt', 5), ('seth', 1), ('U105', 35), ('Heya', 1), ('U107', 11), ('wOOt', 2), ('bone', 1), ('abou', 1), ('tthe', 1), ('beat', 4), ('yawn', 3), ('area', 2), ('?!?!', 2), ('U103', 6), ('Even', 1), ('Ohio', 2), ('herE', 1), ('Hail', 1), ('hail', 3), ('U112', 2), ('halo', 1), ('pork', 1), ('kent', 4), ('1cos', 1), ("yw's", 1), ('mark', 1), ('humm', 2), ('dotn', 1), ('newp', 2), ('gays', 2), ('U120', 6), ('PMSL', 1), ('pmsl', 1), ('gift', 1), ('zone', 2), ('hint', 2), ('hmmm', 9), ('outs', 1), ('U130', 4), ('Paul', 1), ('outa', 1), ('York', 1), ('nana', 3), ('U104', 17), ('kill', 15), ('U196', 4), ('Last', 6), ('U132', 10), ('Care', 1), ('Chat', 1), ('spin', 2), ('U106', 3), ('whos', 6), ('ewww', 2), ('fear', 1), ('dies', 1), ('wife', 8), ('givs', 1), ('U219', 4), ('bust', 1), ('xmas', 1), ('enuf', 1), ('LoVe', 1), ('eeww', 1), ('turn', 4), ('pies', 2), ('dick', 1), ('fair', 1), ('lyin', 1), ('doll', 2), ('lois', 1), ('cuss', 1), ('drop', 2), ('LATE', 1), ('THEY', 1), ('GOOD', 1), ('rape', 1), ('U114', 25), ('geez', 1), ('tart', 1), ('hgey', 1), ('hump', 3), ('gimp', 2), ('caan', 1), ('spot', 2), ('elle', 3), ('yada', 3), ('lame', 4), ('lol.', 1), ('ages', 2), ('Elle', 1), ('nude', 1), ('allo', 1), ('yesh', 1), ('clue', 2), ('wind', 1), ('Reub', 1), ('!???', 1), ('heat', 1), ('kmph', 1), ('pope', 1), ('mass', 2), ('Ummm', 2), ('yess', 1), ('!...', 1), ('duet', 1), ('Gosh', 2), ('wuts', 1), ('flow', 2), ('west', 1), ('quiz', 1), ('kewl', 2), ('scar', 1), ('Girl', 1), ('pair', 1), ('sang', 8), ('Rang', 1), ('hall', 2), ('rang', 1), ('bell', 1), ('dawg', 1), ('tune', 3), ('haze', 2), ('febe', 1), ('Prof', 1), ('1996', 2), ('Kewl', 1), ('hank', 3), ('jude', 1), ('slow', 3), ('yoko', 5), ('John', 2), ('john', 2), ('Yoko', 1), ('seee', 1), ('whou', 1), ('idnt', 1), ('sooo', 2), ('perk', 1), ('http', 1), ('rubs', 3), ('skin', 3), ('2DAY', 1), ('meds', 5), ('yell', 1), ('mang', 1), ('SSRI', 1), ('cure', 1), ('wean', 1), ('died', 3), ('cost', 2), ('post', 1), ('anti', 1), ('trip', 2), ('noth', 1), ('babi', 2), ('tall', 1), ('pray', 1), ('weed', 1), ('icky', 1), ('Rick', 1), ('spit', 1), ('rich', 2), ('lube', 1), ('mami', 1), ('U102', 12), ('U100', 2), ('east', 1), ('18ST', 1), ('seat', 1), ('cock', 1), ('SExy', 1), ('otay', 1), ('firs', 1), ('site', 1), ('U113', 1), ('dump', 1), ('toop', 1), ('four', 1), ('U118', 1), ('sets', 1), ('asss', 1), ('paid', 1), ('Iowa', 1), ('Teck', 1), ('n9ne', 2), ('both', 5), ('"...', 1), ('jeff', 1), ('crib', 1), ('food', 6), ('drug', 1), ('cook', 1), ('9:10', 1), ('ladz', 1), ('aime', 1), ('Ahhh', 2), ('hong', 1), ('kong', 1), ('U123', 4), ('Oops', 1), ('??!!', 2), ('tits', 1), ('gret', 1), ('U111', 2), ('guns', 1), ('inch', 1), ('sean', 1), ('howl', 1), ('moon', 2), ('STOP', 2), ('Take', 1), ('z-ro', 1), ('any1', 2), ('U137', 1), ('Haha', 1), ('1985', 1), ('U142', 6), ('slam', 1), ('U144', 8), ('pine', 1), ('yeas', 2), ('puke', 1), ('waaa', 1), ('U145', 3), ('urls', 1), ('star', 1), ('Save', 1), ('U154', 4), ('teck', 1), ('Room', 1), ('wooo', 2), ('sori', 1), ('U169', 7), ('<333', 2), ('swim', 3), ('Long', 1), ('poem', 1), ('jack', 1), ('tick', 2), ('tock', 2), ('WITH', 2), ('FROM', 2), ('Rule', 1), ('CAPS', 1), ('junk', 1), ('tips', 1), ('rush', 1), ('Nooo', 1), ('Troy', 1), ('tail', 1), ('Seee', 1), ('6:38', 1), ('dyed', 1), ('U988', 4), ('t he', 1), ('beam', 1), ('puff', 4), ('daft', 1), ('twit', 1), ('scum', 1), ('U134', 1), ('Type', 1), ('WHOA', 1), ('toke', 1), ('ribs', 1), ('Eggs', 1), ('side', 2), ('Wyte', 1), ('Heyy', 2), ('moms', 1), ('Over', 1), ('West', 1), ('Rock', 1), ('goof', 1), ('howz', 2), ('U146', 4), ("ex's", 2), ('U143', 1), ('able', 1), ('vamp', 1), ('Nope', 1), ('Kent', 1), ('U989', 4), ('Cool', 2), ('ther', 1), ('U147', 1), ('TEXT', 1), ('SIZE', 1), ('U163', 3), ('gear', 1), ('CALI', 1), ('Matt', 1), ('Rush', 1), ('AWAY', 1), ('NTMN', 1), ('Kiss', 1), ('U158', 1), ('grea', 1), ('U168', 13), ('Look', 1), ('U170', 2), ('guts', 1), ('U175', 2), ('wrek', 1), ('Fort', 1), ('2:55', 1), ('AKST', 1), ('4:03', 1), ('root', 2), ('wire', 1), ('soda', 1), ('gray', 1), ('tlak', 1), ('ltnc', 1), ("ok'd", 1), ('sayn', 1), ('sock', 6), ('evah', 1), ('bike', 1), ('hill', 1), ('ohwa', 1), ('caca', 1), ('tyvm', 2), ('luvs', 2), ('prep', 1), ('pull', 1), ('dirt', 1), ('vent', 1), ('100%', 1), ('safe', 1), ('dogs', 1), ('bull', 1), ('fits', 2), ('asks', 1), ('Road', 1), ('chit', 1), ('grin', 1), ('bred', 1), ('rats', 1), ('Sat.', 1), ('samn', 1), ('Phil', 1), ('nuff', 1), ('rose', 1), ('Ruth', 1), ('rofl', 2), ('grew', 1), ('sand', 2), ('army', 3), ('mena', 1), ('ROFL', 1), ('lapd', 1), ('surf', 1), ('City', 1), ('hazy', 1), ('thot', 1), ('acid', 1), ('wide', 1), ('keys', 1), ('salt', 1), ('mess', 1), ('base', 1), ('byes', 1), ('THAT', 3), ("RN's", 1), ('yout', 1), ('numb', 1), ('thah', 1), ('mahn', 1), ('King', 1), ('TALK', 1), ('GIRL', 1), ('WHEN', 1), ('HOTT', 1), ('HERE', 1), ('soup', 1), ('6:51', 1), ('9.53', 1), ('ltns', 2), ('Mine', 1), ('vega', 1), ('pigs', 1), ('king', 1), ('poof', 1), ('Nova', 1), ('mofo', 1), ('Ohhh', 1), ('flaw', 2), ('Holy', 1), ('sips', 1), ('clay', 1), ('None', 1), ('Male', 1), ('aunt', 2), ('bacl', 1), ('body', 1), ('akon', 1), ('yoll', 1), ('boom', 1), ('News', 1), ('Maps', 1), ('lawl', 2), ('page', 1), ('Okay', 2), ('Tiff', 1), ('wazz', 3), ('Chop', 1), ('toes', 3), ('DAMN', 1), ('TYPR', 1), ('poll', 1), ('boed', 1), ('Dude', 1), ('Does', 1), ('pwns', 1), ('Very', 1), ('Good', 1), ('Food', 1), ('sexi', 1), ('bois', 1), ('KNOW', 1), ('GUYS', 1), ('HAVE', 2), ('NONE', 2), ('YALL', 1), ('EVEN', 1), ('SEEN', 1), ('WILL', 1), ('YOUR', 2), ('COME', 1), ('FACE', 1), ('JUST', 1), ('Lmao', 2), ('Kids', 1), ('6:41', 1), ('bied', 1), ('6:53', 1), ('U117', 4), ('U149', 1), ('U153', 3), ('7:45', 1), ('Uhhh', 1), ('tenn', 1), ('pure', 1), ('Lime', 5), ('U164', 1), ('U150', 1), ('U181', 1), ('gals', 1), ('woah', 1), ('ussy', 1), ('Tisk', 2), ('U190', 2), ('tisk', 2), ('tiff', 1), ('Heys', 1), ('U197', 6), ("<3's", 1), ('lisa', 1), ('U819', 4), ('U820', 4), ('brwn', 1), ('hurr', 1), ('Were', 1)])


# %% 24. ◑ Write expressions for finding all words in text6 that meet the conditions listed below. The result should be in the form of a list of words: ['word1', 'word2', ...].

# Ending in ise
# Containing the letter z
# Containing the sequence of letters pt
# Having all lowercase letters except for an initial capital (i.e., titlecase)

print("Cond 1: ", [w for w in text6 if w.endswith('ise')])

print("Cond 2: ", [w for w in text6 if 'z' in w])

print("Cond 3: ", [w for w in text6 if 'pt' in w])

print("Cond 4: ", [w for w in text6 if w[1:].islower()])

# %% 25. ◑ Define sent to be the list of words ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']. Now write code to perform the following tasks:

# Print all words beginning with sh
# Print all words longer than four characters
sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
print("Both Cond: ", [w for w in sent if w.startswith('sh') and len(w) > 4])

# Output:
# Both Cond:  ['shells', 'shore']


# %% 26. ◑ What does the following Python code do? sum(len(w) for w in text1) Can you use it to work out the average word length of a text?

sum(len(w) for w in text1)  # -> 999044


def avg_word_len(text) -> float:
    """Computes and prints the average word length of the input text"""
    print(
        f"Average word length of {text} is : {sum(len(w) for w in text) / len(text)}")


avg_word_len(text1)

# Output: for text1
# Average word length of <Text: Moby Dick by Herman Melville 1851> is : 3.830411128023649

# %% 27. ◑ Define a function called vocab_size(text) that has a single parameter for the text, and which returns the vocabulary size of the text.


def vocab_size(text) -> int:
    """Returns the vocabulary size of the input text"""
    return len(set(text))


text = text1
print(f"The vocabulary size of {text} is: {vocab_size(text)}")
# Output: for text1
# The vocabulary size of <Text: Moby Dick by Herman Melville 1851> is: 19317
# %% 28. ◑ Define a function percent(word, text) that calculates how often a given word occurs in a text, and expresses the result as a percentage.


def word_percentage(word: str, text) -> float:
    """Measure of Lexical richness of a word in a text.
    Form: Percentage"""
    count = text.count(word)
    total = len(text)
    return 100 * count / total


word = 'a'
text = text1
print(
    f"The lexical diversity of {word} in {text} is: {word_percentage(word, text)}")

# Output:
# The lexical diversity of a in <Text: Moby Dick by Herman Melville 1851> is: 1.7517895552087845

# %% ◑ We have been using sets to store vocabularies. Try the following Python expression: set(sent3) < set(text1).

set(sent3) < set(text1)  # -> True

set(sent5) < set(text4)  # -> False

set(sent8) < set(text2)  # -> False

set(sent1) < set(text8)  # -> False


""" END OF EXERCISE 1 from http://www.nltk.org/book/ch01.html """
