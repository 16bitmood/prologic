import setuptools

with open("README.org", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="prologic-16bitmood",
    version="0.0.1",
    author="16bitmood",
    author_email="16bitmood@gmail.com",
    description="Propositional Logic Evaluator",
    long_description=long_description,
    long_description_content_type="text/org",
    # url="https://github.com/16bitmood/prologic",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'prologic=prologic.repl:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
