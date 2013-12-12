
from setuptools import setup, find_packages


entry_points = {'console_scripts': ['wanderbits = wanderbits:main']}

with open('readme.md', 'r') as fi:
    long_description = fi.read()

# Do it.
setup(name='WanderBits',
      description='Wandering Text-Based Adventure Game',
      long_description=long_description,

      version='0.1.0',

      url='https://github.com/Who8MyLunch/WanderBits',

      author='Pierre V. Villeneuve',
      author_email='pierre.villeneuve@gmail.com',

      packages=find_packages(),
      entry_points=entry_points,
      package_data={'': ['*.txt', '*.md', '*.yml']},

      license='MIT',
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Console',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: Microsoft',
                   'Operating System :: POSIX',
                   'Operating System :: MacOS',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Games/Entertainment'],

      zip_safe=False,
      )
