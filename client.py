input_string = 'Hello'
print(type(input_string))
input_bytes_encoded = input_string.encode()
print(type(input_bytes_encoded))
print(input_bytes_encoded)
output_string=input_bytes_encoded.decode()
print(type(output_string))
print(output_string)

//all'inizio i dati vengono convertiti in byte per essere comunicati al server e viceversa dal client

import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224

sock_service = socket.socket() 

sock_service.connect((SERVER_ADDRESS, SERVER_PORT))
//il client aspetta che il server accetta la connessione

print("Connesso a " + str((SERVER_ADDRESS, SERVER_PORT)))
while True:
    try:
        dati = input("Inserisci i dati da inviare (0 per terminare la connessione): ")
    except EOFError:
        print("\nOkay. Exit")
        break
    if not dati:
        print("Non puoi inviare una stringa vuota!")
        continue
    if dati == '0': 
        print("Chiudo la connessione con il server!")
        break
    //una volta connesso i dati vengono controllati con un ciclo infinito

    dati = dati.encode()
 
    sock_service.send(dati)
    //i dati,una volta codificati, vengono inviati al server.
    
    dati = sock_service.recv(2048)

    if not dati:
        print("Server non risponde. Exit")
        break
    
    dati = dati.decode()

    print("Ricevuto dal server:")
    print(dati + '\n')
     //se i dati erano vuoti la connessione 
     //si interrompe ed essi vengono comunicati dopo essere stati riconvertiti
sock_service.close()