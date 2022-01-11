from detect_languages.detect import DetectLanguages


def test_main_language_python():
    detect = DetectLanguages(True, "./samples/Python", ["programming"], [], False)
    assert detect.main_language == "Python"


def test_main_language_c():
    detect = DetectLanguages(True, "./samples/C", ["programming"], [], False)
    assert detect.main_language == "C"


def test_main_language_c_pp():
    detect = DetectLanguages(True, "./samples/C++", ["programming"], [], False)
    assert detect.main_language == "C++"


def test_main_language_java():
    detect = DetectLanguages(True, "./samples/Java", ["programming"], [], False)
    assert detect.main_language == "Java"


def test_main_language_js():
    detect = DetectLanguages(True, "./samples/JavaScript", ["programming"], [], False)
    assert detect.main_language == "JavaScript"


def test_main_language_go():
    detect = DetectLanguages(True, "./samples/Go", ["programming"], [], False)
    assert detect.main_language == "Go"


def test_main_language_perl():
    detect = DetectLanguages(True, "./samples/Perl", ["programming"], [], False)
    assert detect.main_language == "Perl"


def test_main_language_php():
    detect = DetectLanguages(True, "./samples/PHP", ["programming"], [], False)
    assert detect.main_language == "PHP"


def test_main_language_ruby():
    detect = DetectLanguages(True, "./samples/Ruby", ["programming"], [], False)
    assert detect.main_language == "Ruby"


def test_main_language_rust():
    detect = DetectLanguages(True, "./samples/Rust", ["programming"], [], False)
    assert detect.main_language == "Rust"


def test_not_detected_languages():
    detect = DetectLanguages(True, "./samples/XML", ["programming"], [], False)
    assert len(detect.all_languages) == 0
    assert detect.main_language is None
