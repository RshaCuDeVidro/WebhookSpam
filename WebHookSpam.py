import time
from dhooks import Webhook
print('''
          ██                    ██  ██              
        ██  ██                ██      ██            
        ██    ██              ██  ██  ██            
      ██  ██  ██              ██  ██    ██          
      ██  ██    ██          ██    ██    ██          
      ██  ████  ██████████████    ████    ██        
      ██  ████████████████████▓▓██████  ████        
      ██  ██████████████████████████████░░██        
      ██  ██████████████████████████████    ██      
      ██▓▓██████░░░░██████████████████████  ██      
      ████████      ░░████░░▒▒████████████████      
      ████████        ████    ████████████████      
    ████████░░        ████        ██████████░░▓▓    
    ██  ████  ████    ████    ████  ██████    ██    
    ██    ██    ██▓▓  ████  ████                ▓▓  
  ▓▓░░    ░░    ████  ████  ████                ██  
  ██            ██    ████                      ████
  ██                  ░░                        ░░██
  ██                ██████                        ██
  ████            ██████████                    ████
  ░░██        ██  ░░██████      ██            ▓▓  ██
    ████      ▒▒██  ▒▒██      ▓▓██          ██▒▒  ██
    ██████      ██    ██    ████          ██      ██
      ██████      ▓▓▓▓████▓▓░░██                ██░░
      ██  ████      ██  ██  ██          ██      ██  
    ████  ████      ██  ██  ██                  ██  
    ████  ░░██      ██    ██▒▒                  ░░██
    ████    ██        ████                        ██
  ██  ████  ████      ░░                          ██
  ██  ████    ████                                ██
  ██  ████      ████                              ██
  ██  ██░░██    ░░████                            ██
  ██  ██  ▒▒██      ▒▒░░                          ██
  ██  ██      ██        ██                          
  ██  ░░██                                          
    ██  ██                                          
    ██    ██                                        
''')
time.sleep(0.4)
print('-------------------------------------------------------------------------------------------------------')
print("""8888888b.                    888           88888888888                888 """)
print("""8888888b.                    888           88888888888                888 """)
print("""888    888                   888               888                    888 """)
print("""888   d88P 888  888 .d8888b  88888b.   8888b.  888   .d88b.   .d88b.  888 """)
print("""8888888P"  888  888 88K      888 "88b     "88b 888  d88""88b d88""88b 888 """)
print("""888 T88b   888  888 "Y8888b. 888  888 .d888888 888  888  888 888  888 888 """)
print("""888  T88b  Y88b 888      X88 888  888 888  888 888  Y88..88P Y88..88P 888 """)
print("""888   T88b  "Y88888  88888P' 888  888 "Y888888 888   "Y88P"   "Y88P"  888 """)
print("""                888              """)
print("""           Y8b d88P    """)
print("""            "Y88P"  """)
print('-------------------------------------------------------------------------------------------------------')
a = input('COLOQUE O WEBHOOK(url): ')
b = input('COLOQUE O TEXTO PARA SPAM: ')
c = float(input('TEMPO ENTRE AS MENSAGENS:' ))
d = input('NOME DO BOT: ')
webamount = int(input('QUANTIDADE DE MENSAGEM: '))
x=1
hook = Webhook(a)
hook.modify(name=d)

while x <= (webamount):
    print(x)
    hook.send(b)
    time.sleep(c)
    x += 1

