# [lib](http://lib.pyfunc.com)

all libs for cameramonit, ocr, fin-officer, cfo, and other projects


## Install

```bash
git clone https://github.com/pyfunc/lib.git pyfunc
```


## TODO

+ [ ] create Docker for test purpose, based on pyDock




## Contributing

```bash
python3 -m venv pytest-env
source pytest-env/bin/activate
```

```bash
pip install --upgrade pip
pip install pytest
```

run the test, execute the pytest command:
```bash
pytest
```



## Tips

simple method to generate a requirements.txt file is to pipe them,
```bash
pip freeze > requirements.txt
```

## if push not possible

```
[remote rejected] (refusing to allow a Personal Access Token to create or update workflow `.github/workflows/python-app.yml` without `workflow` scope)
```

Problem z odrzuceniem tokena dostępu osobistego (Personal Access Token, PAT) podczas próby aktualizacji pliku workflow, 
musisz zaktualizować uprawnienia swojego tokena. 

### Oto kroki, które powinieneś podjąć:

1. Przejdź do ustawień GitHub:
   - Kliknij na swój awatar w prawym górnym rogu GitHub
   - Wybierz "Settings"

2. Przejdź do ustawień deweloperskich:
   - W lewym menu wybierz "Developer settings"

3. Zarządzaj tokenami dostępu:
   - Wybierz "Personal access tokens"
   - Następnie "Tokens (classic)"

4. Utwórz nowy token lub zaktualizuj istniejący:
   - Jeśli tworzysz nowy, kliknij "Generate new token"
   - Jeśli aktualizujesz istniejący, znajdź odpowiedni token i kliknij "Edit"

5. Dodaj uprawnienie "workflow":
   - Przewiń do sekcji "Select scopes"
   - Zaznacz pole obok "workflow"

6. Zapisz zmiany:
   - Przewiń na dół i kliknij "Generate token" (dla nowego) lub "Update token" (dla istniejącego)

7. Skopiuj nowy token:
   - Upewnij się, że skopiowałeś nowy token, ponieważ nie będziesz mógł go zobaczyć ponownie

8. Zaktualizuj token w swoim lokalnym repozytorium:
   - Jeśli używasz HTTPS, zaktualizuj swoje dane logowania
   - Jeśli używasz SSH, upewnij się, że Twój klucz SSH jest poprawnie skonfigurowany

9. Spróbuj ponownie wykonać push:
   - Użyj nowego tokena do autoryzacji

Pamiętaj, że tokeny dostępu osobistego są bardzo wrażliwe na bezpieczeństwo.
Traktuj je jak hasła i nigdy nie udostępniaj ich publicznie. Jeśli przypadkowo ujawnisz swój token, natychmiast go usuń i wygeneruj nowy.

Po wykonaniu tych kroków, powinieneś być w stanie zaktualizować plik workflow bez problemów. Jeśli nadal napotkasz problemy, upewnij się, że masz odpowiednie uprawnienia w repozytorium i że workflow nie są zablokowane przez ustawienia organizacji lub repozytorium.