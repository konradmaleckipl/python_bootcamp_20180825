from zjazd4.zad1.mathematica.geometry import figures as fig


def test_square_area():
    assert fig.square_area(5) == 25

def test_square_triangle():
    assert fig.triangle_area(10, 5) == 25