import ktview


filename = "/home/nwchen/Desktop/ldeo/spring/2014_KT15_82_calib_217_155922.txt"
data = ktview.get_data(filename)


def test_data():
    assert len(ktview.get_data(filename)) == 379 - 1
    for i in [e for sublist in data for e in sublist]:
        assert not isinstance(i, str)
