from setuptools import setup

package_name = 'joystick_pub'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bo',
    maintainer_email='bo@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
            'console_scripts': [
                    'joystick_driver = joystick_pub.joystick_driver:main',
                    'joystick_pub = joystick_pub.joystick_pub:main',
            ],
    },
)
