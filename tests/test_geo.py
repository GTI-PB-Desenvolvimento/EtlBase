import pytest
import pandas as pd
from pandas import DataFrame

from etl_base.geo import get_municipios, get_unidades_saude


def test_municipios():
    municipios = get_municipios()
    assert type(municipios) == DataFrame

    jp = municipios.loc[94]
    assert jp['nome'] == 'JOAO PESSOA'
    assert jp['codigo_ibge'] == 2507507


def test_unidades_saude():
    unidades = get_unidades_saude()
    assert type(unidades) == DataFrame
    
    unidd = unidades.loc[3]
    assert unidd['nome'] == 'USF INTEGRADA GROTAO'
    assert unidd['cnes'] == 2399016
    assert unidd['municipio_id'] == 94
