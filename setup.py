import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="telegram_button",
    version="0.0.1",
    author="Yunzhi Gao",
    author_email="gaoyunzhi@gmail.com",
    description="Append buttons to telegram message.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gaoyunzhi/telegram_button",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'telegram_util>=0.0.29',
    ],
    python_requires='>=3.0',
)