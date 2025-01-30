from distutils.core import setup
setup(
    name = 'jadelogs',         # How you named your package folder (MyLib)
    packages=['jadelogs'],
    package_data={
        'jadelogs': ['*','*/*','*/*/*']
    },   # Chose the same as "name"
    version = '0.15',      # Start with a small number and increase it with every change you make
    license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    description = 'Package to log and track progress of machine learning programs run on the Jade supercomputer',   # Give a short description about your library
    author = 'Ved Mathai',                   # Type in your name
    author_email = 'vedu29@gmail.com',      # Type in your E-Mail
    url = 'https://github.com/vedmathai/jade-logs',   # Provide either the link to your github or to your website
    keywords = ['jade', 'supercomputer', 'logs'],   # Keywords that define your package best
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)