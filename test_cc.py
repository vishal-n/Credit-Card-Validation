import validate_credit_card
from unittest import TestCase

class TestLuhnCheck(TestCase):

    def setUp(self):
        pass
    def test_known_sum(self):
        self.assertEquals(67, validate_credit_card.check_sum("7992739871"))

    def test_check_digit(self):
        self.assertEquals(3, validate_credit_card.find_check_digit("7992739871"))

    def test_check_valid(self):
        self.assertFalse(validate_credit_card.is_luhn_valid("abcdefg"))
        self.assertTrue(validate_credit_card.is_luhn_valid("79927398713"))

    def test_check_invalid(self):
        self.assertFalse(validate_credit_card.is_luhn_valid("79927398714"))

    def test_regex(self):
        self.assertTrue(validate_credit_card.check_regex("346340033233241"))
        self.assertFalse(validate_credit_card.check_regex("996340033233241"))

    def test_check_cc(self):
        #amex
        self.assertTrue(validate_credit_card.is_valid_cc("346340033233241"))
        #discover
        self.assertTrue(validate_credit_card.is_valid_cc("6011066253550425"))
        #visa
        self.assertTrue(validate_credit_card.is_valid_cc("4485332611430235"))
        #mc
        self.assertTrue(validate_credit_card.is_valid_cc("5463393720504875"))
        #bad:
        self.assertFalse(validate_credit_card.is_valid_cc("abcdefg"))
        self.assertFalse(validate_credit_card.is_valid_cc("11abcdefg"))
        self.assertFalse(validate_credit_card.is_valid_cc("946340033233241"))
        self.assertFalse(validate_credit_card.is_valid_cc("546339372050487500"))