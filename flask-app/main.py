class Calculator:
    def add(self, x, y):
        """2つの数値を加算する"""
        return x + y
    
    def subtract(self, x, y):
        """2つの数値を減算する"""
        return x - y
    
    def multiply(self, x, y):
        """2つの数値を乗算する"""
        return x * y
    
    def divide(self, x, y):
        """2つの数値を除算する"""
        if y == 0:
            raise ValueError("0での除算はできません")
        return x / y

class StringUtils:
    def reverse_string(self, text):
        """文字列を反転する"""
        return text[::-1]
    
    def count_vowels(self, text):
        """文字列中の母音の数を数える"""
        vowels = 'aeiouAEIOU'
        return sum(1 for char in text if char in vowels)
    
    def is_palindrome(self, text):
        """文字列が回文かどうかを判定する"""
        cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
        return cleaned_text == cleaned_text[::-1]

def get_user_info(name, age=None, email=None):
    """ユーザー情報を辞書形式で返す"""
    info = {'name': name}
    if age is not None:
        if not isinstance(age, int) or age < 0:
            raise ValueError("年齢は0以上の整数である必要があります")
        info['age'] = age
    if email is not None:
        if '@' not in email:
            raise ValueError("無効なメールアドレスです")
        info['email'] = email
    return info