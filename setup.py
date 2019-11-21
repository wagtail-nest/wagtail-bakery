from setuptools import find_packages, setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

install_requires = [
    'django-bakery~=0.12.7',
    'wagtail>=2.6',
]

test_requires = [
    'factory-boy',
    'flake8',
    'isort',
    'pytest',
    'pytest-cov',
    'pytest-django',
]

setup(
    name='wagtail-bakery',
    version='0.4.0',
    description='A set of helpers for baking your Django Wagtail site out as flat files.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Rob Moorman and Wagtail Core Team',
    author_email='hello@wagtail.io',
    install_requires=install_requires,
    tests_require=test_requires,
    extras_require={'test': test_requires},
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
    license='MIT',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Wagtail',
        'Framework :: Wagtail :: 2',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
