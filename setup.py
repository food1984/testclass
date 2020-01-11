from setuptools import setup
import pkutils


requirements = list(pkutils.parse_requirements('requirements.txt'))
readme = pkutils.read('README.md')
module = pkutils.parse_module('testclass/__init__.py')
packages = [module.__title__]

setup(
      name=module.__title__,
      version=module.__version__,
      description=module.__description__,
      long_description=readme,
      url='http://github.com/erikdeirdre/testclass',
      author=module.__author__,
      author_email=module.__email,
      license=module.__license__,
      install_requires=requirements,
      packages=packages,
      setup_requires=['wheel', 'pkutils'],
      zip_safe=False
      )
