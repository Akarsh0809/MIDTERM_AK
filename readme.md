# **Midterm Project.**

**1. Design Patterns Used:**

*a. Command Pattern:* Command Pattern: Utilized in the Command and CommandHandler classes to decouple command execution from command objects. This promotes extensibility and maintainability by encapsulating requests as objects, enabling parameterization of clients with different requests and queuing of requests. "https://github.com/Akarsh0809/MIDTERM_AK/blob/main/app/commands/__init__.py"
'''

*b. Factory Pattern:* Implemented in the AppFactory class to dynamically create command objects based on plugin modules. This pattern encapsulates the object creation logic, allowing for flexibility and scalability in adding new commands without modifying existing code.
import pkgutil
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
        # Perform complex Pandas data manipulations here
        # This could involve operations like filtering, transformation, aggregation, etc.
        pass
    ```

**2. Environment Variables Usage:**
Environment variables are used to load application settings dynamically and manage the environment. They are loaded using the load_dotenv function from the dotenv library. The environment variable ENVIRONMENT is accessed using the getEnvironmentVariable method of the App class. This approach allows for easy configuration and adaptation of the application behavior based on the environment.

You can find the code illustrating the usage of environment variables here in the App class.

*Example snippet:*
```python
def getEnvironmentVariable(self, envvar: str = 'ENVIRONMENT'):
   return self.settings[envvar]
```

**3. Logging:**
Logging is extensively used throughout the application to provide insights into its behavior and to track various events. The logging module is configured to write log messages to a file (app.log) with a specified format. Loggers are created using getLogger(__name__) to ensure proper organization and separation of logs.

You can find the logging configuration and usage in the App class here, as well as in other modules where loggers are utilized.

*Example snippet:*
```python
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
Try/Except and Exceptions:
Exceptions are used for error handling in various parts of the code. For example, in the DivisionCommand class, a try/except block catches a ZeroDivisionError if the divisor is zero, and an error message is printed.

*Example snippet:*
```python
python
Copy code
try:
    return a / b
except ZeroDivisionError:
    print("Division by zero error")
```

This is an example of the "Look Before You Leap" (LBYL) methodology, in which any mistakes are recognized and addressed in advance. Conversely, the "Easier to Ask for Forgiveness than Permission" (EAFP) technique is employed in different sections of the code, prioritizing tasks and handling exceptions when they arise.


**4. Working:**
a. Before linking the github repository to your WSL-2 IDE, set it up.


    
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

c. The aforementioned command launches the application and prompts you to enter the menu in order to see it. You can then choose the option you wish to interact with, and once the command operation is complete, you will be prompted to enter the menu once more to select the option to interact with. This continues until you choose to quit the menu.

**5.a video describing the calculator app's functionality**
https://drive.google.com/file/d/11jf8NeGATLZujoOkuJvLC4yfB8EYGRT1/view?usp=sharing



Click on the video link to see the video.



