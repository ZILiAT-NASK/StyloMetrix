import json
import unittest
from unittest.mock import MagicMock, Mock, call, patch

from src.stylo_metrix.pipeline.new_pipe import SMComponent


class TestSMComponent(unittest.TestCase):
    @patch("spacy.load")
    def setUp(
        self,
        mock_nlp,
    ) -> None:
        self.metrics_ids = list(range(363, 536))
        self.metrics_ids.remove(366)
        self.customization = None
        self.mock_nlp = mock_nlp

    @patch("src.stylo_metrix.pipeline.new_pipe.Doc")
    @patch("src.stylo_metrix.pipeline.new_pipe.SMComponent._assign_name")
    @patch("src.stylo_metrix.pipeline.new_pipe.pl_components", [Mock(), Mock()])
    def test_init_pl(
        self,
        mock_assign_name,
        MockDoc,
    ):

        set_extension_expected_calls = [
            call("name", default=None, force=True),
            call("assign_name", method=mock_assign_name, force=True),
            call("metrics", default=dict(), force=True),
        ]

        self.mock_nlp.config = {"nlp": {"lang": "pl"}}

        component = SMComponent(self.mock_nlp, self.metrics_ids, self.customization)

        self.assertSequenceEqual(component.metrics_ids, self.metrics_ids)
        self.assertEqual(component.customization, self.customization)
        MockDoc.set_extension.assert_has_calls(set_extension_expected_calls)
        self.assertEqual(MockDoc.set_extension.call_count, 3)
        self.assertEqual(len(component.components), 2)

    @patch("src.stylo_metrix.pipeline.new_pipe.Doc")
    @patch("src.stylo_metrix.pipeline.new_pipe.SMComponent._assign_name")
    @patch("src.stylo_metrix.pipeline.new_pipe.de_components", [Mock(), Mock()])
    def test_init_de(
        self,
        mock_assign_name,
        MockDoc,
    ):

        set_extension_expected_calls = [
            call("name", default=None, force=True),
            call("assign_name", method=mock_assign_name, force=True),
            call("metrics", default=dict(), force=True),
        ]

        self.mock_nlp.config = {"nlp": {"lang": "de"}}

        component = SMComponent(self.mock_nlp, self.metrics_ids, self.customization)

        self.assertSequenceEqual(component.metrics_ids, self.metrics_ids)
        self.assertEqual(component.customization, self.customization)
        MockDoc.set_extension.assert_has_calls(set_extension_expected_calls)
        self.assertEqual(MockDoc.set_extension.call_count, 3)
        self.assertEqual(len(component.components), 2)

    @patch("src.stylo_metrix.pipeline.new_pipe.CP_en")
    @patch("src.stylo_metrix.pipeline.new_pipe.Doc")
    @patch("src.stylo_metrix.pipeline.new_pipe.SMComponent._assign_name")
    @patch("src.stylo_metrix.pipeline.new_pipe.en_components", [Mock(), Mock()])
    def test_init_en(self, mock_assign_name, MockDoc, MockCP_en):

        set_extension_expected_calls = [
            call("name", default=None, force=True),
            call("assign_name", method=mock_assign_name, force=True),
            call("metrics", default=dict(), force=True),
        ]
        tokenizer = self.mock_nlp.tokenizer

        self.mock_nlp.config = {"nlp": {"lang": "en"}}

        component = SMComponent(self.mock_nlp, self.metrics_ids, self.customization)

        self.assertSequenceEqual(component.metrics_ids, self.metrics_ids)
        self.assertEqual(component.customization, self.customization)
        MockDoc.set_extension.assert_has_calls(set_extension_expected_calls)
        self.assertEqual(MockDoc.set_extension.call_count, 3)
        self.assertEqual(len(component.components), 2)
        MockCP_en.assert_called_once_with(tokenizer)

    @patch("src.stylo_metrix.pipeline.new_pipe.CP_ukr")
    @patch("src.stylo_metrix.pipeline.new_pipe.Doc")
    @patch("src.stylo_metrix.pipeline.new_pipe.SMComponent._assign_name")
    @patch("src.stylo_metrix.pipeline.new_pipe.ukr_components", [Mock(), Mock()])
    def test_init_ukr(self, mock_assign_name, MockDoc, MockCP_ukr):

        set_extension_expected_calls = [
            call("name", default=None, force=True),
            call("assign_name", method=mock_assign_name, force=True),
            call("metrics", default=dict(), force=True),
        ]
        tokenizer = self.mock_nlp.tokenizer

        self.mock_nlp.config = {"nlp": {"lang": "uk"}}

        component = SMComponent(self.mock_nlp, self.metrics_ids, self.customization)

        self.assertSequenceEqual(component.metrics_ids, self.metrics_ids)
        self.assertEqual(component.customization, self.customization)
        MockDoc.set_extension.assert_has_calls(set_extension_expected_calls)
        self.assertEqual(MockDoc.set_extension.call_count, 3)
        self.assertEqual(len(component.components), 2)
        MockCP_ukr.assert_called_once_with(tokenizer)

    @patch("src.stylo_metrix.pipeline.new_pipe.CP_ru")
    @patch("src.stylo_metrix.pipeline.new_pipe.Doc")
    @patch("src.stylo_metrix.pipeline.new_pipe.SMComponent._assign_name")
    @patch("src.stylo_metrix.pipeline.new_pipe.ru_components", [Mock(), Mock()])
    def test_init_ru(self, mock_assign_name, MockDoc, MockCP_ru):

        set_extension_expected_calls = [
            call("name", default=None, force=True),
            call("assign_name", method=mock_assign_name, force=True),
            call("metrics", default=dict(), force=True),
        ]
        tokenizer = self.mock_nlp.tokenizer

        self.mock_nlp.config = {"nlp": {"lang": "ru"}}

        component = SMComponent(self.mock_nlp, self.metrics_ids, self.customization)

        self.assertSequenceEqual(component.metrics_ids, self.metrics_ids)
        self.assertEqual(component.customization, self.customization)
        MockDoc.set_extension.assert_has_calls(set_extension_expected_calls)
        self.assertEqual(MockDoc.set_extension.call_count, 3)
        self.assertEqual(len(component.components), 2)
        MockCP_ru.assert_called_once_with(tokenizer)

    @patch("src.stylo_metrix.pipeline.new_pipe.len")
    @patch("src.stylo_metrix.pipeline.new_pipe.Metric")
    @patch(
        "src.stylo_metrix.pipeline.new_pipe.pl_components", [MagicMock(), MagicMock()]
    )
    def test_basic_call(self, MockMetric, mock_len):

        self.mock_nlp.config = {"nlp": {"lang": "pl"}}
        doc = self.mock_nlp("Raz dwa trzy")
        mock_len.return_value = 3
        component = SMComponent(self.mock_nlp, self.metrics_ids, self.customization)
        component(doc)

        for comp in component.components:
            comp.assert_called_once_with(doc)
            doc = comp(doc)

        expected_calls = [[call(i), call()(doc)] for i in self.metrics_ids]

        MockMetric.get_by_id.assert_has_calls(sum(expected_calls, []))

    @patch("src.stylo_metrix.pipeline.new_pipe.len")
    @patch("src.stylo_metrix.pipeline.new_pipe.Metric")
    @patch(
        "src.stylo_metrix.pipeline.new_pipe.pl_components", [MagicMock(), MagicMock()]
    )
    def test_customization_call(self, MockMetric, mock_len):

        self.mock_nlp.config = {"nlp": {"lang": "pl"}}
        doc = self.mock_nlp("Raz dwa trzy")
        mock_len.return_value = 3
        customization = MagicMock()
        component = SMComponent(self.mock_nlp, self.metrics_ids, customization)
        component(doc)

        for comp in component.components + [customization]:
            comp.assert_called_once_with(doc)
            doc = comp(doc)

        expected_calls = [[call(i), call()(doc)] for i in self.metrics_ids]

        MockMetric.get_by_id.assert_has_calls(sum(expected_calls, []))


if __name__ == "__main__":
    unittest.main()
