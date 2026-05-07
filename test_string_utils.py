#Модуль с тестами для класса StringUtils.
#Покрывает позитивные и негативные сценарии для всех методов.
#"""

import pytest
from string_utils import StringUtils


class TestStringUtilsCapitalize:
    """Тесты метода capitalize"""

    @pytest.fixture
    def utils(self):
        return StringUtils()

    # ---------- ПОЗИТИВНЫЕ ТЕСТЫ ----------

    @pytest.mark.parametrize("input_text, expected", [
        ("skypro", "Skypro"),             # стандартный кейс
        ("hello world", "Hello world"),   # строка с пробелом
        ("python", "Python"),             # обычное слово
        ("a", "A"),                       # одна буква
        ("123abc", "123abc"),             # начинается с цифры
    ])
    def test_capitalize_positive(self, utils, input_text, expected):
        """Позитивные проверки: первая буква становится заглавной"""
        assert utils.capitalize(input_text) == expected

    @pytest.mark.parametrize("input_text, expected", [
        ("SkyPro", "Skypro"),             # ПРОБЛЕМА: остальные буквы стали строчными
        ("TEST", "Test"),                 # ПРОБЛЕМА: заглавные буквы стали строчными
    ])
    def test_capitalize_behavior_note(self, utils, input_text, expected):
        """
        Документирование фактического поведения метода capitalize.
        Встроенный str.capitalize() делает первую букву заглавной,
        а ВСЕ остальные — строчными. Это может быть дефектом.
        """
        assert utils.capitalize(input_text) == expected

    # ---------- НЕГАТИВНЫЕ ТЕСТЫ ----------

    @pytest.mark.parametrize("input_text", [
        "",    # пустая строка
        " ",   # строка из пробела
    ])
    def test_capitalize_empty_or_space(self, utils, input_text):
        """Пустая строка или пробел — результат равен исходному"""
        assert utils.capitalize(input_text) == input_text

    def test_capitalize_none(self, utils):
        """Передача None вызывает AttributeError"""
        with pytest.raises(AttributeError):
            utils.capitalize(None)

    def test_capitalize_int(self, utils):
        """Передача числа вызывает AttributeError (у int нет метода capitalize)"""
        with pytest.raises(AttributeError):
            utils.capitalize(123)


class TestStringUtilsTrim:
    """Тесты метода trim"""

    @pytest.fixture
    def utils(self):
        return StringUtils()

    # ---------- ПОЗИТИВНЫЕ ТЕСТЫ ----------

    @pytest.mark.parametrize("input_text, expected", [
        ("   skypro", "skypro"),          # несколько пробелов в начале
        (" skypro", "skypro"),            # один пробел в начале
        ("skypro", "skypro"),             # нет пробелов
        ("   skypro   ", "skypro   "),    # пробелы только в начале (в конце остаются)
        ("   ", ""),                      # только пробелы
        ("   a", "a"),                    # пробелы перед символом
    ])
    def test_trim_positive(self, utils, input_text, expected):
        """Удаление пробелов в начале строки"""
        assert utils.trim(input_text) == expected

    # ---------- НЕГАТИВНЫЕ ТЕСТЫ ----------

    def test_trim_empty_string(self, utils):
        """Пустая строка остаётся пустой"""
        assert utils.trim("") == ""

    def test_trim_none(self, utils):
        """Передача None вызывает AttributeError"""
        with pytest.raises(AttributeError):
            utils.trim(None)

    def test_trim_tabs_not_removed(self, utils):
        """Табуляция не удаляется (метод удаляет только пробелы)"""
        assert utils.trim("\t skypro") == "\t skypro"


class TestStringUtilsContains:
    """Тесты метода contains"""

    @pytest.fixture
    def utils(self):
        return StringUtils()

    # ---------- ПОЗИТИВНЫЕ ТЕСТЫ ----------

    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "S", True),            # символ в начале
        ("SkyPro", "P", True),            # символ в середине
        ("SkyPro", "o", True),            # символ в конце
        ("SkyPro", "Sky", True),          # подстрока из нескольких символов
        ("SkyPro", "Pro", True),          # подстрока
        ("SkyPro", "U", False),           # символа нет
        ("hello", "x", False),            # символа нет (другой пример)
    ])
    def test_contains_positive(self, utils, string, symbol, expected):
        """Проверка наличия символа/подстроки"""
        assert utils.contains(string, symbol) == expected

    # ---------- НЕГАТИВНЫЕ ТЕСТЫ ----------

    def test_contains_empty_symbol(self, utils):
        """ПОТЕНЦИАЛЬНЫЙ ДЕФЕКТ: пустая строка как искомый символ
        Пустая строка есть в любой строке, метод возвращает True.
        """
        assert utils.contains("SkyPro", "") is True

    def test_contains_empty_string(self, utils):
        """Поиск в пустой строке"""
        assert utils.contains("", "a") is False

    def test_contains_both_empty(self, utils):
        """Поиск пустой строки в пустой строке — возвращает True"""
        assert utils.contains("", "") is True

    def test_contains_none_string(self, utils):
        """Передача None в качестве строки вызывает AttributeError"""
        with pytest.raises(AttributeError):
            utils.contains(None, "a")

    def test_contains_none_symbol(self, utils):
        """Передача None в качестве символа вызывает TypeError"""
        with pytest.raises(TypeError):
            utils.contains("SkyPro", None)


class TestStringUtilsDeleteSymbol:
    """Тесты метода delete_symbol"""

    @pytest.fixture
    def utils(self):
        return StringUtils()

    # ---------- ПОЗИТИВНЫЕ ТЕСТЫ ----------

    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "k", "SyPro"),              # удаление одного символа
        ("SkyPro", "Pro", "Sky"),              # удаление подстроки
        ("Hello World", "o", "Hell Wrld"),     # удаление всех вхождений символа
        ("abc123abc", "abc", "123"),           # удаление всех вхождений подстроки
        ("SkyPro", "X", "SkyPro"),             # символа нет — строка не меняется
        ("aaaa", "a", ""),                      # удаление всех символов
    ])
    def test_delete_symbol_positive(self, utils, string, symbol, expected):
        """Удаление символа/подстроки из строки"""
        assert utils.delete_symbol(string, symbol) == expected

    # ---------- НЕГАТИВНЫЕ ТЕСТЫ ----------

    def test_delete_symbol_empty_string(self, utils):
        """Удаление из пустой строки возвращает пустую строку"""
        assert utils.delete_symbol("", "a") == ""

    def test_delete_symbol_empty_symbol(self, utils):
        """Удаление пустой подстроки не меняет строку"""
        result = utils.delete_symbol("SkyPro", "")
        assert result == "SkyPro"

    def test_delete_symbol_none_string(self, utils):
        """Передача None в качестве строки вызывает AttributeError"""
        with pytest.raises(AttributeError):
            utils.delete_symbol(None, "a")

    def test_delete_symbol_none_symbol(self, utils):
        """Передача None в качестве символа вызывает TypeError"""
        with pytest.raises(TypeError):
            utils.delete_symbol("SkyPro", None)

    def test_delete_symbol_case_sensitivity(self, utils):
        """Удаление чувствительно к регистру"""
        assert utils.delete_symbol("SkyPro", "s") == "SkyPro"
        assert utils.delete_symbol("SkyPro", "S") == "kyPro"