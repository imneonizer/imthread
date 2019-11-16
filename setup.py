from distutils.core import setup
setup(
  name = 'imthread',         # How you named your package folder (MyLib)
  packages = ['imthread'],   # Chose the same as "name"
  version = '1.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This short little python module can help you with running your iterable functions on multithreading without any hassle of creating threads by yourself.',   # Give a short description about your library
  author = 'Nitin Rai',                   # Type in your name
  author_email = 'mneonizer@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/imneonizer/imthread',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/imneonizer/imthread/archive/v1.1.tar.gz',    # I explain this later on
  keywords = ['Multi Threading', 'Synchronous Threading', 'Asyncio'],   # Keywords that define your package best
  classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
