# from run import divisao, informacoes

# def test_divisao():
#     val = 8
#     resp = divisao(val)
#     assert resp == 4
#     assert isinstance(resp, float)
    
# def test_informacoes():
#     resp = informacoes()
    
#     assert isinstance(resp, dict)
#     assert "name" in resp
#     assert "age" in resp
#     assert "is_ok" in resp


# mocks
from test import run

def test_get_discount(mocker):
    mocker.patch('test.run.fetch_discount_rate', return_value=0.20)
    
    
    resp = run.get_discount(100)
    assert resp == 80