# **Midterm Project.**

**1. Design Patterns Used:**

*a. Command Pattern:* Command Pattern: Utilized in the Command and CommandHandler classes to decouple command execution from command objects. This promotes extensibility and maintainability by encapsulating requests as objects, enabling parameterization of clients with different requests and queuing of requests. 

link: "https://github.com/Akarsh0809/MIDTERM_AK/blob/main/app/commands/__init__.py"
'''

*b. Factory Pattern:* Implemented in the AppFactory class to dynamically create command objects based on plugin modules. This pattern encapsulates the object creation logic, allowing for flexibility and scalability in adding new commands without modifying existing code.

*Code snipped:*
```python
import pkgutil
import importlib
class AppFactory:
    @staticmethod
    def create_command_objects():
        commands = {}
        plugins_packages = [
            'app.plugins.addition',
            'app.plugins.subtraction',
            'app.plugins.multiplication',
            'app.plugins.division'
        ]
        for plugins_package in plugins_packages:
            for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
                if is_pkg:  
                    plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                    for item_name in dir(plugin_module):
                        item = getattr(plugin_module, item_name)
                        try:
                            if issubclass(item, Command):  
                                commands[plugin_name] = item
                        except TypeError:
                            continue
        return commands ```
```

*c) Facade Pattern:* Applied in the AppFacade class to provide a simplified interface for complex subsystems (data manipulation). This pattern hides the complexities of the subsystem and provides a single entry point for interacting with it. You can find the implementation within the AppFacade class here.

*Code snipped:*

```python
class AppFacade:
    @staticmethod
    def perform_data_manipulation(data):
       #Perform intricate data manipulations using Pandas here.
```     #This may include tasks such as filtering, transforming, aggregating, and more.

    
**2. Environmental usage:** 
The load_dotenv function from the dotenv library, these variables are seamlessly integrated. Within the App class, the getEnvironmentVariable method facilitates the retrieval of the ENVIRONMENT variable. This systematic approach empowers effortless configuration adjustments, facilitating the adaptation of application behavior to varying environments.

*Example snippet:*
```class MyClass:
    def __init__(self, settings):
        self.settings = settings

    def getEnvironmentVariable(self, envvar: str = 'ENVIRONMENT'):
        return self.settings.get(envvar)
```

**3. Logging:**
The logging module, log messages are systematically written to a designated file named "app.log" with a predefined format. To maintain organizational clarity and segregate logs effectively, loggers are instantiated using getLogger(__name__).
You can find the logging configuration and usage in the App class here, as well as in other modules where loggers are utilized.

*Example snippet:*
```python
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
Try/Except and Exceptions:

Exceptions are used for error handling in various parts of the code.  For instance, within the FileNotFoundError block in the FileHandling class, file-related errors are handled. When attempting to access a file that doesn't exist, an appropriate error message is displayed to the user.
```try:
    with open(filename, 'r') as file:
        # Perform file operations
except FileNotFoundError:
    print("File not found error: The specified file does not exist.")
```

This situation follows the "Look Before You Leap" (LBYL) approach, where potential errors are anticipated and fixed beforehand. On the other hand, the code utilizes the "Easier to Ask for Forgiveness than Permission" (EAFP) method in certain areas, focusing on task completion and managing errors as they occur.

**4. Procedure:**
a. Prepare the GitHub repository before connecting it to your WSL-2 IDE.
    
```php
git remote add origin <paste your github repository ssh link>
git add .
git commit -m "add your commit statement"
git push orign master 
ssh-keygen -t rsa -b 2048  (this command will create a ssh key)
vi ~/.ssh/id_rsa.pub (This will open the file containing th essh key. Paste this key in the github profile ssh key section)
```
 
b. Configure the environment for Python.

```python
sudo apt update -y
sudo apt install python3-pip
pip3 --version
(the above commands will update the wsl-2 and installs the python-3 packages)
pip3 install virtualenv (This command will install virtual environment)
virtualenv venv (This command will create a virtual environment venu)
source ./venv/bin/activate (This command will activate the virtual environment.)
pip3 install -r requirments.txt (This command will install all the required packages)
pytest (Runs the tests)
pytest --pylint  (Runs tests with pylint static code analysis)
pytest --pylint --cov (Runs tests, pylint, and coverage to check if you have all your code tested.)
python3 main.py 
```
c.The given command starts the application and guides you to the menu for interaction. From there, you can select your desired option. After completing the chosen operation, you'll be prompted to re-enter the menu for further interaction. This cycle repeats until you opt to exit the menu.


**5.a video describing the calculator app's functionality**
https://drive.google.com/file/d/11jf8NeGATLZujoOkuJvLC4yfB8EYGRT1/view?usp=sharing



Click on the video link to see the video.



