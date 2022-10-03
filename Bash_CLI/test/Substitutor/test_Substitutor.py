from src.Controller import Controller
from src.Substitutor import Substitutor


def test_resolve_env_vars_1():
    controller = Controller()
    substitutor = Substitutor(controller)

    list_tokens = ['echo', 'aboba']

    output = substitutor.resolve_env_vars(list_tokens)

    assert output == 'echo aboba'

def test_resolve_env_vars_2():
    controller = Controller()
    substitutor = Substitutor(controller)

    list_tokens = ['echo', '"', '$HOME', '"']

    output = substitutor.resolve_env_vars(list_tokens)

    assert output == 'echo "$HOME"'

def test_resolve_env_vars_3():
    controller = Controller()
    controller.env_vars['HOME'] = 'aboba'
    substitutor = Substitutor(controller)

    list_tokens = ['echo', '"', '$HOME', '"']

    output = substitutor.resolve_env_vars(list_tokens)

    assert output == 'echo "aboba"'

def test_resolve_env_vars_4():
    controller = Controller()
    controller.env_vars['x'] = 'cat'
    controller.env_vars['y'] = 'echo'
    substitutor = Substitutor(controller)

    list_tokens = ['go', "'$x$y'", '"', '$y', '$x', '"']

    output = substitutor.resolve_env_vars(list_tokens)

    assert output == "go '$x$y' \"echocat\""

def test_resolve_env_vars_5():
    controller = Controller()
    substitutor = Substitutor(controller)

    list_tokens = ['x', '=', 'y']

    output = substitutor.resolve_env_vars(list_tokens)

    assert output == 'x = y'

def test_resolve_env_vars_6():
    controller = Controller()
    substitutor = Substitutor(controller)

    list_tokens = ['pwd', '"', 'home/user/home = ab', '"', '"', 's=t', '"', '-v']

    output = substitutor.resolve_env_vars(list_tokens)

    assert output == 'pwd "home/user/home = ab" "s=t" -v'

def test_resolve_env_vars_7():
    controller = Controller()
    substitutor = Substitutor(controller)

    list_tokens = ['cat', "'$x$y = $exit'"]

    output = substitutor.resolve_env_vars(list_tokens)

    assert output == 'cat \'$x$y = $exit\''

def test_resolve_env_vars_8():
    controller = Controller()
    substitutor = Substitutor(controller)

    list_tokens = ['abc', '\'"raz, dva"\'', '"', " ' aaaa ' hhhhh ' ", '"', "' fffff"]

    output = substitutor.resolve_env_vars(list_tokens)

    assert output == 'abc \'"raz, dva"\' " \' aaaa \' hhhhh \' " \' fffff'

def test_resolve_env_vars_9():
    controller = Controller()
    substitutor = Substitutor(controller)

    list_tokens = ['$x', '$y', '=', '15']

    output = substitutor.resolve_env_vars(list_tokens)

    assert output == '$x$y = 15'

def test_resolve_env_vars_10():
    controller = Controller()
    controller.env_vars['x'] = 'cat'
    controller.env_vars['y'] = 'echo'
    substitutor = Substitutor(controller)

    list_tokens = ['x', '=', 'ex', '|', 'y', '=', 'it', '|', 'wc', '$x', '$y']

    output = substitutor.resolve_env_vars(list_tokens)

    assert output == 'x = ex | y = it | wccatecho'

def test_resolve_env_vars_11():
    controller = Controller()
    controller.env_vars['x'] = 'cat'
    controller.env_vars['y'] = 'echo'
    substitutor = Substitutor(controller)

    list_tokens = ['$x', '\'aboba$y\'', '"', '$x', '$y', '"', '\'"$r\'', '=', '15']

    output = substitutor.resolve_env_vars(list_tokens)

    assert output == 'cat \'aboba$y\' "catecho" \'"$r\' = 15'

def test_resolve_env_vars_12():
    controller = Controller()
    substitutor = Substitutor(controller)

    list_tokens = ['wc', '|', 'cat', '"', ' | echo ', '$___12', '"', '\' x=ex | $123 \'', '|', 'pwd']

    output = substitutor.resolve_env_vars(list_tokens)

    assert output == 'wc | cat " | echo $___12" \' x=ex | $123 \' | pwd'
