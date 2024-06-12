from setuptools import setup, find_packages

setup(
    name='Image-recognition',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'opencv-python-headless>=4.5.3.56',
        'numpy>=1.21.1',
        'Pillow>=8.3.1',
    ],
    author='João Lucas S. A. Maia',
    description='A computer desktop app for object recognition and classification using Python.',
    entry_points={
        'console_scripts': [
            'image-detection=image_recognition.app:create_initial_window',
        ],
    },
)