if __name__ == "__main__":
    poem = """
        My kitty cat likes %s,
        My kitty cat likes %s
        My kitty cat fell on his %s
        And now thinks he's a %s"""

    args = ("roast beef", "ham", "head", "clam")

    print(poem % args)
