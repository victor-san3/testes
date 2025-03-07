# cep.py

def validar_cep(cep, cidade):
    # Dicionário com as faixas de CEP e suas respectivas cidades
    faixas_cep = {
        "Aluminio": ("18125-000", "18129-999"),
        "Ipero": ("18560-000", "18569-999"),
        "Aracariguama": ("18147-000", "18149-999"),
        "Aracoiaba da Serra": ("18190-000", "18194-999"),
        "Itu": ("13300-000", "13314-999"),
        "Mairinque": ("18120-000", "18124-999"),
        "Cabreuva": ("13315-000", "13319-999"),
        "Capela do Alto": ("18195-000", "18199-999"),
        "Salto": ("13320-000", "13329-999"),
        "Salto de Pirapora": ("18160-000", "18169-999"),
        "Sao Roque": ("18130-000", "18146-999"),
        "Sarapui": ("18225-000", "18229-999"),
        "Sorocaba": ("18000-000", "18109-999"),
        "Votorantim": ("18110-000", "18119-999"),
        "Porto Feliz": ("18540-000", "18549-999"),
    }

    if cidade not in faixas_cep:
        return False

    cep_min, cep_max = faixas_cep[cidade]
    return cep_min <= cep <= cep_max