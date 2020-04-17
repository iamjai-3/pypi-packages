from setuptools import setup
setup(
  name = 'voice_timer',        
  packages = ['voice_timer'],  
  version = '2.1',      
  description = 'Speech recognition based Timer',   
  author = 'JAI',                  
  author_email = 'mail2jai1123@gmail.com',     
  url = 'https://github.com/iamjai-3/timer_package.git',   
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],  
  install_requires=[            
          'beautifulsoup4',         
          'speechrecognition'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',


  ],
)