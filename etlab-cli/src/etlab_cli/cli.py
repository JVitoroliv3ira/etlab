import typer

app = typer.Typer()

@app.command(help='Mostra versão do etlab-cli')
def version() -> None:
    print('Version command')

@app.command(help='Executa pipeline definida no arquivo yaml')
def run() -> None:
    print('Run command')

if __name__ == '__main__':
    app()

