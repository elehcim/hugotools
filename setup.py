from setuptools import setup

setup(name='hugotools',
      version='0.1',
      description='Some tools to help my workflow with hugo',
      license="MIT",
      author='Michele Mastropietro',
      author_email='michele.mastropietro@gmail.com',
      install_requires=["pyyaml"],
      packages=['hugotools'],
      entry_points={
          'console_scripts': ['hugojot=hugotools:main']},
      )
