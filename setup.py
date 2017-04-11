from setuptools import find_packages, setup


install_requires = [
    'django-bakery==0.9.2',
    'six>=1.10.0',
    'wagtail>=1.6',
]

test_requires = [
    'factory-boy==2.8.1',
    'flake8==3.2.1',
    'isort==4.2.5',
    'pytest==3.0.5',
    'pytest-cov==2.4.0',
    'pytest-django==3.1.2',
]

setup(
    name='wagtail-bakery',
    version='0.1.0',
    description='A set of helpers for baking your Django Wagtail site out as flat files.',
    author='Rob Moorman',
    author_email='rob@moori.nl',
    install_requires=install_requires,
    tests_require=test_requires,
    extras_require={'test': test_requires},
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
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
