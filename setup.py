import setuptools

setuptools.setup(
    name="pyx2py",
    version="0.1.0",
    url="",

    author="fx-kirin",
    author_email="ono.kirin@gmail.com",

    description="pyx to py converter",
    long_description=open('README.md').read(),

    packages=setuptools.find_packages(),
    scripts=["pyx2py"],

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
