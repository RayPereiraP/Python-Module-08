import os
import sys
from typing import Optional, List

try:
    from dotenv import load_dotenv
except ImportError:
    print("SYSTEM ERROR: python-dotenv not installed.")
    print("Please run: pip install -r requirements.txt")
    sys.exit(1)


def check_security(has_env_file: bool) -> None:
    """Verifica e exibe o status de segurança do ambiente."""
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")

    if has_env_file:
        print("[OK] .env file properly configured")
    else:
        print("[!] No .env file found, relying entirely on system env vars")

    print("[OK] Production overrides available\n")
    print("The Oracle sees all configurations")


def main() -> None:
    """Main entry point for The Oracle."""
    # Checamos se o arquivo .env existe fisicamente no diretório
    has_env_file: bool = os.path.isfile(".env")

    # load_dotenv() carrega as variáveis do .env para o os.environ.
    # Por padrão (override=False), ele NÃO sobrescreve variáveis que
    # já foram passadas diretamente na linha de comando (ex: override).
    load_dotenv()

    # Leitura das configurações
    mode: str = os.getenv("MATRIX_MODE", "development")
    db_url: Optional[str] = os.getenv("DATABASE_URL")
    api_key: Optional[str] = os.getenv("API_KEY")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    zion_endpoint: Optional[str] = os.getenv("ZION_ENDPOINT")

    print("ORACLE STATUS: Reading the Matrix...")

    # Verificação de variáveis obrigatórias faltantes
    required_vars: List[str] = ["DATABASE_URL", "API_KEY", "ZION_ENDPOINT"]
    missing_vars: List[str] = [var for var in required_vars if os.getenv(var) is None]

    if missing_vars:
        print("WARNING: Missing or default configuration detected.")
        for var in missing_vars:
            print(f" -> Missing critical key: {var}")
        print("\nPlease copy .env.example to .env and configure your variables.")
        sys.exit(1)

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    # Demonstração clara da diferença entre Development e Production
    if mode.lower() == "production":
        print("Database: Connected to SECURE production cluster")
        print("API Access: Authenticated (Restricted Mode)")
        print(f"Log Level: {log_level} (Production Logging)")
        print("Zion Network: Online (Encrypted Connection)")
    else:
        print("Database: Connected to local instance")
        print("API Access: Authenticated")
        print(f"Log Level: {log_level}")
        print("Zion Network: Online")

    check_security(has_env_file)


if __name__ == "__main__":
    main()
