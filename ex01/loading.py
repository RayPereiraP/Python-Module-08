import sys
import importlib.metadata
from typing import Dict, List, Tuple


def check_dependencies() -> bool:
    """
    Verifica se as dependências necessárias estão instaladas
    e exibe as suas versões.
    """
    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    packages: Dict[str, str] = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
    }

    missing: List[str] = []
    installed: Dict[str, Tuple[str, str]] = {}

    # Checa a existência e a versão de cada pacote sem importá-los na memória
    for pkg, desc in packages.items():
        try:
            version = importlib.metadata.version(pkg)
            installed[pkg] = (version, desc)
            print(f"[OK] {pkg} ({version}) - {desc}")
        except importlib.metadata.PackageNotFoundError:
            missing.append(pkg)

    if missing:
        print("\nSYSTEM ERROR: Missing dependencies detected.")
        print("To load these programs into your environment, run:\n")
        print("Using pip:")
        print("$> pip install -r requirements.txt")
        print("$> python3 loading.py\n")
        print("Using Poetry:")
        print("$> poetry install")
        print("$> poetry run python loading.py")
        return False
        
    return True


def run_analysis() -> None:
    """
    Roda a análise de dados e gera a visualização.
    Os imports são feitos localmente (dentro da função) para garantir
    que o Python não lance um ImportError antes da nossa checagem manual.
    """
    # O '# type: ignore' é o truque de mecânica mencionado no enunciado 
    # para que o 'mypy' ignore erros caso os pacotes não estejam instalados.
    import pandas as pd  # type: ignore
    import numpy as np  # type: ignore
    import matplotlib.pyplot as plt  # type: ignore

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")

    # Gerando dados simulados da Matrix USANDO NUMPY (não listas hardcoded)
    np.random.seed(42)
    # Simula 1000 sinais com flutuação aleatória
    matrix_signal = np.random.normal(0, 1, 1000)
    time_steps = np.arange(1000)

    # Criação do DataFrame usando Pandas
    df = pd.DataFrame({"Time": time_steps, "Signal": matrix_signal})

    print("Generating visualization...")
    
    # Criando o gráfico da anomalia com Matplotlib
    plt.figure(figsize=(10, 5))
    # Usando verde clássico de terminal para manter a estética do projeto
    plt.plot(df["Time"], df["Signal"], color="#00FF41", linewidth=0.8) 
    
    plt.title("Matrix Signal Analysis")
    plt.xlabel("Time Step")
    plt.ylabel("Signal Amplitude")
    
    # Estilizando fundo escuro Matrix
    ax = plt.gca()
    ax.set_facecolor('black')
    plt.gcf().patch.set_facecolor('black')
    ax.tick_params(colors='#00FF41')
    ax.xaxis.label.set_color('#00FF41')
    ax.yaxis.label.set_color('#00FF41')
    plt.title("Matrix Signal Analysis", color='#00FF41')

    plt.tight_layout()
    plt.savefig("matrix_analysis.png")
    plt.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    """Main entry point."""
    if check_dependencies():
        run_analysis()
    else:
        # Encerra o script retornando erro de sistema se faltar dependência
        sys.exit(1)


if __name__ == "__main__":
    main()
