from sys import argv

from client import RE
from client import exit


def main():
    try:
        game_id = argv[1]
    except IndexError:
        print("게임 아이디가 없습니다.")
        exit(-1)

    match = RE.match(game_id)

    if match is None:
        print("올바른 게임 아이디가 아닙니다.")
        exit(-2)

    print(f"게임 아이디 {game_id!r}가 실행되고 있습니다.")
    exit(0)


if __name__ == "__main__":
    main()
