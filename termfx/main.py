import os
import time
import termfx

def clear():
    os.system("cls")

def main():
    registry = termfx.New()
    registry.register_variable("username", "root")
    registry.register_variable("botcount", "61951")
    registry.register_variable("apicount", "5")

    with open("example.tfx", encoding="utf-8") as f:
        print(registry.execute(f.read()))

if __name__ == "__main__":
    main()