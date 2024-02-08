import lab3q3
from io import StringIO
from sys import stderr
def test_case1(monkeypatch, capsys):
    number_inputs = StringIO('4\n2\n')

    monkeypatch.setattr('sys.stdin', number_inputs)
    lab3q3.main()
    captured_stdout, captured_stderr = capsys.readouterr()

    assert captured_stdout.strip().find(f'16') != -1

def test_case2(monkeypatch, capsys):
  with open(f"lab3q3.py") as tf:
    head = [next(tf) for _ in range(8)]
    s = tf.read()
    assert(s.find("while") != -1 )

