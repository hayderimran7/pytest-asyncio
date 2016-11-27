from pathlib import Path

from setuptools import setup, find_packages


setup(
    name="pytest-asyncio",
    use_scm_version={"write_to": "pytest_asyncio/_version.py"},
    setup_requires=["setuptools-scm"],
    packages=find_packages(),
    url="https://github.com/pytest-dev/pytest-asyncio",
    license="Apache 2.0",
    author="Tin Tvrtković",
    author_email="tinchester@gmail.com",
    description="Pytest support for asyncio.",
    long_description=Path(__file__).parent.joinpath("README.rst").read_text(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Testing",
        "Framework :: Pytest",
    ],
    python_requires=">= 3.5",
    install_requires=["pytest >= 3.0.6"],
    extras_require={
        ':python_version == "3.5"': "async_generator >= 1.3",
        "testing": ["coverage", "async_generator >= 1.3"],
    },
    entry_points={"pytest11": ["asyncio = pytest_asyncio.plugin"]},
)
