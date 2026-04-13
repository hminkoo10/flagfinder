from flagfinder import findflag_labeled, findflags_labeled


def test_findflag_labeled():
    text = "hello DH{test123} world"
    assert findflag_labeled("flag", "DH", text) == "flag: DH{test123}"


def test_findflag_labeled_none():
    text = "hello world"
    assert findflag_labeled("flag", "DH", text) is None


def test_findflags_labeled():
    text = "A DH{one} B DH{two} C"
    assert findflags_labeled("flag", "DH", text) == [
        "flag: DH{one}",
        "flag: DH{two}",
    ]