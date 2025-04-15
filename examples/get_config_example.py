from pyfunc2.config.get_config import get_config

if __name__ == "__main__":
    # Przykład: pobierz konfigurację z pliku konfiguracyjnego
    config_path = "./example_config.json"  # Podmień na istniejący plik konfiguracyjny
    try:
        config = get_config(config_path)
        print(f"get_config: {config}")
    except Exception as e:
        print(f"Błąd podczas wczytywania konfiguracji: {e}")
