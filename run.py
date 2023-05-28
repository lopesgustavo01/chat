from app import clients, run_flask_app, handle_client
import threading

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.start()

    while True:
        # Verifica se há novos clientes e cria uma nova thread para cada um
        new_clients = set(clients)
        for client_thread in new_clients:
            if not client_thread.is_alive():
                # A thread do cliente não está mais ativa, remove-a da lista de clientes
                clients.remove(client_thread)
            else:
                # Manipule as ações específicas do cliente na thread separada
                handle_client(client_thread)
