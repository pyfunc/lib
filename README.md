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