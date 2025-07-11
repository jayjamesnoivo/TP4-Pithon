class PithonRuntimeError(Exception):
    def __init__(self, message):
        super().__init__(f"[ERREUR D'EXÉCUTION] {message}")

class Classe:
    def __init__(self, nom, méthodes):
        self.nom = nom
        self.méthodes = méthodes

    def instancier(self, args=[], env=None):
        instance = Instance(self)
        if "__init__" in self.méthodes:
            if env is None:
                env = {}
            nouvel_env = env.copy()
            nouvel_env["self"] = instance
            nouvel_env["args"] = args
            eval_block(self.méthodes["__init__"], nouvel_env)
        return instance

class Instance:
    def __init__(self, classe):
        self.classe = classe
        self.attributs = {}

    def appeler_méthode(self, nom_méthode, args, env):
        if nom_méthode not in self.classe.méthodes:
            raise PithonRuntimeError(f"Méthode '{nom_méthode}' non définie")
        corps = self.classe.méthodes[nom_méthode]
        nouvel_env = env.copy()
        nouvel_env["self"] = self
        nouvel_env["args"] = args
        return eval_block(corps, nouvel_env)

    def __str__(self):
        try:
            if "__str__" in self.classe.méthodes:
                val = self.appeler_méthode("__str__", [], {})
                return str(val)
            else:
                return f"[Instance de {self.classe.nom}]"
        except:
            return f"[Instance de {self.classe.nom}]"

def eval_expr(expr, env):
    try:
        if isinstance(expr, int) or isinstance(expr, float) or isinstance(expr, str):
            if expr in env:
                return env[expr]
            else:
                return expr
        elif isinstance(expr, list):
            op = expr[0]
            args = expr[1:]

            if op == "+":
                return eval_expr(args[0], env) + eval_expr(args[1], env)
            elif op == "print":
                val = eval_expr(args[0], env)
                print(str(val))
                return val
            elif op == "set":
                env[args[0]] = eval_expr(args[1], env)
                return env[args[0]]
            elif op == "get":
                source = eval_expr(args[0], env)
                key = args[1]
                if isinstance(source, Instance):
                    if key in source.attributs:
                        return source.attributs[key]
                    else:
                        raise PithonRuntimeError(f"Attribut '{key}' non défini")
                elif isinstance(source, list) and isinstance(key, int) and key < len(source):
                    return source[key]
                elif isinstance(source, dict) and key in source:
                    return source[key]
                else:
                    raise PithonRuntimeError(f"Impossible d'accéder à '{key}' dans {source}")
            elif op == "setattr":
                instance = eval_expr(args[0], env)
                attr = args[1]
                val = eval_expr(args[2], env)
                instance.attributs[attr] = val
                return val
            elif op == "call":
                instance = eval_expr(args[0], env)
                méthode = args[1]
                arguments = [eval_expr(arg, env) for arg in args[2:]]
                return instance.appeler_méthode(méthode, arguments, env)
            elif op == "class":
                nom = args[0]
                méthodes = args[1]
                env[nom] = Classe(nom, méthodes)
                return f"[Classe {nom} créée]"
            elif op == "new":
                nom = args[0]
                arguments = [eval_expr(arg, env) for arg in args[1:]]
                if nom not in env:
                    raise PithonRuntimeError(f"Classe '{nom}' inconnue")
                return env[nom].instancier(arguments, env)
            else:
                raise PithonRuntimeError(f"Opérateur inconnu : {op}")
        else:
            raise PithonRuntimeError("Expression invalide.")
    except Exception as e:
        raise PithonRuntimeError(str(e))

def eval_block(block, env):
    result = None
    for expr in block:
        result = eval_expr(expr, env)
    return result