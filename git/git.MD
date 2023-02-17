Iniciando um repositorio

<git init >


Adicionar um arquivo | Sem aspas ao digitar o nome do arquivo

<git add 'seu arquivo' >
Exemplo <git add hello-world.py >


Adicionar todos arquivos do diretorio

<git add . >


Fazer um commit | é obrigatorio o uso das aspas apos o '-m'. Não as esqueãs ;)

< git commit -m 'sua mensagem' >
Exemplo <git commit -m 'Primeiro commit diretorio vazio' >

Exemplo <git commit -m 'Arquivo hello-world.py acriado'>


Verificar o status

<git status>


Verificar log

<git log>


Remover um arquivo adicionado no 'git add' antes de fazer o 'commit'
_ nome do arquivo sem aspas

[Use o comando <git status> paara ver os arquivos que estão adicionados]

<git rm --cached 'nome do arquivo'>
Exemplo <git rm --cached hello-world2.py>