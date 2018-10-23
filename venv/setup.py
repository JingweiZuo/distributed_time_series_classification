from setuptools import setup, find_packages  
setup(   
	name = "eggtest",   
	version = "0.1",   
	#packages = find_packages(),
	description = "egg test demo",   
	long_description = "egg test demo",   
	author = "jingwei zuo",
	author_email = "jingwei.zuo.uvsq@gmail.com",
	license = "GPL",   
	keywords = ("test", "egg"),   
	platforms = "Independant",
	requires=['numpy'],

    package_dir={'': 'src'},
    packages=['your', 'you.module'],

    use_2to3=True,

)   
