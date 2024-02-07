from setuptools import setup

setup(
    name='latex2readme',
    version='0.0.1',
    py_modules=["latex2readme"],
    description="Convert LaTeX documents to README.md files",
    url="https://github.com/leon-h-a/tex2readme",
    license="MIT",
    install_requires=[
        "natsort==8.4.0",
        "pdf2image==1.16.3",
        "pillow==10.2.0",
        "pdflatex"
    ],
    entry_points={
        'console_scripts': [
            'ttr = latex2readme:run',
        ]
    }
)
