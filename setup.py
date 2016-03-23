from setuptools import setup

VERSION = '0.2b'


setup(
    name='django-liststyle',
    version=VERSION,
    description="Django admin changelist CSS styling",
    long_description="",
    author="Simon Litchfield",
    author_email="simon@s29.com.au",
    url="http://github.com/litchfield/django-liststyle",
    license="MIT License",
    platforms=["any"],
    packages=['liststyle', 'liststyle.templatetags'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    include_package_data=True,
)
