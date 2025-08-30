from pathlib import Path
import typer

from etlab_cli.pipelines.parser import parse_pipeline

app = typer.Typer()

@app.command(help='Mostra versão do etlab-cli')
def version() -> None:
    print('Version command')

@app.command(help='Executa pipeline definida no arquivo yaml')
def run(path: Path) -> None:
    result = parse_pipeline(path)
    if result.is_ok():
        pipeline = result.ok
        print(pipeline.name)
    else:
        err = result.error
        print(err)

if __name__ == '__main__':
    app()

