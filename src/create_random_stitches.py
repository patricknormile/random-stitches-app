import random
from functools import cache

def random_stitch():
    """Returns a random stitch: either "front" or "back"."""
    
    return random.choice(["Front", "Back"])
