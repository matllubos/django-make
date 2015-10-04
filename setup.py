from setuptools import setup, find_packages

from make.version import get_version

setup(
    name='django-make',
    version=get_version(),
    description="Django make, helper for django development.",
    keywords='django, make',
    author='Lubos Matl',
    author_email='matllubos@gmail.com',
    url='https://github.com/matllubos/django-make',
    license='LGPL',
    package_dir={'make': 'make'},
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU LESSER GENERAL PUBLIC LICENSE (LGPL)',
        'Natural Language :: Czech',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
    scripts=['make/bin/dmake'],
    zip_safe=False
)
