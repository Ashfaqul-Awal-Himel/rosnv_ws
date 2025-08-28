from setuptools import find_packages, setup

package_name = 'tway_follr'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='himel',
    maintainer_email='63048839+Ashfaqul-Awal-Himel@users.noreply.github.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ["tway_follr_node = tway_follr.twayfoll:main",
        ],
    },
)
