from setuptools import setup

setup(
		name='bugh',
		version='1.0',
		description='Create read-only backups of your Github repositories.',
		author='Will Haldean Brown',
		author_email='will.h.brown@gmail.com',
		url='https://github.com/haldean/bugh',
		scripts=['bugh'],
		install_requires=['sh', 'requests'],
		)
