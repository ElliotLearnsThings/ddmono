def hashtab(songs, attribute: str):
    return {getattr(s, attribute): s for s in songs}
