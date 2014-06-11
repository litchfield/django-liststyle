from distutils.core import setup
from distutils.command.install import INSTALL_SCHEMES
import os

root = os.path.dirname(os.path.abspath(__file__))
os.chdir(root)

VERSION = '0.1'

# Make data go to the right place.
# http://groups.google.com/group/comp.lang.python/browse_thread/thread/35ec7b2fed36eaec/2105ee4d9e8042cb
for scheme in INSTALL_SCHEMES.values():
    scheme['data'] = scheme['purelib']


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
    packages=['liststyle'],
    #data_files=[(template_dir, templates)],
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
