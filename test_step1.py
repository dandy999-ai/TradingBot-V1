"""
TradingBot PRO
STEP 1 Test Suite

Test:

1. configurazione rischio;
2. position sizing;
3. limite cash;
4. input invalidi;
5. wrapper risk.py;
6. calcolo stop/target;
7. utilizzo reale dei parametri config.
"""

import unittest

import pandas as pd

from config import (
    INITIAL_CAPITAL,
    RISK_PER_TRADE,
    ATR_STOP,
    ATR_TARGET,
)

from position_size import (
    calculate_position,
)

from risk import (
    calcola_dimensione_posizione,
    calculate_risk_amount,
)

from entry import (
    calculate_entry,
)


class TestConfiguration(unittest.TestCase):

    def test_initial_capital_positive(self):

        self.assertGreater(
            INITIAL_CAPITAL,
            0,
        )

    def test_risk_fraction_valid(self):

        self.assertGreater(
            RISK_PER_TRADE,
            0,
        )

        self.assertLess(
            RISK_PER_TRADE,
            1,
        )

    def test_atr_stop_positive(self):

        self.assertGreater(
            ATR_STOP,
            0,
        )

    def test_atr_target_positive(self):

        self.assertGreater(
            ATR_TARGET,
            0,
        )


class TestPositionSizing(unittest.TestCase):

    def test_basic_one_percent_risk(self):
        """
        Capitale 500
        Rischio 1% = 5

        Entry 100
        Stop 95

        Rischio per azione = 5

        Risultato = 1 azione
        """

        shares = calculate_position(
            capital=500,
            risk_percent=0.01,
            entry_price=100,
            stop_price=95,
            available_cash=500,
        )

        self.assertEqual(
            shares,
            1,
        )

    def test_five_shares(self):
        """
        Capitale 500
        Rischio massimo = 5

        Entry 100
        Stop 99

        Rischio per azione = 1

        Risultato = 5 azioni
        """

        shares = calculate_position(
            capital=500,
            risk_percent=0.01,
            entry_price=100,
            stop_price=99,
            available_cash=500,
        )

        self.assertEqual(
            shares,
            5,
        )

    def test_cash_limit(self):
        """
        Il rischio permetterebbe molte azioni,
        ma abbiamo solo 250 di cash.

        Entry 100.

        Possiamo comprare massimo 2 azioni.
        """

        shares = calculate_position(
            capital=10000,
            risk_percent=0.01,
            entry_price=100,
            stop_price=99,
            available_cash=250,
        )

        self.assertEqual(
            shares,
            2,
        )

    def test_zero_stop_distance(self):

        shares = calculate_position(
            capital=500,
            risk_percent=0.01,
            entry_price=100,
            stop_price=100,
            available_cash=500,
        )

        self.assertEqual(
            shares,
            0,
        )

    def test_zero_capital(self):

        shares = calculate_position(
            capital=0,
            risk_percent=0.01,
            entry_price=100,
            stop_price=95,
        )

        self.assertEqual(
            shares,
            0,
        )

    def test_zero_available_cash(self):

        shares = calculate_position(
            capital=500,
            risk_percent=0.01,
            entry_price=100,
            stop_price=95,
            available_cash=0,
        )

        self.assertEqual(
            shares,
            0,
        )

    def test_invalid_risk_zero(self):

        with self.assertRaises(
            ValueError
        ):

            calculate_position(
                capital=500,
                risk_percent=0,
                entry_price=100,
                stop_price=95,
            )

    def test_invalid_risk_100_percent(self):

        with self.assertRaises(
            ValueError
        ):

            calculate_position(
                capital=500,
                risk_percent=1,
                entry_price=100,
                stop_price=95,
            )

    def test_invalid_entry(self):

        with self.assertRaises(
            ValueError
        ):

            calculate_position(
                capital=500,
                risk_percent=0.01,
                entry_price=0,
                stop_price=95,
            )

    def test_nan_entry(self):

        with self.assertRaises(
            ValueError
        ):

            calculate_position(
                capital=500,
                risk_percent=0.01,
                entry_price=float("nan"),
                stop_price=95,
            )


class TestRiskModule(unittest.TestCase):

    def test_risk_amount(self):

        result = calculate_risk_amount(
            equity=500
        )

        expected = (
            500
            * RISK_PER_TRADE
        )

        self.assertAlmostEqual(
            result,
            expected,
            places=10,
        )

    def test_wrapper_consistency(self):

        direct = calculate_position(
            capital=INITIAL_CAPITAL,
            risk_percent=RISK_PER_TRADE,
            entry_price=100,
            stop_price=95,
            available_cash=INITIAL_CAPITAL,
        )

        wrapper = (
            calcola_dimensione_posizione(
                prezzo_ingresso=100,
                stop_loss=95,
                equity=INITIAL_CAPITAL,
                available_cash=INITIAL_CAPITAL,
            )
        )

        self.assertEqual(
            direct,
            wrapper,
        )


class TestEntryEngine(unittest.TestCase):

    def setUp(self):

        self.df = pd.DataFrame(
            {
                "Close": [
                    95.0,
                    98.0,
                    100.0,
                ],
                "ATR": [
                    1.8,
                    1.9,
                    2.0,
                ],
            }
        )

    def test_entry_price(self):

        result = calculate_entry(
            self.df
        )

        self.assertEqual(
            result["entry"],
            100.0,
        )

    def test_stop_uses_config(self):

        result = calculate_entry(
            self.df
        )

        expected_stop = round(
            100.0
            - 2.0 * ATR_STOP,
            2,
        )

        self.assertEqual(
            result["stop"],
            expected_stop,
        )

    def test_target_uses_config(self):

        result = calculate_entry(
            self.df
        )

        expected_target = round(
            100.0
            + 2.0 * ATR_TARGET,
            2,
        )

        self.assertEqual(
            result["target"],
            expected_target,
        )

    def test_risk_reward(self):

        result = calculate_entry(
            self.df
        )

        expected_rr = round(
            ATR_TARGET
            / ATR_STOP,
            2,
        )

        self.assertEqual(
            result["rr"],
            expected_rr,
        )

    def test_empty_dataframe(self):

        empty_df = pd.DataFrame()

        with self.assertRaises(
            ValueError
        ):

            calculate_entry(
                empty_df
            )

    def test_missing_atr(self):

        invalid_df = pd.DataFrame(
            {
                "Close": [
                    100.0
                ]
            }
        )

        with self.assertRaises(
            ValueError
        ):

            calculate_entry(
                invalid_df
            )

    def test_invalid_atr_zero(self):

        invalid_df = pd.DataFrame(
            {
                "Close": [
                    100.0
                ],
                "ATR": [
                    0.0
                ],
            }
        )

        with self.assertRaises(
            ValueError
        ):

            calculate_entry(
                invalid_df
            )


if __name__ == "__main__":

    print()
    print("=" * 70)
    print("TRADINGBOT PRO - STEP 1 TEST SUITE")
    print("=" * 70)
    print()

    unittest.main(
        verbosity=2
    )