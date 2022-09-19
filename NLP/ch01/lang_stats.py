# %% Import and downloads
from nltk.book import *
import nltk
texts()
# Output:

# *** Introductory Examples for the NLTK Book ***
# Loading text1, ..., text9 and sent1, ..., sent9
# Type the name of the text or sentence to view it.
# Type: 'texts()' or 'sents()' to list the materials.
# text1: Moby Dick by Herman Melville 1851
# text2: Sense and Sensibility by Jane Austen 1811
# text3: The Book of Genesis
# text4: Inaugural Address Corpus
# text5: Chat Corpus
# text6: Monty Python and the Holy Grail
# text7: Wall Street Journal
# text8: Personals Corpus
# text9: The Man Who Was Thursday by G . K . Chesterton 1908
# %% Py basics on list of texts
sent = ['After', 'all', 'is', 'said', 'and', 'done',
        'more', 'is', 'said', 'than', 'done']

tokens = set(sent)
tokens = sorted(tokens)
tokens[-2:]

# Output:
# ['said', 'than']

"""Frequency Distribution"""
# %%
fdist1 = FreqDist(text1)  # Total number of words that have been counted up
print(fdist1)

# Output
# <FreqDist with 19317 samples and 260819 outcomes>

fdist1.most_common(50)  # 50 most frequently occuring types in the text

# Output
# [(',', 18713),
#  ('the', 13721),
#  ('.', 6862),
#  ('of', 6536),
#  ('and', 6024),
#  ('a', 4569),
#  ('to', 4542),
#  (';', 4072),
#  ('in', 3916),
#  ('that', 2982),
#  ("'", 2684),
#  ('-', 2552),
#  ('his', 2459),
#  ('it', 2209),
#  ('I', 2124),
#  ('s', 1739),
#  ('is', 1695),
#  ('he', 1661),
#  ('with', 1659),
#  ('was', 1632),
#  ('as', 1620),
#  ('"', 1478),
#  ('all', 1462),
#  ('for', 1414),
#  ('this', 1280),
# show more (open the raw output data in a text editor) ...

#  ('were', 680),
#  ('now', 646),
#  ('which', 640),
#  ('?', 637),
#  ('me', 627),
#  ('like', 624)]

# Generate cumulative frequency plot for the given amount of words
fdist1.plot(50, cumulative=True)

# Output:
# cumulative frequency plot located at "plots/freq_dist.png"


"""Fine grained Selection of Words"""
# %% The set of all w such that w is an element of V and length of w is greater than 15

V = set(text1)
long_words = [w for w in V if len(w) > 15]
sorted(long_words)

# Output:
# ['CIRCUMNAVIGATION',
#  'Physiognomically',
#  'apprehensiveness',
#  'cannibalistically',
#  'characteristically',
#  'circumnavigating',
#  'circumnavigation',
#  'circumnavigations',
#  'comprehensiveness',
#  'hermaphroditical',
#  'indiscriminately',
#  'indispensableness',
#  'irresistibleness',
#  'physiognomically',
#  'preternaturalness',
#  'responsibilities',
#  'simultaneousness',
#  'subterraneousness',
#  'supernaturalness',
#  'superstitiousness',
#  'uncomfortableness',
#  'uncompromisedness',
#  'undiscriminating',
#  'uninterpenetratingly']

# %% all words from the chat corpus that are longer than seven characters, that occur more than seven times:
fdist5 = FreqDist(text5)
sorted(w for w in set(text5) if len(w) > 7 and fdist5[w] > 7)

# Output:
# ['#14-19teens',
#  '#talkcity_adults',
#  '((((((((((',
#  '........',
#  'Question',
#  'actually',
#  'anything',
#  'computer',
#  'cute.-ass',
#  'everyone',
#  'football',
#  'innocent',
#  'listening',
#  'remember',
#  'seriously',
#  'something',
#  'together',
#  'tomorrow',
#  'watching']
# %%
"""A collocation is a sequence of words that occur together unusually often. Thus red wine is a collocation, whereas the wine is not. A characteristic of collocations is that they are resistant to substitution with words that have similar senses; for example, maroon wine sounds definitely odd.

To get a handle on collocations, we start off by extracting from a text a list of word pairs, also known as bigrams. This is easily accomplished with the function bigrams():"""

list(bigrams(['more', 'is', 'said', 'than', 'done']))

# Output:
# [('more', 'is'), ('is', 'said'), ('said', 'than'), ('than', 'done')]

# %% Using collocation() method

text4.collocations()

# Output:
# United States; fellow citizens; four years; years ago; Federal
# Government; General Government; American people; Vice President; God
# bless; Chief Justice; Old World; Almighty God; Fellow citizens; Chief
# Magistrate; every citizen; one another; fellow Americans; Indian
# tribes; public debt; foreign nations
# %%
