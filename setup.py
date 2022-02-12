import setuptools

setuptools.setup(
    name="mlx90614-prometheus",
    version="0.0.1",
    author="Timo Pomer",
    author_email="timopomer@gmail.com",
    description="Expose mlx90614 sensor data as a prometheus endpoint",
    url="https://github.com/timopomer/mlx90614-prometheus",
    project_urls={
        "Bug Tracker": "https://github.com/timopomer/mlx90614-prometheus/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=[
        'prometheus-client==0.13.1',
        'smbus2==0.4.1',
        'PyMLX90614==0.0.4'
    ],
    entry_points={
        'console_scripts': ['collect-mlx90614=collect_data:main'],
    }
)
