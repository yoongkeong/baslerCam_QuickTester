import setuptools

setuptools.setup(name='basler_CQT_lite',
    version='1.0',
    description='A Basler Camera Quick Tester lite version with limited functions based on pypylon',
    url='https://github.com/yoongkeong/basler_CQT_lite',
    author='Yoong Keong Lim',
    author_email='yoongkeong.lim@baslerweb.com',
    license='MIT',
    packages=setuptools.find_packages(),
    install_requires=['pypylon', 'python'],
    test_suite='tests',
    )
