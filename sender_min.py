import socket, hashlib, time

symmetric_key = 3

def encrypt_data(message):
    print("".center(80, "*"))
    print("Encrypting data...")
    t = ""
    print(message)
    for i in message:
        if i.isupper():
            alphabet = chr((ord(i) + symmetric_key - 65) % 26 + 65)
        elif i.islower():
            alphabet = chr((ord(i) + symmetric_key - 97) % 26 + 97)
        else:
            alphabet = chr(ord(i) + symmetric_key)
        t = t + alphabet
    return t

def hash_data(messageToSent):
    print("".center(80, "*"))
    print("Computing the hash of the data...")
    hashedData = hashlib.md5(messageToSent.encode())
    hashedDataByte = hashedData.hexdigest()
    return hashedDataByte

def makeConnection():
    senderSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    port = 9999
    senderSocket.bind((host, port))
    print("Socket binded to ", port)
    senderSocket.listen(5)
    print("Socket is listening for client connections")
    clientSocket, address = senderSocket.accept()
    print("Got a connection from client with address ", str(address))
    messageToSent = "This is a data to be sent to the receiver 123."
    hashedData = hash_data(messageToSent)
    encryptedData_Key = encrypt_data(messageToSent)
    dataToSent = '{"Message":"' + encryptedData_Key + '","Key":"' + str(symmetric_key) + '","Hash":"' + str(hashedData) + '"}'
    clientSocket.send(dataToSent.encode('ascii'))
    print("".center(80, "*"))
    print("Data is sent successfully")
    dataToSent = '{"Message":"' + encryptedData_Key + '","Key":"' + "" + '","Hash":"' + str(hashedData) + '"}'
    clientSocket.send(dataToSent.encode('ascii'))
    print("".center(80, "*"))
    print("Data is sent successfully")
    print("".center(80, "*"))
    dataToSent = '{"Message":"' + "" + '","Key":"' + "" + '","Hash":"' + "" + '"}'
    time.sleep(10)
    clientSocket.send(dataToSent.encode('ascii'))
    clientSocket.close()
    print("Connection closed...\nThank you")

print("".center(80, "*"))
print("\t\t\t\t\tSender")
print("".center(80, "*"))
makeConnection()
