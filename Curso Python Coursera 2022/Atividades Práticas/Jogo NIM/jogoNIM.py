def computador_escolhe_jogada(n, m):
  jogada_vencedora = jogadaVencedora(n,m)
  if jogada_vencedora!=-1 and jogada_vencedora<m:
    pecas_retirar = jogada_vencedora
  else:
    pecas_retirar=m
  return pecas_retirar

def jogadaVencedora(n, m):
  jogada_vencedora=-1
  for i in range(m):
    if (n-i)%(m+1)==0:
      jogada_vencedora=i
  return jogada_vencedora

def usuario_escolhe_jogada(n, m):
  pecas_retirar=m+1
  while pecas_retirar>m:
    pecas_retirar = int(input("Quantas peças você vai retirar? "))
    if n-pecas_retirar<0 or pecas_retirar>m:
      print("Oops! Jogada inválida! Tente de novo.") 
      pecas_retirar=m+1
  return pecas_retirar
  
def partida():
  vez_comput=False
  pecas_retiradas_comput=pecas_retiradas_vitima=vitima=comput=0
  n=m=-1
  
  while n<0 or m<0:
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

  if n%(m+1)==0:
    print("\nVocê começa!")
  else:
    print("\nComputador começa!")
    vez_comput=True
  
  while n>0:
    if vez_comput: 
      pecas_retiradas_comput = computador_escolhe_jogada(n, m)
      comput+=pecas_retiradas_comput
      vez_comput=False
      n-=pecas_retiradas_comput
      print("\nO computador retirou {0} peça(s)\nAgora resta(m) {1} peça(s) no tabuleiro\n".format(pecas_retiradas_comput, n))
    else:
      pecas_retiradas_vitima = usuario_escolhe_jogada(n,m)
      vitima+=pecas_retiradas_vitima
      n-=pecas_retiradas_vitima
      vez_comput=True
      print("\nVocê retirou {0} peça(s)\nAgora resta(m) {1} peça(s) no tabuleiro\n".format(pecas_retiradas_vitima, n))
    
  if comput>vitima:
    print("Fim do Jogo! O computador ganhou!")
    return True

  else:
    print("Fim do Jogo! Você ganhou!")
    return False

def campeonato(opcao_partida):
  rodada=1
  computador=vitima=0
  if opcao_partida==1:
    print("\n**** RODADA ÚNICA ****")
    resultado = partida()
    if resultado:
      computador+=1
    else:
      vitima+=1
  
  else:
    for i in range(3):
      print("\n**** RODADA {0} ****".format(rodada))
      resultado = partida()
      if resultado:
        computador+=1
      else:
        vitima+=1
      rodada+=1
    print("**** Final do Campeonato! ****")
  
  print("\nPlacar: Você {0} X {1} Computador".format(vitima, computador))

def main():
  opcao_partida=0
  print("Bem-Vindo ao jogo do NIM! Escolha:\n")
  print("1 - para jogar uma partida isolada\n2 - para jogar um campeonato\n")
  while opcao_partida<1 or opcao_partida>2:
    opcao_partida = int(input())
  campeonato(opcao_partida)

main()