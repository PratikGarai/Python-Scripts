from flair.data import Sentence
from flair.models import MultiTagger
from flair.tokenization import SciSpacyTokenizer

scp = SciSpacyTokenizer()
tagger = MultiTagger.load("hunflair")
