from .models import StatusEnum

def obter_string_status_enum(status: str):
    for choice in StatusEnum:
        if choice.value == status.upper():
            return choice
    return None