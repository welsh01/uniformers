from setuptools import setup, find_packages

setup(
    name="uniformers",
    description="Universal Coded Character Set Transformers for Language Modelling",
    keywords=[
        "Deep Learning",
        "Language Models",
        "Transformers",
        "Character-Level",
        "Tokenization-Free",
        "Natural Language Processing",
        "Natural Language Generation",
        "Poetry Generation",
    ],
    url="https://github.com/potamides/uniformers",
    author="Jonas Belouadi",
    author_email="potamides@posteo.net",
    packages=find_packages(include=["uniformers*"]),
    install_requires=[
        "datasets~=2.3.2",
        "numpy~=1.22.4",
        "tokenizers~=0.12.1",
        "torch~=1.11.0",
        "zstandard~=0.17.0",
        "transformers==4.20.0",
    ],
    extras_require={
        "examples": [],
    },
    python_requires="~=3.10.4",
    zip_safe=False,
)
