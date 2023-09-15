# Project Name

GDG ABA Website Backend Repository

## Overview

Welcome to the GDG Aba website backend project! This is an open-source Django project that aims to maintain and manage the server that stores data of the GDG Aba website. We appreciate your interest in contributing to this project, and we want to ensure that the contribution process is smooth and efficient for both new and experienced contributors.

## Project Set Up

- First clone the repo:  

```bash
git clone https://github.com/YourUsername/gdg-aba-website-backend.git

```
- Go into the directory: 

```bash
cd gdg-aba-website-backend
```
- Install pipenv: 

```bash
pip install pipenv
```
NOTE: Pipenv creates a virtual environment for you that can be activated with `pipenv shell`

- install packages from requirements.txt using pipenv: 

```bash
pipenv install -r requirements.txt 
```
- Generate DB migrations:

```bash
python manage.py makemigrations
```
- Make migrations: 

```bash
python manage.py migrate

```
- Spin up the local server: 

```bash
python manage.py runserver

```
- Visit the localhost url `http://127.0.0.1:8000/` on your web browser

## TIPS

- To acitvate your virtual environment use: `pipenv shell`
- To exit from the virtual environment use: `exit`
- To install packages use: `pipenv install package-name`
More about Pipenv [here](https://pipenv.pypa.io/en/latest/)

## Getting Started With Contributing

To contribute to this project, follow these steps:

1. **Fork the Repository:** Click the "Fork" button at the top right corner of this repository's page to create a copy of the project in your own GitHub account.

2. **Clone Your Fork:** Use `git clone` to create a local copy of your fork on your development machine.

 ```bash
    git clone https://github.com/YourUsername/gdg-aba-website-backend.git
 ```
    
3. **Create a Branch:** Create a new branch for your work. Use a descriptive branch name that reflects the nature of your contribution. Preferably, use your username as the branch.

 ```bash
    git checkout -b feature/your-new-feature
 ```
Note: Don't forget to install the required packages by doing `pip install -r requirements.txt`

4. **Make Changes:** Make your changes or additions to the project code. Be sure to follow the project's coding guidelines and best practices.

5. **Commit Your Changes:** Commit your changes with clear and concise commit messages.

 ```bash
    git commit -m "Add a new feature"
 ```
6. Update the Requirements file: Do this before pushing so the next contributor won't face any issue
```bash
       pip freeze >> requirements.txt
```     

7. **Push Your Changes:** Push your changes to your fork on GitHub.

 ```bash
    git push origin feature/your-new-feature
 ```

8. **Submit a Pull Request:** Go to the original repository on GitHub and click the "New Pull Request" button. Provide a clear and detailed description of your changes in the pull request.

## Code Guidelines

Please adhere to the following guidelines when contributing to this project:

- Use [Black](https://pypi.org/project/black/) for formatting.
- Write clear and concise code with comments where necessary.
- Test your code thoroughly.
- Keep your pull requests focused on a single issue or feature.
- Here is [DRF documentation](https://www.django-rest-framework.org/) to assist you. 

## Reporting Issues

If you encounter bugs, have suggestions, or want to discuss new features, please open an issue on the GitHub issue tracker. Provide detailed information about the problem or enhancement you're proposing.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

We appreciate your interest and contributions to this project. Special thanks to all our contributors for helping make this project better. We look forward to your valuable input!
