import setuptools

l_description=''
try:
    with open("README.md", "r") as fh:
        l_description = fh.read()
except:
    pass

setuptools.setup(
    name='monte_carlo',
    version='0.1',
    packages=setuptools.find_packages(exclude=['test']),
    # url='https://github.com/Shvarpa/BibFast',
    license='',
    author='Shvarpa',
    author_email='Shvarpa@gmail.com',
    description='monte carlo integration',
    long_description = l_description,
    install_requires=['Equation'],
	scripts=['monte_carlo.py']
)
