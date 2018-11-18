from distutils.core import setup

setup(
    name='requests-proxy-negotiate',
    version='1.0',
    description='Negotiate proxy authentication for the requests HTTP client library',
    author='AGZ',
    author_email='agzarifis@gmail.com',
    url='https://github.com/agzarifis/requests-proxy-negotiate',
    license='BSD',
    packages=['requests_proxy_negotiate'],
    long_description=open('README.md').read(),
    classifiers=['License :: OSI Approved :: BSD License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Internet :: WWW/HTTP :: Dynamic Content'],
    install_requires=['requests', 'gssapi', 'www-authenticate'],
)
