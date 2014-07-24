import os


try:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup
    has_setuptools = True
except ImportError:
    try:
        from setuptools import setup
        has_setuptools = True
    except:
        pass
    has_setuptools = False
    from distutils.core import setup


def find_packages(base):
    packages = []
    for pkg in ['ctk']:
        path = os.path.join(base, pkg)
        for (dirname, subdirs, files) in os.walk(path):
            if '__init__.py' in files:
                (lib, fragment) = dirname.split(os.sep, 1)
                packages.append(fragment.replace(os.sep, '.'))
    return packages

def run_setup():
    setup(
        name='ctk',
        version='0.1',
        description='Continuum Consultant Toolkit',
        author='Continuum Analytics, Inc',
        keywords='Continuum,toolkit',
        packages=find_packages('lib'),
        package_dir={'': 'lib'},
        data_files=[('conf', ['conf/ctk.conf'])],
        zip_safe=False, # http://stackoverflow.com/a/2798497
        scripts=['bin/ctk', 'bin/ctk.bat'],
#        entry_points={
#            'console_scripts': [
#                'evnadmin = evn.admin.cli:main',
#            ],
#        },
    )

if __name__ == '__main__':
    run_setup()

# vim:set ts=8 sw=4 sts=4 tw=78 et:
