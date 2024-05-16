import unittest
import sys
sys.path.append('.')

from src.utils.string_utils import StringUtils

class TestStringUtils(unittest.TestCase):
    
    def test_sanitizar(self):
        str_teste = 'Hoje, eu fui dormir as 00:30 e acordei as 03:00 da manhã. To me sentindo um zumbi (morto-vivo), pode isso?'
        str_teste_sanitizado = 'HOJE DORMIR 00 30 ACORDEI 03 00 MANHA TO SENTINDO ZUMBI MORTO VIVO PODE ISSO'
        self.assertEqual(str_teste_sanitizado, StringUtils.sanitizar(str_teste))

if __name__ == '__main__':
    unittest.main()