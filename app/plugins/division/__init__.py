from app.commands import Command

class DivisionCommand(Command):
    def execute(self, args):
        if args:
            x = float(args[0])
            y = float(args[1])
            try:
                return x/y
            except:
                print ("error! user is trying to do division by zero.")
        else:
            print ("there nothing to Divide here.")
