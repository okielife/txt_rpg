import pathlib
from setuptools import setup

from txt_rpg import VERSION

readme_file = pathlib.Path(__file__).parent.resolve() / 'README.md'
readme_contents = readme_file.read_text()

setup(
    name="txt_rpg",
    version=VERSION,
    packages=['txt_rpg'],
    description="Text based RPG",
    package_data={"txt_rpg": []},  # patterns relative to /txt_rpg/
    include_package_data=True,
    long_description=readme_contents,
    long_description_content_type='text/markdown',
    author='Them Lee Boys',
    url='https://github.com/okielife/txt_rpg',
    license='Unlicensed',
    install_requires=['pygame'],
    entry_points={
        # 'gui_scripts': ['txt_rpg=txt_rpg.runner:main_gui'],
        'console_scripts': ['txt_rpg_cli=txt_rpg.runner:main_cli',]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Utilities',
    ],
    platforms=[
        'Linux (Tested on Ubuntu)', 'MacOSX', 'Windows'
    ],
    keywords=[
        'energyplus_launch', 'ep_launch',
        'EnergyPlus', 'eplus', 'Energy+',
        'Building Simulation', 'Whole Building Energy Simulation',
        'Heat Transfer', 'HVAC', 'Modeling',
    ]
)
