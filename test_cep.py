# test_cep.py

import pytest
from cep import validar_cep

@pytest.mark.parametrize("cep, cidade, expected", [
    ("18050-100", "Sorocaba", True),
    ("18195-000", "Capela do Alto", True),
    ("18130-020", "Sao Roque", True),
    ("19000-000", "Votorantim", False),
    ("18125-500", "Aluminio", True),
    ("18560-500", "Ipero", True),
    ("13300-500", "Itu", True),
    ("18120-500", "Mairinque", True),
    ("13315-500", "Cabreuva", True),
    ("13320-500", "Salto", True),
    ("18160-500", "Salto de Pirapora", True),
    ("18225-500", "Sarapui", True),
    ("18110-500", "Votorantim", True),
    ("18540-500", "Porto Feliz", True),
])
def test_validar_cep(cep, cidade, expected):
    assert validar_cep(cep, cidade) == expected