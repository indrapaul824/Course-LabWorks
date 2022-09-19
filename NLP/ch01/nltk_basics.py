'''Getting Started'''
"""import nltk
nltk.download()"""

# %% Import and downloads
# %%
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


'''Searching Text'''
# %%
text1.concordance("monstrous")
#  Output:
# Displaying 11 of 11 matches:
# ong the former , one was of a most monstrous size . ... This came towards us ,
# ON OF THE PSALMS . " Touching that monstrous bulk of the whale or ork we have r
# ll over with a heathenish array of monstrous clubs and spears . Some were thick
# d as you gazed , and wondered what monstrous cannibal and savage could ever hav
# that has survived the flood ; most monstrous and most mountainous ! That Himmal
# they might scout at Moby Dick as a monstrous fable , or still worse and more de
# th of Radney .'" CHAPTER 55 Of the Monstrous Pictures of Whales . I shall ere l
# ing Scenes . In connexion with the monstrous pictures of whales , I am strongly
# ere to enter upon those still more monstrous stories of them which are to be fo
# ght have been rummaged out of this monstrous cabinet there is no telling . But
# of Whale - Bones ; for Whales of a monstrous size are oftentimes cast up dead u
# %%
text4.concordance("advantage")
# Output:
# Displaying 18 of 18 matches:
# e and happiness ; between duty and advantage ; between the genuine maxims of an
# uch cases choice would have little advantage to boast of over lot or chance . S
#  honorable treaty , and with great advantage to the original States ; the State
# ve to carry them into effect . The advantage of these fortifications and of an
# l peace a band of adventurers took advantage of this conflict and of the facili
# oans may be resorted to with great advantage . I am equally well satisfied , as
# be considered it would appear that advantage must result from the observance of
#  interests can rightfully claim an advantage over the others , or to be enriche
# by the conviction that no apparent advantage can be purchased at a price so dea
# m no exception . Unwilling to take advantage of the fortune of war against a si
# obligations or to obtain an unjust advantage over others . They will presently
# es of other powers into commercial advantage to ourselves . We have a just righ
# No political party can long pursue advantage at the expense of public honor or
#  prevent other nations from taking advantage of us and of our inability to defe
# d . We desire neither conquest nor advantage . We wish nothing that can be had
# servations no special privilege or advantage but only to clarify our relation t
# we have fought not for our selfish advantage , but to help others resist aggres
# people . Let us put aside personal advantage , so that we can feel the pain and

# %%
text1.similar("monstrous")
# Output:
# true contemptible christian abundant few part mean careful puzzled
# mystifying passing curious loving wise doleful gamesome singular
# delightfully perilous fearless

# %%
text7.similar("unjust")
# Output:
# scheduled reported said likely about expected thought next japanese
# trying seeking possible subject set japan attached beginning able paid
# believed
# %%
text2.common_contexts(["monstrous", "very"])
# Output
# a_pretty am_glad a_lucky is_pretty be_glad

# %%
text4.dispersion_plot(
    ["citizens", "democracy", "freedom", "duties", "America"])
# Output
# dispersion plot located at plots/dispersion.png


'''Counting Vocabulary'''
# %% Count the length of a text in terms of the words and punctuations
len(text3)

# Output:
# 44764

# %% Wrapping sorted() around set(text3) -> List of Vocabulary Items
sorted(set(text3))

# Output:
# ['!',
#  "'",
#  '(',
#  ')',
#  ',',
#  ',)',
#  '.',
#  '.)',
#  ':',
#  ';',
#  ';)',
#  '?',
#  '?)',
#  'A',
#  'Abel',
#  'Abelmizraim',
#  'Abidah',
#  'Abide',
#  'Abimael',
#  'Abimelech',
#  'Abr',
#  'Abrah',
#  'Abraham',
#  'Abram',
#  'Accad',
#  ...
#  ...
#  'co',
#  'coat',
#  'coats',
#  'coffin',
#  'cold',
#  ...]

# %% Check the size of the vocabulary
len(set(text3))

# Output:
# 2789

# %% Measure of Lexical richness of the text
len(set(text3)) / len(text3)

# Output
# 0.06230453042623537
# This means that the number of distinct words is just 6% of the total number of the words

# %% Measure of Lexical Richness of a word

100 * text4.count('a') / len(text4)

# Output:
# 1.457973123627309
# This is the percentage of text4 taken up by the word

# %% Methods to automate the above


def lexical_diversity(text) -> float:
    """Measure of Lexical richness of the text as a whole."""
    return len(set(text)) / len(text)


def word_percentage(word: str, text) -> float:
    """Measure of Lexical richness of a word in a text."""
    count = text.count(word)
    total = len(text)
    return 100 * count / total


# %%
print(f"The Lexical Diversity of text3 is: {lexical_diversity(text3)}")
print(f"The Lexical Diversity of text6 is: {lexical_diversity(text6)}")
print(
    f"The Lexical Diversity percentage of a in text4 is: {word_percentage('a', text4)}")

# %%
