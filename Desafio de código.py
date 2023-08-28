saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    operação= input("""
     ******** MENU ******** 
      
      [1] Depositar
      [2] Sacar
      [3] Extrato
      [4] Sair

      """)

    if operação == "1":
        valor = float(input("""
     Digite o valor de deposito: R$"""))
        if valor>0:
              saldo+=valor
              extrato+=f"Deposito: R${valor}\n"
            
        else:
             print("""
     Operação inválida, nao eh possivel depositar um valor negativo""")

    elif operação=="2":
         valor = float(input("""
      Digite o valor do saque: R$"""))
         if valor>saldo:
                print("""
        Operação invalida, nao eh possivel sacar um valor maior que o seu saldo""")
         elif valor>limite:
                print("""
        Operação invalida, nao eh possivel sacar um valor maior que R$500 por vez""")
         elif numero_saques>=LIMITE_SAQUES:
                    print("""
        Operação invalida, nao eh possivel sacar mais de 3 vezes no dia""")
         elif valor>0:
            saldo-=valor
            extrato+=f"Saque: R${valor}/n"
            numero_saques+=1
         else:
               print("""
         Operação invalida, nao eh possivel sacar um valor negativo""")
    
    elif operação == "3":
          print("******** EXTRATO ********")
          print("Não foram realizadas movimentacoes na sua conta"if not extrato else extrato) 
          print(f"\nSaldo: R$ {saldo}")
          print("*************************")
    elif operação == "4":
          break
    else:
     print ("""
        Operação invalida, por favor siga as instrucoes do menu de comando""")

