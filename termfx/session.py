from ast import arg
import re
from .errors import *

class New():

    def __init__(self, split = None):
        self.variables = {}
        self.functions = {}

        self.split = { "start": "<<", "end": ">>" } if split is None else split

    def register_variable(self, name: str, value: str, overwrite=False):
        if name in self.variables.keys() and not overwrite:
            raise RegisteredVariable(f"A variable with the name {name} already exists.")

        self.variables[name] = value

    def register_function(self, name: str, func: any, overwrite=False):
        if name in self.functions.keys() and not overwrite:
            raise RegisteredFunction(f"A function with the name {name} already exists.")

        self.functions[name] = func
    
    def stripper(self, string):
        for x in ['"', "'", '''"""''', """'''"""]:
            string=string.replace(x, "")
        return string
    
    def execute_file(self, file: str):
        with open(file) as f:
            return self.execute(f.read())

    def execute(self, string: str):
        output = string
        for line in re.findall(r"(<<(.*?)>>)", string):
            line = line[0]
            value = line.split(self.split["start"])[1].split(self.split["end"])[0]

            if "(" in line and ")" in line:

                arguments = value.split("(")[1].split(")")[0]
                arglist = arguments.split(",")  if len(arguments.split(",")) > 1 else [arguments]
                arguments = [int(x) if x.isdigit() else float(x) if re.match(r"^-?\d+(?:\.\d+)$", x) else self.stripper(x) for x in arglist]
                func = self.functions.get(value.split("(")[0])

                if func is None:
                    raise RegisteredFunction(f"{value.split('(')[0]} is not a registered function.")
                elif len(arglist) <= 1 and arglist[0] is "":
                    func_output = func()
                    output = output.replace(line, "" if func_output is None else str(func_output))
                    continue
                else:
                    func_output = func(*arguments)
                    output = output.replace(line, "" if func_output is None else str(func_output))

            elif value.startswith("$"):
                name = self.variables.get(value.replace("$",""))

                if name is None:
                    raise RegisteredVariable(f"{value.replace('$','')} is not a registered variable.")

                output = output.replace(line, str(name))
        
        return output
