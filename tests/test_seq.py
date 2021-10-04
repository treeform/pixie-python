import pixie

def test_seqfloat32():
    floats = pixie.SeqFloat32()
    assert floats
    assert len(floats) == 0
    floats.append(100)
    assert len(floats) == 1
    assert floats[0] == 100
    floats.append(200)
    assert floats[1] == 200
    assert len(floats) == 2
    floats[1] = 250
    assert floats[1] == 250
    floats.clear()
    assert len(floats) == 0
    floats.append(50)
    floats.append(55)
    del(floats[0])
    assert len(floats) == 1
    assert floats[0] == 55
    floats2 = pixie.SeqFloat32()
    assert floats != floats2
