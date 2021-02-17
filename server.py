import socket



SERVER_ADDRESS = '127.0.0.1'

SERVER_PORT = 22224

sock_listen = socket.socket() //_accettazioni delle richieste del client 

sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) //_la porta viene liberata in automatico

sock_listen.bind((SERVER_ADDRESS, SERVER_PORT))

sock_listen.listen(5) //mettiamo un limite di 5 richieste dai client

print("Server in ascolto su %s." % str((SERVER_ADDRESS, SERVER_PORT)))


while True:
    sock_service, addr_client = sock_listen.accept()
    print("\nConnessione ricevuta da " + str(addr_client))
    print("\nAspetto di ricevere i dati ")
    contConn=0
    while True:
        dati = sock_service.recv(2048)
        contConn+=1
        if not dati:
            print("Fine dati dal client. Reset")
            break
        //una volta accetta la richiesta, il contatore di esse si incrementa di 
        //uno e se non ci sono dati la connessione si interrompe   
        
        dati = dati.decode()
        print("Ricevuto: '%s'" % dati)
        if dati=='0':
            print("Chiudo la connessione con " + str(addr_client))
            break
        dati = "Risposta a : " + str(addr_client) + ". Il valore del contatore è : " + str(contConn)

        dati = dati.encode()

        sock_service.send(dati)
        // una volta ricodificati i dati in byte,vengono rinviati al server.
    sock_service.close()