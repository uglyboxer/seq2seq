import re
import requests
from bs4 import BeautifulSoup


def get_text(url):
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')

    text = soup.get_text()

    # # clean up
    # regex_remove_names = re.compile(r"[A-Z]{2,}")
    # text = regex_remove_names.sub("", text)

    regex_redundant_linebreaks = re.compile(r"\n{2,}")
    text = regex_redundant_linebreaks.sub("\n", text)
    ltext = text.split("\n")
    return ltext


def get_tags(url):
    resp = requests.get(url)
    text = resp.text
    split_text = text.split("\n")

    ltext = []
    for l in split_text:
        if l == '<T>':
            lines = []
        elif l == '</T>':
            ltext.append(lines)
        else:
            lines.append(l)

    return ltext


def get_pairs(name):

    org_url = "https://raw.githubusercontent.com/aforsyth/nfs-webscraper/355fba07d70d298597efe429fe3226d8360c49c4/output/{}_{}.txt".format(name, "original")

    mdn_url = "https://raw.githubusercontent.com/aforsyth/nfs-webscraper/355fba07d70d298597efe429fe3226d8360c49c4/output/{}_{}.txt".format(name, "modern")

    a = get_tags(org_url)
    b = get_tags(mdn_url)

    rv = list(zip(a, b))

    return rv


# name = 'hamlet'
# l = get_pairs(name)

names = ['antony-and-cleopatra', 'asyoulikeit', 'errors', 'hamlet', 'henry4pt1', 'henry4pt2',
         'henryv', 'juliuscaesar', 'lear', 'macbeth', 'merchant',
         'msnd', 'muchado', 'othello', 'richardiii', 'romeojuliet',
         'shrew', 'tempest', 'twelfthnight']


pairs = []
for name in names:
    l = get_pairs(name)
    print("Extracted {} pairs from {}...".format(len(l), name))
    pairs.extend(l)

