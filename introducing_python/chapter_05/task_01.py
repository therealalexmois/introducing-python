song = """
    When an eel grabcs your arm,
    And it causes great harm,
    That's - a moray!"""

if __name__ == "__main__":
    ans_1 = song.replace("moray", "Moray")
    ans_2 = song[:-6] + "M" + song[-5:]

    print(ans_1)
    print(ans_2)
