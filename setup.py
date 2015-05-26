import setuptools

setuptools.setup(
    name="zca",
    version="0.1.0",
    url="https://github.com/mwv/zca",

    author="Maarten Versteegh",
    author_email="maartenversteegh@gmail.com",

    description="ZCA whitening",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)
