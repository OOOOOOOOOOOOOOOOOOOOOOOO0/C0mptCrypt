from setuptools import setup, find_packages


setup(
    name='C0mptCrypt',
    version='0.1',
    license='MIT',
    author="execution",
    author_email='wank@example.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/execution/C0mptCrypt',
    keywords='example project',
    install_requires=[
          'pycryptodome',
          'hashlib'
      ],

)
