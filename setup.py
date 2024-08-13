from setuptools import setup, find_packages

setup(
    name="DollarPeru",
    version="0.1.1",
    description="Scrapea el precio del dolar en diferentes casas de cambio y bancos",
    author="Tjhon",
    author_email="fr.jhonk@gmail.com",
    packages=find_packages(),
    install_requires=["selenium", "pandas", "numpy", "python-dotenv", "requests"],
)
