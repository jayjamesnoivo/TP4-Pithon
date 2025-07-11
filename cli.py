from evaluator import eval_block, PithonRuntimeError

def run(code):
    env = {}
    try:
        eval_block(code, env)
    except PithonRuntimeError as e:
        print(e)

if __name__ == "__main__":
    programme = [
        ["class", "Personne", {
            "__init__": [
                ["setattr", "self", "nom", ["get", "args", 0]]
            ],
            "__str__": [
                ["+", "Nom: ", ["get", "self", "nom"]]
            ]
        }],
        ["set", "p", ["new", "Personne", "Jeremy"]],
        ["print", "p"]
    ]
    run(programme)