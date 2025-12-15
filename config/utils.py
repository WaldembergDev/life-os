from decouple import config

def obter_ambiente():
    ambiente = config('AMBIENTE')
    if ambiente:
        return ambiente
    return 'dev'