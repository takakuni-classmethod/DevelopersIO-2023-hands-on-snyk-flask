from main import Calculator
from main import StringUtils
from main import get_user_info
import pytest

class TestMain:

    def test_add_floating_point(self):
        """
        Test adding floating point numbers
        """
        calculator = Calculator()
        result = calculator.add(1.5, 2.7)
        assert pytest.approx(result, 0.001) == 4.2, "Adding 1.5 and 2.7 should approximately equal 4.2"

    def test_add_negative_numbers(self):
        """
        Test adding two negative numbers
        """
        calculator = Calculator()
        result = calculator.add(-2, -3)
        assert result == -5, "Adding -2 and -3 should equal -5"

    def test_add_positive_and_negative(self):
        """
        Test adding a positive and a negative number
        """
        calculator = Calculator()
        result = calculator.add(5, -3)
        assert result == 2, "Adding 5 and -3 should equal 2"

    def test_add_positive_numbers(self):
        """
        Test adding two positive numbers
        """
        calculator = Calculator()
        result = calculator.add(2, 3)
        assert result == 5, "Adding 2 and 3 should equal 5"

    def test_add_with_boolean_input(self):
        """
        Test add method with boolean input.
        """
        calc = Calculator()
        with pytest.raises(TypeError):
            calc.add(True, 5)
        with pytest.raises(TypeError):
            calc.add(10, False)
        with pytest.raises(TypeError):
            calc.add(True, False)

    def test_add_with_float_overflow(self):
        """
        Test add method with float overflow.
        """
        calc = Calculator()
        max_float = float('inf')
        assert calc.add(max_float, 1) == float('inf')
        assert calc.add(max_float, max_float) == float('inf')

    def test_add_with_large_integers(self):
        """
        Test add method with very large integers.
        """
        calc = Calculator()
        large_int1 = 10**1000
        large_int2 = 10**999
        result = calc.add(large_int1, large_int2)
        assert result == large_int1 + large_int2

    def test_add_with_negative_numbers(self):
        """
        Test add method with negative numbers.
        """
        calc = Calculator()
        assert calc.add(-5, -3) == -8
        assert calc.add(-10, 5) == -5
        assert calc.add(7, -2) == 5

    def test_add_with_non_numeric_input(self):
        """
        Test add method with non-numeric input.
        """
        calc = Calculator()
        with pytest.raises(TypeError):
            calc.add("5", 3)
        with pytest.raises(TypeError):
            calc.add(2, "7")
        with pytest.raises(TypeError):
            calc.add("x", "y")

    def test_add_with_none_input(self):
        """
        Test add method with None as input.
        """
        calc = Calculator()
        with pytest.raises(TypeError):
            calc.add(None, 5)
        with pytest.raises(TypeError):
            calc.add(10, None)
        with pytest.raises(TypeError):
            calc.add(None, None)

    def test_add_zero(self):
        """
        Test adding zero to a number
        """
        calculator = Calculator()
        result = calculator.add(10, 0)
        assert result == 10, "Adding 10 and 0 should equal 10"

    def test_count_vowels_all_vowels(self):
        """Test count_vowels with input containing only vowels"""
        string_utils = StringUtils()
        assert string_utils.count_vowels("aeiouAEIOU") == 10

    def test_count_vowels_empty_input(self):
        """Test count_vowels with empty input"""
        string_utils = StringUtils()
        assert string_utils.count_vowels("") == 0

    def test_count_vowels_mixed_case(self):
        """Test count_vowels with mixed case input"""
        string_utils = StringUtils()
        assert string_utils.count_vowels("aEiOu") == 5

    def test_count_vowels_no_vowels(self):
        """Test count_vowels with input containing no vowels"""
        string_utils = StringUtils()
        assert string_utils.count_vowels("Rhythm") == 0

    def test_count_vowels_non_string_input(self):
        """Test count_vowels with non-string input"""
        string_utils = StringUtils()
        with pytest.raises(TypeError):
            string_utils.count_vowels(123)

    def test_count_vowels_none_input(self):
        """Test count_vowels with None input"""
        string_utils = StringUtils()
        with pytest.raises(TypeError):
            string_utils.count_vowels(None)

    def test_count_vowels_unicode_input(self):
        """Test count_vowels with Unicode input"""
        string_utils = StringUtils()
        assert string_utils.count_vowels("áéíóú") == 0

    def test_count_vowels_with_all_vowels(self):
        """
        Test count_vowels method with a string containing only vowels.
        """
        string_utils = StringUtils()
        text = "aeiouAEIOU"
        result = string_utils.count_vowels(text)
        assert result == 10, f"Expected 10 vowels, but got {result}"

    def test_count_vowels_with_empty_string(self):
        """
        Test count_vowels method with an empty string.
        """
        string_utils = StringUtils()
        text = ""
        result = string_utils.count_vowels(text)
        assert result == 0, f"Expected 0 vowels, but got {result}"

    def test_count_vowels_with_mixed_case(self):
        """
        Test count_vowels method with a string containing mixed case vowels and consonants.
        """
        string_utils = StringUtils()
        text = "Hello World"
        result = string_utils.count_vowels(text)
        assert result == 3, f"Expected 3 vowels, but got {result}"

    def test_count_vowels_with_no_vowels(self):
        """
        Test count_vowels method with a string containing no vowels.
        """
        string_utils = StringUtils()
        text = "Rhythm"
        result = string_utils.count_vowels(text)
        assert result == 0, f"Expected 0 vowels, but got {result}"

    def test_count_vowels_with_numbers(self):
        """Test count_vowels with input containing numbers"""
        string_utils = StringUtils()
        assert string_utils.count_vowels("h3ll0 w0rld") == 2

    def test_count_vowels_with_special_characters(self):
        """
        Test count_vowels method with a string containing special characters and vowels.
        """
        string_utils = StringUtils()
        text = "He!!o, W@rld!"
        result = string_utils.count_vowels(text)
        assert result == 2, f"Expected 2 vowels, but got {result}"

    def test_count_vowels_with_special_characters_2(self):
        """Test count_vowels with input containing special characters"""
        string_utils = StringUtils()
        assert string_utils.count_vowels("Hello, World!") == 3

    def test_divide_2(self):
        """
        Test division with positive numerator and denominator
        """
        calculator = Calculator()
        result = calculator.divide(15, 3)
        assert result == 5.0

    def test_divide_by_zero(self):
        """
        Test that dividing by zero raises a ValueError.
        """
        calculator = Calculator()
        with pytest.raises(ValueError, match="0での除算はできません"):
            calculator.divide(10, 0)

    def test_divide_by_zero_2(self):
        """
        Test division by zero raises ValueError
        """
        calculator = Calculator()
        with pytest.raises(ValueError) as excinfo:
            calculator.divide(10, 0)
        assert str(excinfo.value) == "0での除算はできません"

    def test_divide_decimal_numbers(self):
        """
        Test division of decimal numbers.
        """
        calculator = Calculator()
        assert calculator.divide(5.5, 2.2) == pytest.approx(2.5, 0.001)

    def test_divide_decimal_numbers_2(self):
        """
        Test division with decimal numbers
        """
        calculator = Calculator()
        result = calculator.divide(7.5, 2.5)
        assert result == 3.0

    def test_divide_mixed_signs(self):
        """
        Test division with mixed sign numbers.
        """
        calculator = Calculator()
        assert calculator.divide(-10, 2) == -5.0

    def test_divide_negative_numbers(self):
        """
        Test division of negative numbers.
        """
        calculator = Calculator()
        assert calculator.divide(-10, -2) == 5.0

    def test_divide_negative_numbers_2(self):
        """
        Test division with negative numbers
        """
        calculator = Calculator()
        result = calculator.divide(-20, -4)
        assert result == 5.0

    def test_divide_normal_case(self):
        """
        Test division with non-zero denominator
        """
        calculator = Calculator()
        result = calculator.divide(10, 2)
        assert result == 5.0

    def test_divide_positive_numbers(self):
        """
        Test division of positive numbers.
        """
        calculator = Calculator()
        assert calculator.divide(10, 2) == 5.0

    def test_divide_with_float_input(self):
        """
        Test dividing with float input to ensure it works correctly.
        """
        calculator = Calculator()
        result = calculator.divide(10.5, 2.1)
        assert pytest.approx(result, 0.001) == 5.0

    def test_divide_with_large_numbers(self):
        """
        Test dividing with large numbers to check for potential overflow issues.
        """
        calculator = Calculator()
        result = calculator.divide(1e100, 1e50)
        assert result == 1e50

    def test_divide_with_negative_numbers(self):
        """
        Test dividing with negative numbers to ensure correct behavior.
        """
        calculator = Calculator()
        assert calculator.divide(-10, 2) == -5
        assert calculator.divide(10, -2) == -5
        assert calculator.divide(-10, -2) == 5

    def test_divide_with_non_numeric_input(self):
        """
        Test that dividing with non-numeric input raises a TypeError.
        """
        calculator = Calculator()
        with pytest.raises(TypeError):
            calculator.divide("10", 2)
        with pytest.raises(TypeError):
            calculator.divide(10, "2")

    def test_divide_with_small_numbers(self):
        """
        Test dividing with very small numbers to check for potential underflow issues.
        """
        calculator = Calculator()
        result = calculator.divide(1e-100, 1e100)
        assert pytest.approx(result, abs=1e-200) == 1e-200

    def test_get_user_info_2(self):
        """
        Test get_user_info with valid name and age, but invalid email
        """
        with pytest.raises(ValueError, match="無効なメールアドレスです"):
            get_user_info("Alice", age=25, email="alice.example.com")

    def test_get_user_info_3(self):
        """
        Test get_user_info with name and invalid email (without '@')
        """
        name = "John Doe"
        email = "johndoe.example.com"
        
        with pytest.raises(ValueError) as exc_info:
            get_user_info(name, email=email)
        
        assert str(exc_info.value) == "無効なメールアドレスです"

    def test_get_user_info_4(self):
        """
        Test get_user_info with invalid age (float) and valid email.
        """
        with pytest.raises(ValueError, match="年齢は0以上の整数である必要があります"):
            get_user_info("Bob", age=30.5, email="bob@example.com")

    def test_get_user_info_5(self):
        """
        Test get_user_info with invalid age type
        """
        with pytest.raises(ValueError, match="年齢は0以上の整数である必要があります"):
            get_user_info("Jane Doe", age="not an integer")

    def test_get_user_info_empty_name(self):
        """Test get_user_info with an empty name"""
        with pytest.raises(ValueError):
            get_user_info("")

    def test_get_user_info_invalid_age(self):
        """
        Test get_user_info with invalid age input
        """
        with pytest.raises(ValueError, match="年齢は0以上の整数である必要があります"):
            get_user_info("John Doe", age=-5)

    def test_get_user_info_invalid_age_valid_email(self):
        """
        Test get_user_info with invalid age and valid email.
        """
        with pytest.raises(ValueError, match="年齢は0以上の整数である必要があります"):
            get_user_info("Alice", age=-1, email="alice@example.com")

    def test_get_user_info_invalid_email(self):
        """
        Test get_user_info with valid age but invalid email format
        """
        with pytest.raises(ValueError, match="無効なメールアドレスです"):
            get_user_info("John Doe", age=30, email="invalid_email")

    def test_get_user_info_invalid_email_2(self):
        """Test get_user_info with an invalid email address"""
        with pytest.raises(ValueError, match="無効なメールアドレスです"):
            get_user_info("John", email="johndoe.com")

    def test_get_user_info_large_age(self):
        """Test get_user_info with a very large age value"""
        result = get_user_info("John", age=1000000)
        assert result == {"name": "John", "age": 1000000}

    def test_get_user_info_negative_age(self):
        """Test get_user_info with a negative age"""
        with pytest.raises(ValueError, match="年齢は0以上の整数である必要があります"):
            get_user_info("John", age=-1)

    def test_get_user_info_non_integer_age(self):
        """Test get_user_info with a non-integer age"""
        with pytest.raises(ValueError, match="年齢は0以上の整数である必要があります"):
            get_user_info("John", age="twenty")

    def test_get_user_info_none_values(self):
        """Test get_user_info with None values for optional parameters"""
        result = get_user_info("John", age=None, email=None)
        assert result == {"name": "John"}

    def test_get_user_info_special_characters_in_name(self):
        """Test get_user_info with special characters in the name"""
        result = get_user_info("John@Doe#123")
        assert result == {"name": "John@Doe#123"}

    def test_get_user_info_with_invalid_age_and_email(self):
        """
        Test get_user_info with invalid age and email
        """
        with pytest.raises(ValueError) as exc_info:
            get_user_info("John Doe", age=-5, email="invalid_email")
        
        assert str(exc_info.value) == "年齢は0以上の整数である必要があります"

        with pytest.raises(ValueError) as exc_info:
            get_user_info("John Doe", age=30, email="invalid_email")
        
        assert str(exc_info.value) == "無効なメールアドレスです"

    def test_get_user_info_with_invalid_email(self):
        """
        Test get_user_info with name and invalid email (without '@')
        """
        name = "John Doe"
        email = "johndoe.example.com"
        
        with pytest.raises(ValueError) as exc_info:
            get_user_info(name, email=email)
        
        assert str(exc_info.value) == "無効なメールアドレスです"

    def test_get_user_info_zero_age(self):
        """Test get_user_info with age equal to zero"""
        result = get_user_info("John", age=0)
        assert result == {"name": "John", "age": 0}

    def test_is_palindrome_empty_string(self):
        """Test is_palindrome with an empty string"""
        string_utils = StringUtils()
        assert string_utils.is_palindrome("") == True

    def test_is_palindrome_incorrect_type(self):
        """Test is_palindrome with incorrect input type"""
        string_utils = StringUtils()
        with pytest.raises(AttributeError):
            string_utils.is_palindrome(12345)

    def test_is_palindrome_mixed_case(self):
        """Test is_palindrome with mixed case input"""
        string_utils = StringUtils()
        assert string_utils.is_palindrome("RaCeCaR") == True

    def test_is_palindrome_non_alphanumeric(self):
        """Test is_palindrome with non-alphanumeric characters"""
        string_utils = StringUtils()
        assert string_utils.is_palindrome("A man, a plan, a canal: Panama") == True

    def test_is_palindrome_non_palindrome(self):
        """Test is_palindrome with a non-palindrome string"""
        string_utils = StringUtils()
        assert string_utils.is_palindrome("hello") == False

    def test_is_palindrome_none_input(self):
        """Test is_palindrome with None input"""
        string_utils = StringUtils()
        with pytest.raises(AttributeError):
            string_utils.is_palindrome(None)

    def test_is_palindrome_numbers(self):
        """Test is_palindrome with numbers"""
        string_utils = StringUtils()
        assert string_utils.is_palindrome("12321") == True

    def test_is_palindrome_single_character(self):
        """Test is_palindrome with a single character"""
        string_utils = StringUtils()
        assert string_utils.is_palindrome("a") == True

    def test_is_palindrome_unicode(self):
        """Test is_palindrome with unicode characters"""
        string_utils = StringUtils()
        assert string_utils.is_palindrome("世界界世") == True

    def test_is_palindrome_with_empty_string(self):
        """
        Test is_palindrome method with an empty string.
        """
        string_utils = StringUtils()
        assert string_utils.is_palindrome("") == True

    def test_is_palindrome_with_mixed_case(self):
        """
        Test is_palindrome method with a mixed case palindrome.
        """
        string_utils = StringUtils()
        assert string_utils.is_palindrome("RaceCar") == True

    def test_is_palindrome_with_non_palindrome(self):
        """
        Test is_palindrome method with a non-palindrome string.
        """
        string_utils = StringUtils()
        assert string_utils.is_palindrome("hello world") == False

    def test_is_palindrome_with_punctuation(self):
        """
        Test is_palindrome method with a palindrome containing punctuation.
        """
        string_utils = StringUtils()
        assert string_utils.is_palindrome("Was it a car or a cat I saw?") == True

    def test_is_palindrome_with_simple_palindrome(self):
        """
        Test is_palindrome method with a simple palindrome.
        """
        string_utils = StringUtils()
        assert string_utils.is_palindrome("radar") == True

    def test_is_palindrome_with_single_character(self):
        """
        Test is_palindrome method with a single character.
        """
        string_utils = StringUtils()
        assert string_utils.is_palindrome("a") == True

    def test_is_palindrome_with_spaces(self):
        """
        Test is_palindrome method with a palindrome containing spaces.
        """
        string_utils = StringUtils()
        assert string_utils.is_palindrome("A man a plan a canal Panama") == True

    def test_multiply_by_zero(self):
        """
        Test multiplication by zero
        """
        calculator = Calculator()
        result = calculator.multiply(5, 0)
        assert result == 0

    def test_multiply_float_numbers(self):
        """
        Test multiplication of float numbers
        """
        calculator = Calculator()
        result = calculator.multiply(2.5, 3.2)
        assert pytest.approx(result, 0.0001) == 8.0

    def test_multiply_negative_numbers(self):
        """
        Test multiplication of two negative numbers
        """
        calculator = Calculator()
        result = calculator.multiply(-2, -5)
        assert result == 10

    def test_multiply_positive_and_negative(self):
        """
        Test multiplication of a positive and a negative number
        """
        calculator = Calculator()
        result = calculator.multiply(-3, 4)
        assert result == -12

    def test_multiply_positive_numbers(self):
        """
        Test multiplication of two positive numbers
        """
        calculator = Calculator()
        result = calculator.multiply(3, 4)
        assert result == 12

    def test_multiply_with_float_inputs(self):
        """
        Test multiply method with float inputs
        """
        calc = Calculator()
        result = calc.multiply(2.5, 3.0)
        assert result == 7.5, f"Expected 7.5, but got {result}"

    def test_multiply_with_invalid_input_types(self):
        """
        Test multiply method with invalid input types
        """
        calc = Calculator()
        with pytest.raises(TypeError):
            calc.multiply("2", 3)
        with pytest.raises(TypeError):
            calc.multiply(2, "3")
        with pytest.raises(TypeError):
            calc.multiply(None, 3)

    def test_multiply_with_large_numbers(self):
        """
        Test multiply method with large numbers
        """
        calc = Calculator()
        result = calc.multiply(1e10, 1e10)
        assert result == 1e20, f"Expected 1e20, but got {result}"

    def test_multiply_with_negative_numbers(self):
        """
        Test multiply method with negative numbers
        """
        calc = Calculator()
        assert calc.multiply(-2, 3) == -6
        assert calc.multiply(2, -3) == -6
        assert calc.multiply(-2, -3) == 6

    def test_multiply_with_zero(self):
        """
        Test multiply method with zero as one of the inputs
        """
        calc = Calculator()
        assert calc.multiply(0, 5) == 0
        assert calc.multiply(5, 0) == 0

    def test_reverse_string_empty(self):
        """
        Test reverse_string method with an empty string
        """
        string_utils = StringUtils()
        result = string_utils.reverse_string("")
        assert result == "", "Reversing an empty string should return an empty string"

    def test_reverse_string_multiple_characters(self):
        """
        Test reverse_string method with multiple characters
        """
        string_utils = StringUtils()
        result = string_utils.reverse_string("hello")
        assert result == "olleh", "Reversing 'hello' should return 'olleh'"

    def test_reverse_string_single_character(self):
        """
        Test reverse_string method with a single character
        """
        string_utils = StringUtils()
        result = string_utils.reverse_string("a")
        assert result == "a", "Reversing a single character should return the same character"

    def test_reverse_string_with_empty_input(self):
        """Test reverse_string with an empty string input."""
        string_utils = StringUtils()
        result = string_utils.reverse_string("")
        assert result == "", "Reversing an empty string should return an empty string"

    def test_reverse_string_with_non_string_input(self):
        """Test reverse_string with non-string input."""
        string_utils = StringUtils()
        with pytest.raises(TypeError):
            string_utils.reverse_string(123)

    def test_reverse_string_with_none_input(self):
        """Test reverse_string with None input."""
        string_utils = StringUtils()
        with pytest.raises(AttributeError):
            string_utils.reverse_string(None)

    def test_reverse_string_with_spaces(self):
        """
        Test reverse_string method with a string containing spaces
        """
        string_utils = StringUtils()
        result = string_utils.reverse_string("hello world")
        assert result == "dlrow olleh", "Reversing 'hello world' should return 'dlrow olleh'"

    def test_reverse_string_with_special_characters(self):
        """
        Test reverse_string method with special characters
        """
        string_utils = StringUtils()
        result = string_utils.reverse_string("!@#$%^&*()_+")
        assert result == "+_)(*&^%$#@!", "Reversing '!@#$%^&*()_+' should return '+_)(*&^%$#@!'"

    def test_reverse_string_with_special_characters_2(self):
        """Test reverse_string with special characters."""
        string_utils = StringUtils()
        result = string_utils.reverse_string("!@#$%^&*()")
        assert result == ")(*&^%$#@!", "Reversing a string with special characters should work correctly"

    def test_reverse_string_with_unicode_characters(self):
        """Test reverse_string with Unicode characters."""
        string_utils = StringUtils()
        result = string_utils.reverse_string("こんにちは")
        assert result == "はちにんこ", "Reversing a string with Unicode characters should work correctly"

    def test_reverse_string_with_very_long_input(self):
        """Test reverse_string with a very long input string."""
        string_utils = StringUtils()
        long_string = "a" * 1000000
        result = string_utils.reverse_string(long_string)
        assert result == long_string, "Reversing a very long string should work correctly"

    def test_reverse_string_with_whitespace(self):
        """Test reverse_string with whitespace characters."""
        string_utils = StringUtils()
        result = string_utils.reverse_string("  hello  ")
        assert result == "  olleh  ", "Reversing a string with whitespace should preserve the whitespace"

    def test_subtract_floating_point_numbers(self):
        """
        Test subtracting floating-point numbers.
        """
        calculator = Calculator()
        result = calculator.subtract(3.14, 1.59)
        assert abs(result - 1.55) < 1e-10

    def test_subtract_from_zero(self):
        """
        Test subtracting a number from zero.
        """
        calculator = Calculator()
        result = calculator.subtract(0, 5)
        assert result == -5

    def test_subtract_negative_from_positive(self):
        """
        Test subtracting a negative number from a positive number.
        """
        calculator = Calculator()
        result = calculator.subtract(5, -3)
        assert result == 8

    def test_subtract_negative_numbers(self):
        """
        Test subtracting two negative numbers.
        """
        calculator = Calculator()
        result = calculator.subtract(-5, -3)
        assert result == -2

    def test_subtract_positive_from_negative(self):
        """
        Test subtracting a positive number from a negative number.
        """
        calculator = Calculator()
        result = calculator.subtract(-5, 3)
        assert result == -8

    def test_subtract_positive_numbers(self):
        """
        Test subtracting two positive numbers.
        """
        calculator = Calculator()
        result = calculator.subtract(5, 3)
        assert result == 2

    def test_subtract_with_float_inputs(self):
        """
        Test subtract method with float inputs
        """
        calculator = Calculator()
        assert calculator.subtract(5.5, 3.3) == pytest.approx(2.2)
        assert calculator.subtract(-1.1, 2.2) == pytest.approx(-3.3)

    def test_subtract_with_invalid_types(self):
        """
        Test subtract method with invalid input types
        """
        calculator = Calculator()
        with pytest.raises(TypeError):
            calculator.subtract("5", 3)
        with pytest.raises(TypeError):
            calculator.subtract(5, "3")
        with pytest.raises(TypeError):
            calculator.subtract(None, 3)
        with pytest.raises(TypeError):
            calculator.subtract(5, None)

    def test_subtract_with_large_numbers(self):
        """
        Test subtract method with large numbers
        """
        calculator = Calculator()
        assert calculator.subtract(1e100, 1) == 1e100 - 1
        assert calculator.subtract(-1e100, 1) == -1e100 - 1

    def test_subtract_with_negative_numbers(self):
        """
        Test subtract method with negative numbers
        """
        calculator = Calculator()
        assert calculator.subtract(-5, -3) == -2
        assert calculator.subtract(-5, 3) == -8
        assert calculator.subtract(5, -3) == 8

    def test_subtract_with_zero(self):
        """
        Test subtract method with zero
        """
        calculator = Calculator()
        assert calculator.subtract(0, 5) == -5
        assert calculator.subtract(5, 0) == 5
        assert calculator.subtract(0, 0) == 0

    def test_subtract_zero(self):
        """
        Test subtracting zero from a number.
        """
        calculator = Calculator()
        result = calculator.subtract(5, 0)
        assert result == 5