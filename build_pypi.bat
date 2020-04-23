ECHO OFF

REM Build package to dist directory
python setup.py sdist

REM Upload to PyPI
REM twine upload dist/*

PAUSE