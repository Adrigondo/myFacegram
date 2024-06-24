# myFacegram
This app were build based in the Course of Django from Platzi imparted by Pablo Trinidad.
## TODOS
- Configure static route
- Configure cache
- Implement rotating keys
- Implement loging
## Steps for use Poetry
*(This installation is for windows)*
This steps are better explained in the [official documentation of Poetry](https://python-poetry.org/docs/).
### Install pipx
```sh
py -m pip install --user pipx
```
If this warning appear:
```sh
WARNING: The script pipx.exe is installed in `<USER folder>/AppData/Roaming/Python/Python3x/Scripts` which is not on PATH
```
Go to the mentioned folder. Enter the following line (even if you did not get the warning):
```sh
./pipx.exe ensurepath
```
### Install poetry
```sh
pipx install poetry
```
#### Upgrade poetry
```sh
pipx upgrade poetry
```
#### Uninstall poetry
```sh
pipx uninstall poetry
```

### In initialized proyects
```sh
poetry init
```

## Docker
```sh
docker run -dti -p8000:8000 --name my-facegram --env-file ./environment/.env.production poetry-django
```