import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9999))
server.listen(1)
print("Server started. Waiting for client...")
conn, addr=server.accept()
print("Connected to:", addr)
while True:
    data=conn.recv(1024).decode()
    if not data:
        break
    num1, operator, num2 = data.split(",")
    num1=float(num1)
    num2=float(num2)
    if operator=="+":
        result=num1+num2
    elif operator=="-":
        result=num1-num2
    elif operator=="*":
        result=num1*num2
    elif operator=="/":
        if num2==0:
            result="Cannot divide by zero"
        else:
            result=num1/num2
    else:
        result="Invalid operator"

    conn.send(str(result).encode())

conn.close()
server.close()
