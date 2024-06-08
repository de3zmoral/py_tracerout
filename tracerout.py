import os
import socket

def get_public_ip():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except Exception as e:
        print(f"Не удалось определить IP-адрес пользователя: {e}")
        return None

def perform_traceroute(target):
    print(f"Начало traceroute для {target}...")
    try:
        response = os.system(f"tracert {target}")
        if response != 0:
            print("Ошибка выполнения traceroute.")
    except Exception as e:
        print(f"Ошибка выполнения traceroute: {e}")
    print("\nTraceroute завершен.")

def main():
    user_ip = get_public_ip()
    if user_ip:
        print(f"Ваш IP-адрес: {user_ip}")
    else:
        print("Не удалось определить ваш IP-адрес.")

    target = input("Введите IP-адрес или доменное имя: ")
    perform_traceroute(target)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        input("Нажмите Enter для выхода...")