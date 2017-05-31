"""Generate markov text from text files."""


from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_string = open(file_path)

    return text_string.read()


def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
    """

    chains = {}

    # separates string into words
    word_list = text_string.split()


    # loops through range of word_list and stops when only 2 words remain
    for index in range(len(word_list) - 2):
        # creates tuples that will be keys in chains dict
        bigram = (word_list[index], word_list[index + 1])
        # if key does not exist in chains dict, create empty list as value
        if bigram not in chains:
            chains[bigram] = []

        chains[bigram].append(word_list[index + 2])

    return chains


def make_text(chains):
    """Returns text from chains."""

    # assigned randomly selected tuple from chains dictionary to variable bigram
    bigram = choice(chains.keys())

    # converted bigram tuple to list and assigned to variable words
    # this will allow adding additional strings and joining into one string
    words = list(bigram)

    # used while loop to iterate over dictionary because output should have
    # random length
    # for loop would only iterate a fixed number of times
    while bigram != ('I', 'am?'):

        posible_words = chains[bigram]
        new_word = choice(posible_words)
        words.append(new_word)
        bigram = tuple(words[-2:])

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
