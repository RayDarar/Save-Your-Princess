import GameControl, os, sys

#Точка входа программы
def main():
    os.system("cls")
    control = GameControl.GameControl();

    res = ""
    while True:
        os.system("cls")
        res = input("Save your Princess\n\n1)Новая игра (Удалит последнюю игру!)\n2)Продолжить\n3)Exit\n")
        if (res == '1'):
            control = GameControl.GameControl();
            control.setGameMode(0);
            input()
        elif (res == '2'):
            control.setGameMode(1);
            input()
        elif (res == '3'):
            break;
        pass
    return 0

if __name__ == "__main__":
    sys.exit(int(main() or 0))
