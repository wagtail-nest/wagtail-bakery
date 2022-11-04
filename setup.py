from setuptools import find_packages, setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

install_requires = [
    'django-bakery~=0.13.1',
    'wagtail>=2.15',
]

test_requires = [
    'factory-boy<3',
    'flake8',
    'isort',
    'pytest',
    'pytest-cov',
    'pytest-django',
]

setup(
    name='wagtail-bakery',
    version='0.5.0',
    description='A set of helpers for baking your Django Wagtail site out as flat files.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Rob Moorman and Wagtail Core Team',
    author_email='hello@wagtail.io',
    url="https://github.com/wagtail/wagtail-bakery/",
    project_urls={
        "Source": "https://github.com/wagtail/wagtail-bakery/",
        "Issue tracker": "https://github.com/wagtail/wagtail-bakery/issues/",
        "Changelog": "https://github.com/wagtail/wagtail-bakery/blob/main/CHANGELOG.md",
    },
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
        'License :: OSI Approved :: MIT License',
        'Framework :: Django',
        'Framework :: Wagtail',
        'Framework :: Wagtail :: 2',
        'Framework :: Wagtail :: 4',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
