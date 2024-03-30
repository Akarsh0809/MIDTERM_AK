# **Midterm Project.**

**1. Design Patterns Used:**

*a. Command Pattern:* Command Pattern: Utilized in the Command and CommandHandler classes to decouple command execution from command objects. This promotes extensibility and maintainability by encapsulating requests as objects, enabling parameterization of clients with different requests and queuing of requests. "https://github.com/Akarsh0809/MIDTERM_AK/blob/main/app/commands/__init__.py"
'''
*b. Factory Pattern:* Implemented in the AppFactory class to dynamically create command objects based on plugin modules. This pattern encapsulates the object creation logic, allowing for flexibility and scalability in adding new commands without modifying existing code. You can find the implementation here.
Code snipped:
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
        return commands

*c. Facade Pattern:* Applied in the AppFacade class to provide a simplified interface (perform_data_manipulation()) to complex operations (Pandas data manipulation).
Code snipped:
class AppFacade:
    @staticmethod
    def perform_data_manipulation(data):
        # Perform complex Pandas data manipulations here
        # This could involve operations like filtering, transformation, aggregation, etc.
        pass
