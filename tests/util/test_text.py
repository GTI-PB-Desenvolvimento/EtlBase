from etl_base.util.text import structure_text


def test_structure_text():
    structured_text = structure_text(' Teste ã+123 ')

    assert structured_text == 'TESTE A'
