from random import randint
from flask import Flask

ips: list[str] = []
app = Flask(__name__)

class GenerateIp:
    def __init__(self) -> None:
        self.ip = self.GenerateNewIp()
        ips.append(self.ip)

    def GenerateNewIp(self) -> str:
        while True:
            ip_parts = []
            
            for _ in range(4):
                rand_num = randint(0, 2)
                
                ip_parts.append(str(randint(0, 255))) if rand_num == 0 else \
                ip_parts.append(str(randint(0, 99))) if rand_num == 1 else ip_parts.append(str(randint(0, 9)))
            
            new_ip = '.'.join(ip_parts)
            
            if new_ip not in ips:
                return new_ip

@app.route('/')
def Ip() -> str:
    test_ips = []

    for _ in range(5):
        new_ip = GenerateIp()
        test_ips.append(new_ip.ip)

    response = '<h1>Randomly Generated IPs:</h1>'
    response += '<ul>'
    
    for ip in test_ips:
        response += f'<li>{ip}</li>'
    
    response += '</ul>'
    
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)
