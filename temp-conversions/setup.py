from setuptools import setup
setup(
  name = 'temp_conv',        
  packages = ['temp_conv'],  
  version = '1.1',      
  description = 'Convert celcius, fahrenheit, kelvin',   
  author = 'JAI',                  
  author_email = 'mail2jai1123@gmail.com',     
  url = '',   
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