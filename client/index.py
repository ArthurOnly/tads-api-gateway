import httpx

API_URL = 'http://localhost:5000'

def interface():
    print("------------------")
    print("1 - Listar usuarios        ")
    print("2 - Cadastrar usuarios     ")
    print("3 - Deletar usuarios       ")
    print("4 - Listar filmes          ")
    print("99 - Sair                  ")

def handle_choice(choice):
    if choice == 1:
        print(handle_list_users())
    elif choice == 2:
        print(handle_create_users())
    elif choice == 3:
        print(handle_delete_users())
    elif choice == 4:
        print(handle_list_movies())
    elif choice == 99:
        return True
    return False

def handle_list_movies():
    return httpx.get(f"{API_URL}/movies").text

def handle_list_users():
    return httpx.get(f"{API_URL}/users").text

def handle_create_users():
    username = input("Insira um username: ")
    email = input("Insira um email: ")
    return httpx.post(f"{API_URL}/users", data={'username': username, 'email': email}).text

def handle_delete_users():
    id = int(input("Insira um ID: "))
    return httpx.delete(f"{API_URL}/users/{id}").text

def start():
    while True:
        interface()
        choice = int(input("Selecione uma opção: "))
        is_exit = handle_choice(choice)
        if is_exit:
            break

if __name__ == '__main__':
    start()