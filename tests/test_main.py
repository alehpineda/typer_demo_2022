from typer.testing import CliRunner

from typer_demo_2022.main import app

runner = CliRunner()


def test_main_hola_mundo():
    resultado = runner.invoke(app)
    assert resultado.exit_code == 0
    print(resultado.stdout, type(resultado.stdout))
    assert "Hola mundo!" in resultado.stdout
