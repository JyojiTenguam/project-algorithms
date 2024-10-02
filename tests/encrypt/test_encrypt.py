from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match='tipo inválido para key'):
        encrypt_message('trybe', 'trybe')

    with pytest.raises(TypeError, match='tipo inválido para message'):
        encrypt_message(3, 3)

    assert encrypt_message('trybe', -1) == 'ebyrt'
    assert encrypt_message('trybe', 3) == 'yrt_eb'
    assert encrypt_message('trybe', 2) == 'eby_rt'
    assert encrypt_message('trybe', 1) == 't_ebyr'
    assert encrypt_message('trybe', 4) == 'e_byrt'
    assert encrypt_message('trybe', 5) == 'ebyrt'
