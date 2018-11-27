
import csv     
import random  
import math    
random.seed(123)

# carregando dados pra trainar   
with open('classetrain.csv')as csvfile: 
    csvreader = csv.reader(csvfile)
    next(csvreader, None) # skip header 
    datatrain = list(csvreader)

# carregando dados pra testar  
with open('classetrain.csv')as csvfile: 
    csvreader = csv.reader(csvfile)
    next(csvreader, None) # skip header 
    datateste = list(csvreader)
"""print datateste
print ("\n")
print datatrain"""

Peso1=[[0.5,0.3,0.7],[0.4,0.6,0.7]]
Peso2=[[0.8,0.9,0.1],[0.2,0.3,0.6]]


# S separa as caracteristicas das flres dos numeros corrempondentes a flores

train = [data[:4] for data in datatrain]
train_X= [data[:2] for data in train]

saidaDesejada= [data[2:] for data in train] 

#print saidaDesejada

def somatorio(dados,pesos):
    #print pesos,dados
    if type(dados[0])== str:
        x1=float(dados[0].replace(',', '.'))
        x2=float(dados[1].replace(',', '.'))
        soma=((-1)*pesos[0])+(x1*pesos[1])+(x2*pesos[2]) 
        return soma
    else: 
         x1=dados[0]
         x2=dados[1]
         soma=((-1)*pesos[0])+(x1*pesos[1])+(x2*pesos[2])
         return soma

def sigmoid(z):
    funcao= 1/((1 + math.exp(-z)))
    return funcao 

def verificar(s1,s2,saida):#verifica a qual classe da entrada
    d1=int(saida[0])
    d2=int(saida[1])
    erro=[]
    erro1=d1-s1
    erro2=d2-s2
    erro.append(erro1)
    erro.append(erro2)
    if (erro1>0 and erro1<0.4) and (erro2>0 and erro2<0.4):
        print("nao atualizar os pesos")####
    else:
        return erro  
def gradienteSaida(z,erro):
    grade=(z*(1-z)*erro)
    return grade   
      
def atualizaPeso(dados,pes1,pes2):
    p1=[]
    p2=[]
    aux1=dados[0]
    for i in xrange(len(train_X)):
        print len(train_X)
        for i in xrange(len(Peso1[0])):
            aux=dados[i]+0.5*()
                     
    


for i in xrange(len(train_X)):
    
    print ("i:",i)
    #print ("train_X:",train_X)
    Z11=somatorio(train_X[i],Peso1[0])
    Z12=somatorio(train_X[i],Peso1[1])
    y1=sigmoid(Z11)
    y2=sigmoid(Z12)
    listaX=[]
    listaX.append(y1)
    listaX.append(y2)
    Z21=somatorio(listaX,Peso2[0])
    Z22=somatorio(listaX,Peso2[1])
    s1=sigmoid(Z21)
    s2=sigmoid(Z22)
    erro=verificar(s1,s2,saidaDesejada[i])
    grade21=gradienteSaida(s1,erro[0])
    grade22=gradienteSaida(s2,erro[1])
    atualizaPeso(train_X[i],Peso2[0],Peso2[1],grade21,grade22)
    # (grade21,grade22)
    #print erro



