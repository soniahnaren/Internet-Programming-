import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9999))
print("Connected to server")
while True:
    num1 = input("Enter first number: ")
    operator = input("Enter operator (+, -, *, /): ")
    num2 = input("Enter second number: ")

    message = f"{num1},{operator},{num2}"
    client.send(message.encode())
    result = client.recv(1024).decode()
    print("Result:", result)
    choice = input("Do you want to continue? (y/n): ")

    if choice.lower() != "y":
        break

client.close()

