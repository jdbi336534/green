import os


def change():
    file = open("zero.md", "a+")
    file.write('0')
    file.close()


def commit():
    os.system('git commit -a -m test_github_streak')


if __name__ == '__main__':
    commit()

