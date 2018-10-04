from .GeradorCPF import gerador_cpf

def GeradorListaCPF(quantidade_cpf):
    # Lista com quebra de linha
    cpfs = ''
    while quantidade_cpf > 0:
        cpfs += gerador_cpf() + '\n'
        quantidade_cpf -= 1

    return cpfs


    # Salvar arquivos localmente
    # arquivo = open('ListaCPF.txt', 'a')
    # for cpf in lista_cpf:
    #     arquivo.write(cpf)
    #     arquivo.write('\n')

    # Gerar lista literalmente, porém com formatação fraca
    # lista_cpf = []
    # while len(lista_cpf) < quantidade_cpf:
    #     lista_cpf.append(gerador_cpf())
    #
    # return str(lista_cpf).strip('[]')