from setuptools import setup

setup(
  name = 'syncle',
  description = 'Single-file synchronization tool',
  author = 'Roman Dolgushin',
  license = 'MIT',
  version = '0.1',
  packages = ['syncle'],
  entry_points = {
    'console_scripts': ['syncle = syncle.syncle:main']
  }
)
