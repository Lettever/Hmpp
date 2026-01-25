import importlib.util
from functools import wraps

def KeepsSpace(func):
    func.keeps_space = True
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    
    return wrapper

def SelfCloses(func):
    func.is_self_closing = True
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

full_path = "./script.py"

def load_module_from_path(module_path):
    module_name = "script"
    spec = importlib.util.spec_from_file_location(module_name, module_path)

    if spec is None:
        raise ImportError(f"Could not load spec from {module_path}")
    
    module = importlib.util.module_from_spec(spec)
    module.SelfCloses = SelfCloses
    module.KeepsSpace = KeepsSpace
    
    spec.loader.exec_module(module)
    return module

script = load_module_from_path(full_path)

print(script.Author)
print(script.Header())
print(script.Header())
print(script.Hello("John", 20))
print(script.br())
print(script.pre("foo"))


