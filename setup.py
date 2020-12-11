from setuptools import find_packages, setup

REQUIRED = [
    "pytest==6.1.2",
    "pytest-mock==3.3.1",
    "jira==2.0.0",
    "mock==4.0.2",
]
PACKAGES = find_packages("src")

setup(
    name="Pytest Mocking Class Methods",
    version="0.0.1",
    install_requires=REQUIRED,
    python_required=">=3.8",
    test_suite="tests",
    packages=PACKAGES,
    package_dir={"": "src"},
)
