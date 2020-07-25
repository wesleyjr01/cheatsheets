# Git Cheatsheet, pratical commands

### Adicione o nome do Usuario
```bash
$ git config --global user.name "Wesley"
```

### Adicione o email do Usuario
```bash
$ git config --global user.email "wesleyjr0101@gmail.com"
```

### Para verificar o username sendo utilizado
```bash
$ git config --global user.name
```

### Para verificar o nome de user e o email junto
```bash
$ git config --global --list
```

### Como listar todos os arquivos do diretorio atual
```bash
$ dir -a
```

### Como Criar um Repositorio Git
```bash
$ git init
```

### Agora precisamos conectar o repositório Git no seu computador com o que existe no GitHub.
```bash
$ git remote add origin https://github.com/<your-github-username>/my-first-blog.git
$ git push -u origin master
```

### Verificar Se Existe Arquivos Nao-Rastreados no repositorio
```bash
$ git status
```

### Adicionar um arquivo pro Git Rastrear
```bash
$ git add readme.txt
```

### Adicionar varios arquivos de uma vez pro Git Rastrear
```bash
$ git add .
```

### Commit para salvar mudancas
```bash
$ git commit -m "Versionamento inicial"
```

### Ver Historico de Alteracoes
```bash
$ git log
```

### Ver Historico de Alteracoes entre dois commits
```bash
$ git diff <token do commit A> <token do commit B>
```

### Usar uma versao anterior a que temos no momento
```bash
$ git checkout <token do commit B>
```

### Voltar para o estado de HEAD
```bash
$ git checkout master
```

### Para desfazer a alteracao anterior de um arquivo da repo
```bash
$ git checkout <nomedoarquivo>
```

### Para desfazer todas as alteracos para um estado anterior na repo
```bash
$ git reset --hard
```

### Clonar um repositorio
```bash
$ git clone <git url>
```

### Mandar as alteracoes devolta pro github
```bash
$ git push
```

### Baixar a versao mais atual do repositorio previamente clonado
```bash
$ git pull
```

### Baixar a versao mais atual do repositorio previamente clonado do master branch
```bash
$ git pull origin master
```


### Limpar o repositorio local e sobrescrever com alteracoes atualizadas da branch master
```bash
$ git fetch
$ git reset --hard FETCH_HEAD
$ git clean -df
```

# Branches

### Para criar uma branch nova
```bash
$ git checkout -b <nome da branch> # Cria a branch <nome da branch>, e ja muda pra ela
$ git branch <nomedabranch> # Criada a nova branch
$ git checkout <nomedabranch> # Para acessar a nova branch criada
$ git push -u origin <nomedabranch>  # Para mandar essa nova branch criada para o servidor
$ git branch -m <novo_nome> # Renomear uma branch
```

### Dar push de uma branch nova pra numvem
```bash
git push --set-upstream origin <nome_da_branch_nova>
```

### Remover uma branch localmente, nao no servidor
```bash
$ git branch -d <nomedabranch>
```

### Remover uma branch remota
```bash
$ git push origin --delete <nomedabranch>
```

### Checkar quantas branches remotas existem
```bash
$ git branch -r
```

### Mesclar as alteracoes com a branch master
```bash
$ git checkout master # Primeiramente voltamos para a branch master
$ git merge develop
$ git mergetool # Se der conflito
```

### Cancelar o Merge
```bash
$ git reset --merge
```
