from distutils.core import setup


setup(
    name="stereoProcessing",
    version="0.1",
    packages=['stereoProcessing'],
    author="Mitchell Scott",
    author_email="miscott@uw.edu",
    description="Codebase to help with stereo image processing, including storing opencv calibration values",
    long_description=open('README.md').read(),
)
