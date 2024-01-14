
def setup_module(module):
    print("\n  setup module start")

def teardown_module(module):
    print("\n teardown module ending")

def setup_function(funcation):
    if funcation == test1:
        print("\n Setting up test1!")
    elif funcation == test2:
        print("\n Setting up test2!")
    else:
        print("\n Settingup up unknow testcase")


def teardown_function(funcation):
    if funcation == test1:
        print("\n Tearing down test1!")
    elif funcation == test2:
        print("\n Tearing down test2!")
    else:
        print("\n Tearing down unknow testcase")

def test1():
    print("\n Executing Test1")
    assert True

def test2():
    print("\n Executing Test2")
    assert True
