# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
# com as seguintes informações:
# - Quantidade de notas.
# - A maior nota.
# - A menor nota.
# - A média da turma.
# - A situação (opcional).
# Adicione também as docstrings da função.


def notas(* notas, situacao=False):
    """
    -> Função para analiasr notas e situações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias).
    :param situacao: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """

    nota = dict()
    nota["total"] = len(notas)
    nota["maior"] = max(notas)
    nota["menor"] = min(notas)
    nota["média"] = sum(notas) / len(notas)

    if situacao:
        if nota["média"] >= 7:
            nota["situação"] = "BOA"
        elif nota["média"] >= 5:
            nota["situação"] = "RAZOÁVEL"
        else:
            nota["situação"] = "RUIM"

    return nota


resultado = notas(3.5, 2, 6.5, 2, 7, 4, situacao=True)
print(resultado, end="\n\n")
help(notas)
