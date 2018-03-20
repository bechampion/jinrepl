from __future__ import print_function
import os
import sys
import codecs
from shutil import rmtree
from setuptools import setup, Command


here = os.path.abspath(os.path.dirname(__file__))


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel upload")
    sys.exit()


class UploadCommand(Command):
    """Support setup.py upload."""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPi via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()


about = dict()
with codecs.open(os.path.join(here, 'jinrepl', 'version.py'), 'r', encoding='utf-8') as f:
    exec(f.read(), about)


setup(
    name='jinrepl',
    version=about['__version__'],
    description='Repl for jinja2',
    url='https://github.com/bechampion/jinrepl',
    author='Jeronimo Garcia',
    author_email='garciaj.uk@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],
    project_urls={
        'Source': '',
        'Tracker': ''
    },
    packages=['jinrepl'],
    install_requires=[
        'jinja2',
        'termcolor'
    ],
    entry_points={
        'console_scripts': [
            'jinrepl=jinrepl.__main__:main'
        ]
    },
    cmdclass={
        'upload': UploadCommand,
    }
)
