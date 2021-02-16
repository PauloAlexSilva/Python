"""
Módulos Customizados

Como módulos Python são arquivos Python, então TODOS os arquivos que foram criados são módulos Python
prontos para serem utilizados.


# Importando uma função específica do nosso módulo

from Sec_8_funcoes.c_funcoes_com_parametro import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# Importando todo o módulo (Temos acesso a TODOS os elementos do módulo)

import Sec_8_funcoes.c_funcoes_com_parametro as fcp


# Estamos aceder e imprimir uma variável contida no módulo

print(fcp.lista)

print(fcp.tupla)

print(fcp.soma_impares(fcp.lista))


"""

from Sec_10_expr_lambdas_fun_integradas.b_map import cidades, c_para_f

print(list(map(c_para_f, cidades)))
