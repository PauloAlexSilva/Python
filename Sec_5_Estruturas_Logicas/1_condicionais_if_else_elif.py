"""
Estruturas condicionais
if, else, elif(else if)


"""

"""
# Estrutura condicional if, else em C

if(idade < 18){
    print("Menor de idade");
}else if(idade == 18){
    printf("Tem 18 anos!");
}else{
    printf("Maior de idade!);
}

# Estrutura condicional if, else em Java

if(idade < 18){
    System.out.println("Menor de idade");
}else if(idade == 18){
    System.out.println("Tem 18 anos!");
}else{
    System.out.println("Maior de idade!);
}
"""

idade = 26

if idade < 18:
    print('\nMenor de idade!')
elif idade == 18:
    print('\nTem 18 anos!')
elif idade == 26:
    print('\nTem 26 anos!')
else:
    print('\nMaior de idade!')
