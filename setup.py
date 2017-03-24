from setuptools import find_packages, setup


install_requires = [
    'django-bakery==0.8.14',
    'wagtail>=1.6',
]

docs_require = [
    'mkdocs',
]

test_require = [
    'factory-boy==2.8.1',
    'flake8==3.2.1',
    'isort==4.2.5',
    'pytest==3.0.5',
    'pytest-cov==2.4.0',
    'pytest-django==3.1.2',
    'wagtail==1.9',
]

setup(
    name='wagtail-bakery',
    version='0.1.1',
    description='A set of helpers for baking your Django Wagtail site out as flat files.',
    author='Rob Moorman',
    author_email='rob@moori.nl',
    install_requires=install_requires,
    extras_require={
        'docs': docs_require,
        'test': test_require,
    },
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    classifier=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
