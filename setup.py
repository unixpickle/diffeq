from setuptools import setup

setup(
    name='diffeq',
    version='0.0.1',
    description='Learning about differential equations',
    long_description='Learning about differential equations',
    url='https://github.com/unixpickle/diffeq',
    author='Alex Nichol',
    author_email='unixpickle@gmail.com',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='math differential equations',
    packages=['diffeq'],
    install_requires=['numpy', 'scipy'],
)
