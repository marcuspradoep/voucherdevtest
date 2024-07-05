alunos = [("joao",8.0),("maria",9.5),("pedro",7.5),("ana",8.5)]
maior_nota = 0 
aluno_maior_nota = ""

for aluno,nota in alunos:
    if nota > maior_nota:
        maior_nota = nota
        aluno_maior_nota = aluno

print(f"o aluno com a maior nota é: {aluno_maior_nota}")