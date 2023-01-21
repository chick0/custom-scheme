from re import compile
from sys import argv
from sys import exit as _exit
from subprocess import call

PREFIX = "p-launcher://"
RE = compile(r"^([0-9])+$")


def exit(code: int):
    input()
    _exit(code)


def main():
    try:
        arg = argv[1]
    except IndexError:
        print("전달받은 URI가 없습니다.")
        exit(-1)

    if not arg.startswith(PREFIX):
        print("올바른 URI가 아닙니다.")
        exit(-2)

    # Prefix removed argument
    arg = arg[len(PREFIX):]
    arg_s = arg.split("/")

    try:
        command = arg_s[0]
    except IndexError:
        print("명령이 비어있습니다.")
        exit(-3)

    if command == "game":
        try:
            game_id = arg_s[1]
        except IndexError:
            print("요청에 게임 아이디가 없습니다.")
            exit(-4)

        match = RE.match(game_id)

        if match is None:
            print("올바른 게임 아이디가 아닙니다.")
            exit(-1)

        call(f"start C:\\p-launcher\\game.exe {game_id}", shell=True)
        exit(0)
    else:
        print("등록된 커맨드가 아닙니다.")
        exit(-404)


if __name__ == "__main__":
    main()
