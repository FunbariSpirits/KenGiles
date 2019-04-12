import random

print("READY FIGHT!")

handList = ["グー", "チョキ", "パー"]


class ken:
    def __init__(self, name1, name2):
        self.name1 = name1
        self.name2 = name2
        # self.hand = hand

    def jan(name1, name2):
        hand1 = random.choice(handList)
        print(name1 + ":" + hand1)
        hand2 = random.choice(handList)
        print(name2 + ":" + hand2)
        if hand1 == hand2:
            print("あいこ\n")
            ken.jan(name1, name2)

        if hand1 == "グー" and hand2 == "チョキ":
            print("Winner・・・" + name1 + "!")
        if hand1 == "グー" and hand2 == "パー":
            print("Winner・・・" + name2 + "!")
        if hand1 == "チョキ" and hand2 == "パー":
            print("Winner・・・" + name1 + "!")
        if hand1 == "チョキ" and hand2 == "グー":
            print("Winner・・・" + name2 + "!")
        if hand1 == "パー" and hand2 == "グー":
            print("Winner・・・" + name1 + "!")
        if hand1 == "パー" and hand2 == "チョキ":
            print("Winner・・・" + name2 + "!")

ken.jan("わたし", "あなた")
