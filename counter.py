class MyCounterV1:
    def __init__(self, value):
        self.value = value

    def count_up(self):
        self.value += 1

class MyCounterV2:
    def __init__(self, value, step):
        self.value = value
        self.step = step

    def count_up(self):
        self.value += self.step

class MyCounterV3:
    def __init__(self, value, step):
        self.value = value
        self.step = step

    def count_up(self):
        self.value += self.step

    def count_down(self):
        self.value -= self.step


def main():
    # 課題B-3
    counter1 = MyCounterV1(value=0)
    print(counter1.value)  # 0

    counter1.count_up()
    print(counter1.value)  # 1

    counter1.count_up()
    print(counter1.value)  # 2

    # 課題B-4
    counter2 = MyCounterV2(value=0, step=3)
    print(counter2.value)

    counter2.count_up()
    print(counter2.value)  # 3

    counter2.count_up()
    print(counter2.value)  # 6

    # 課題B-5
    counter3 = MyCounterV3(value=1, step=2)
    print(counter3.value)  # 1

    counter3.count_up()
    print(counter3.value)  # 3

    counter3.count_up()
    print(counter3.value)  # 5

    counter3.count_down()
    print(counter3.value)  # 3


if __name__ == "__main__":
    main()
