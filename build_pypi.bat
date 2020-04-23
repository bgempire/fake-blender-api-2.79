ECHO OFF

REM Build package to dist directory
python setup.py sdist

REM Upload to PyPI
twine upload dist/*

PAUSE