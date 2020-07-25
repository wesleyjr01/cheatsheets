## Very Basic Linux Commands (Ubuntu Examples)

* Be the root

```bash
$ sudo su -
```

* Leave root user mode

```bash
$ exit
```

* Get Help

```bash
$ command --help
$ man command
$ whatis command
```

* Where is?

```bash
$ whereis date
```

* Move to root directory

```bash
$ cd /
```

* Show my current directory

```bash
$ pwd
```

* Move to home directory

```bash
$ cd ~
```


* Create a directory

```bash
$ mkdir dir_name
```

* Remove file from directory

```bash
$ rm arquivo
$ rm -r Aula1
```

# Grep

* Syntax:

```bash
$ grep option search_pattern file_path
```

* Problem: We want to find where the library ggplot was used in any script in the directory r_project.

```bash
$ grep -rn ggplot r_project/
```

* option -r stands for recursion

* option -n tells grep to show the line numbers

* Problem: Given a directory composed of subdirectories whose names contain a date, we want to get the complete name of one or more subdirectories containing a date like 2018_05.

```bash
$ ls models_by_date/ | grep 2018_05
```

# Workspaces

* Mover um processo atual para outro workspace:

`CRTL + ALT + SHIFT + PgDown`

* Navegar entre Workspaces:

`CTRL + ALT + PgUp/PgDown`

* Maximiza a tela do Workspace Atual

`Super + PgUp`

* Setar para Esquerda o processo do Workspace Atual

`Super + PgLeft`

* Setar para Direita o processo do Workspace Atual

`Super + PgRight`
