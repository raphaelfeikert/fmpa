from distutils.core import setup
setup(
  name = 'fmpa',         
  packages = ['fmpa'],   
  version = '0.5',      
  license='MIT',        
  description = 'wrapper for the financial modelling prep api',   
  author = "RAPHAEL FEIKERT"
  url = 'https://github.com/raphaelfeikert/fmpa',   
  download_url = 'https://github.com/raphaelfeikert/fmpa/archive/v_05.tar.gz',    
  install_requires=[            
          'requests',
          'numpy',
          'pandas'         
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
  ],
)