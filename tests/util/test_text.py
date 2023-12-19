from etl_base.util import TextUtils


def test_structure_text():
    structured_text = TextUtils.structure_text(' Teste ã+123 ')

    assert structured_text == 'TESTE A'
