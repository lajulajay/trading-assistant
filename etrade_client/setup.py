from setuptools import setup, find_packages
import os

# Get the directory containing setup.py
setup_dir = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory
parent_dir = os.path.dirname(setup_dir)
# Path to README.md in parent directory
readme_path = os.path.join(parent_dir, "README.md")

setup(
    name="etrade_client",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "rauth==0.7.3",
        "requests==2.31.0",
        "python-dotenv==1.0.0",
    ],
    python_requires=">=3.6",
    author="Your Name",
    author_email="your.email@example.com",
    description="E*TRADE API client with shared authentication",
    long_description=open(readme_path).read(),
    long_description_content_type="text/markdown",
) 