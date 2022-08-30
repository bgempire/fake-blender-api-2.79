python3 -m build --outdir dist
python3 -m twine upload --repository pypi dist/*
