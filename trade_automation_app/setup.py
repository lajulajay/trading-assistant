from setuptools import setup, find_packages
import os

# Get the directory containing setup.py
setup_dir = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory
parent_dir = os.path.dirname(setup_dir)
# Path to README.md in parent directory
readme_path = os.path.join(parent_dir, "README.md")

setup(
    name="trade_automation",
    version="1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # Use a direct path to etrade_client
        f"etrade_client @ file://{os.path.join(parent_dir, 'etrade_client')}",
        "python-dotenv>=1.0.0",
    ],
    python_requires=">=3.6",
    author="Your Name",
    author_email="your.email@example.com",
    description="E*TRADE Trade Automation App",
    long_description=open(readme_path).read(),
    long_description_content_type="text/markdown",
    entry_points={
        "console_scripts": [
            "trade-automation=trade_automation.wrapper:main",
        ],
    },
) 