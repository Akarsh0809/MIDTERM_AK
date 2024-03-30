from app.commands import Command

class DivisionCommand(Command):
    def execute(self, args):
        if args:
            a = float(args[0])
            b = float(args[1])
            try:
                return a/b
            except:
                print ("error! user is trying to do division by zero.")
        else:
            print ("there nothing to Divide here.")
