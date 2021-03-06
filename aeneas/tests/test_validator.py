#!/usr/bin/env python
# coding=utf-8

import unittest

from . import get_abs_path

from aeneas.logger import Logger
from aeneas.validator import Validator

class TestValidator(unittest.TestCase):

    def file_encoding(self, path, expected):
        validator = Validator()
        result = validator.check_file_encoding(get_abs_path(path))
        self.assertEqual(result.passed, expected)

    def jc(self, string, expected):
        validator = Validator()
        result = validator.check_job_configuration(string)
        self.assertEqual(result.passed, expected)
        if expected:
            self.assertEqual(len(result.errors), 0)
        else:
            self.assertGreater(len(result.errors), 0)

    def tc(self, string, expected):
        validator = Validator()
        result = validator.check_task_configuration(string)
        self.assertEqual(result.passed, expected)
        if expected:
            self.assertEqual(len(result.errors), 0)
        else:
            self.assertGreater(len(result.errors), 0)

    def container(self, path, expected):
        validator = Validator()
        result = validator.check_container(get_abs_path(path))
        self.assertEqual(result.passed, expected)
        if expected:
            self.assertEqual(len(result.errors), 0)
        else:
            self.assertGreater(len(result.errors), 0)

    def test_check_string_encoding(self):
        validator = Validator()
        self.assertFalse(validator._check_string_encoding(u"abcdé".encode("latin-1")))
        self.assertTrue(validator._check_string_encoding(u"abcdé".encode("utf-8")))

    def test_check_reserved_characters(self):
        validator = Validator()
        self.assertFalse(validator._check_reserved_characters("string with ~ reserved char"))
        self.assertTrue(validator._check_reserved_characters("string without reserved char"))

    def test_check_file_encoding_iso8859(self):
        self.file_encoding("res/validator/encoding_iso8859.txt", False)

    def test_check_file_encoding_utf32(self):
        self.file_encoding("res/validator/encoding_utf32.xhtml", False)

    def test_check_file_encoding_utf8(self):
        self.file_encoding("res/validator/encoding_utf8.xhtml", True)

    def test_check_file_encoding_utf8_bom(self):
        self.file_encoding("res/validator/encoding_utf8_bom.xhtml", True)

    def test_check_jc_bad_encoding(self):
        self.jc(u"dummy config string with bad encoding é".encode("latin-1"), False)

    def test_check_jc_reserved_characters(self):
        self.jc("dummy config string with ~ reserved characters", False)

    def test_check_jc_malformed_string(self):
        self.jc("malformed config string", False)

    def test_check_jc_no_key(self):
        self.jc("=malformed", False)

    def test_check_jc_no_value(self):
        self.jc("=malformed", False)

    def test_check_jc_invalid_keys(self):
        self.jc("not=relevant|config=string", False)

    def test_check_jc_missing_required_01(self):
        self.jc("job_language=it|missing=other", False)

    def test_check_jc_missing_required_02(self):
        self.jc("job_language=it|os_job_file_name=output.zip", False)

    def test_check_jc_valid(self):
        self.jc("job_language=it|os_job_file_name=output.zip|os_job_file_container=zip", True)

    def test_check_jc_invalid_value_01(self):
        self.jc("job_language=zzzz|os_job_file_name=output.zip|os_job_file_container=zip", False)

    def test_check_jc_invalid_value_02(self):
        self.jc("job_language=it|os_job_file_name=output.zip|os_job_file_container=zzzzzz", False)

    def test_check_jc_invalid_value_03(self):
        self.jc("job_language=it|os_job_file_name=output.zip|os_job_file_container=zip|is_hierarchy_type=zzzzzz", False)

    def test_check_jc_valid_flat(self):
        self.jc("job_language=it|os_job_file_name=output.zip|os_job_file_container=zip|is_hierarchy_type=flat", True)

    def test_check_jc_missing_paged_required(self):
        self.jc("job_language=it|os_job_file_name=output.zip|os_job_file_container=zip|is_hierarchy_type=paged", False)

    def test_check_jc_valid_paged_with_required(self):
        self.jc("job_language=it|os_job_file_name=output.zip|os_job_file_container=zip|is_hierarchy_type=paged|is_task_dir_name_regex=[0-9]*", True)

    def test_check_jc_invalid_value_04(self):
        self.jc("job_language=it|os_job_file_name=output.zip|os_job_file_container=zip|os_job_file_hierarchy_type=zzzzzz", False)

    def test_check_jc_valid_os_flat(self):
        self.jc("job_language=it|os_job_file_name=output.zip|os_job_file_container=zip|os_job_file_hierarchy_type=flat", True)

    def test_check_jc_valid_os_paged(self):
        self.jc("job_language=it|os_job_file_name=output.zip|os_job_file_container=zip|os_job_file_hierarchy_type=paged", True)

    def test_check_tc_bad_encoding(self):
        self.tc(u"dummy config string with bad encoding é".encode("latin-1"), False)

    def test_check_tc_reserved_characters(self):
        self.tc("dummy config string with ~ reserved characters", False)

    def test_check_tc_malformed(self):
        self.tc("malformed config string", False)

    def test_check_tc_no_key(self):
        self.tc("=malformed", False)

    def test_check_tc_no_value(self):
        self.tc("malformed=", False)

    def test_check_tc_invalid_keys(self):
        self.tc("not=relevant|config=string", False)

    def test_check_tc_missing_required_01(self):
        self.tc("task_language=it|missing=other", False)

    def test_check_tc_missing_required_02(self):
        self.tc("task_language=it|is_text_type=plain|missing=other", False)

    def test_check_tc_missing_required_03(self):
        self.tc("task_language=it|is_text_type=plain|os_task_file_name=output.txt|missing=other", False)

    def test_check_tc_valid(self):
        self.tc("task_language=it|is_text_type=plain|os_task_file_name=output.txt|os_task_file_format=txt", True)

    def test_check_tc_invalid_value_01(self):
        self.tc("task_language=zzzz|is_text_type=plain|os_task_file_name=output.txt|os_task_file_format=txt", False)

    def test_check_tc_invalid_value_02(self):
        self.tc("task_language=it|is_text_type=zzzzzz|os_task_file_name=output.txt|os_task_file_format=txt", False)

    def test_check_tc_invalid_value_03(self):
        self.tc("task_language=it|is_text_type=plain|os_task_file_name=output.txt|os_task_file_format=zzzzzz", False)

    def test_check_tc_missing_required_04(self):
        self.tc("task_language=it|is_text_type=unparsed|os_task_file_name=output.txt|os_task_file_format=txt", False)

    def test_check_tc_valid_with_optional(self):
        self.tc("task_language=it|is_text_type=unparsed|is_text_unparsed_class_regex=ra|is_text_unparsed_id_sort=numeric|os_task_file_name=output.txt|os_task_file_format=txt", True)

    def test_check_tc_valid_with_optional_ignored_01(self):
        self.tc("task_language=it|is_text_type=unparsed|is_text_unparsed_id_regex=f[0-9]*|is_text_unparsed_id_sort=numeric|os_task_file_name=output.txt|os_task_file_format=txt", True)

    def test_check_tc_valid_with_optional_ignored_02(self):
        self.tc("task_language=it|is_text_type=unparsed|is_text_unparsed_class_regex=ra|is_text_unparsed_id_regex=f[0-9]*|is_text_unparsed_id_sort=numeric|os_task_file_name=output.txt|os_task_file_format=txt", True)

    def test_check_tc_missing_required_05(self):
        self.tc("task_language=it|is_text_type=unparsed|is_text_unparsed_id_sort=numeric|os_task_file_name=output.txt|os_task_file_format=txt", False)

    def test_check_tc_missing_required_06(self):
        self.tc("task_language=it|is_text_type=unparsed|is_text_unparsed_class_regex=ra|is_text_unparsed_id_regex=f[0-9]*|os_task_file_name=output.txt|os_task_file_format=txt", False)

    def test_check_tc_valid_smil(self):
        self.tc("task_language=it|is_text_type=plain|os_task_file_name=output.txt|os_task_file_format=smil|os_task_file_smil_page_ref=page.xhtml|os_task_file_smil_audio_ref=../Audio/audio.mp3", True)

    def test_check_tc_missing_required_07(self):
        self.tc("task_language=it|is_text_type=plain|os_task_file_name=output.txt|os_task_file_format=smil|os_task_file_smil_page_ref=page.xhtml", False)

    def test_check_tc_missing_required_08(self):
        self.tc("task_language=it|is_text_type=plain|os_task_file_name=output.txt|os_task_file_format=smil|os_task_file_smil_audio_ref=../Audio/audio.mp3", False)

    def test_check_tc_missing_required_09(self):
        self.tc("task_language=it|is_text_type=plain|os_task_file_name=output.txt|os_task_file_format=smil", False)

    def test_check_tc_valid_aba_auto(self):
        self.tc("task_language=it|is_text_type=plain|os_task_file_name=output.txt|os_task_file_format=txt|task_adjust_boundary_algorithm=auto", True)

    def test_check_tc_invalid_value_04(self):
        self.tc("task_language=it|is_text_type=plain|os_task_file_name=output.txt|os_task_file_format=txt|task_adjust_boundary_algorithm=foo", False)

    def test_check_tc_missing_required_10(self):
        self.tc("task_language=it|is_text_type=plain|os_task_file_name=output.txt|os_task_file_format=txt|task_adjust_boundary_algorithm=rate", False)

    def test_check_tc_valid_aba_rate(self):
        self.tc("task_language=it|is_text_type=plain|os_task_file_name=output.txt|os_task_file_format=txt|task_adjust_boundary_algorithm=rate|task_adjust_boundary_rate_value=21", True)

    def test_check_tc_missing_required_11(self):
        self.tc("task_language=it|is_text_type=plain|os_task_file_name=output.txt|os_task_file_format=txt|task_adjust_boundary_algorithm=percent", False)

    def test_check_tc_valid_aba_percent(self):
        self.tc("task_language=it|is_text_type=plain|os_task_file_name=output.txt|os_task_file_format=txt|task_adjust_boundary_algorithm=percent|task_adjust_boundary_percent_value=50", True)

    def test_check_tc_missing_required_12(self):
        self.tc("task_language=it|is_text_type=plain|os_task_file_name=output.txt|os_task_file_format=txt|task_adjust_boundary_algorithm=aftercurrent", False)

    def test_check_tc_valid_aba_aftercurrent(self):
        self.tc("task_language=it|is_text_type=plain|os_task_file_name=output.txt|os_task_file_format=txt|task_adjust_boundary_algorithm=aftercurrent|task_adjust_boundary_aftercurrent_value=0.200", True)

    def test_check_tc_missing_required_13(self):
        self.tc("task_language=it|is_text_type=plain|os_task_file_name=output.txt|os_task_file_format=txt|task_adjust_boundary_algorithm=beforenext", False)

    def test_check_tc_valid_aba_beforenext(self):
        self.tc("task_language=it|is_text_type=plain|os_task_file_name=output.txt|os_task_file_format=txt|task_adjust_boundary_algorithm=beforenext|task_adjust_boundary_beforenext_value=0.200", True)

    def test_check_tc_missing_required_14(self):
        self.tc("task_language=it|is_text_type=plain|os_task_file_name=output.txt|os_task_file_format=txt|task_adjust_boundary_algorithm=rateagressive", False)

    def test_check_tc_valid_aba_rateaggressive(self):
        self.tc("task_language=it|is_text_type=plain|os_task_file_name=output.txt|os_task_file_format=txt|task_adjust_boundary_algorithm=rateaggressive|task_adjust_boundary_rate_value=21", True)

    def test_check_tc_missing_required_15(self):
        self.tc("task_language=it|is_text_type=plain|os_task_file_name=output.txt|os_task_file_format=txt|task_adjust_boundary_algorithm=offset", False)

    def test_check_tc_valid_aba_offset(self):
        self.tc("task_language=it|is_text_type=plain|os_task_file_name=output.txt|os_task_file_format=txt|task_adjust_boundary_algorithm=offset|task_adjust_boundary_offset_value=0.200", True)

    def test_check_tc_invalid_value_05(self):
        self.tc("task_language=it|is_text_type=plain|os_task_file_name=output.txt|os_task_file_format=txt|os_task_file_head_tail_format=foo", False)

    def test_check_tc_valid_head_tail_format(self):
        self.tc("task_language=it|is_text_type=plain|os_task_file_name=output.txt|os_task_file_format=txt|os_task_file_head_tail_format=add", True)

    def test_check_container_txt_valid(self):
        self.container("res/validator/job_txt_config", True)

    def test_check_container_txt_no_config(self):
        self.container("res/validator/job_no_config", False)

    def test_check_container_txt_bad_config_01(self):
        self.container("res/validator/job_txt_config_bad_1", False)

    def test_check_container_txt_bad_config_02(self):
        self.container("res/validator/job_txt_config_bad_2", False)

    def test_check_container_txt_bad_config_03(self):
        self.container("res/validator/job_txt_config_bad_3", False)
    
    def test_check_container_txt_not_root(self):
        self.container("res/validator/job_txt_config_not_root", True)
    
    def test_check_container_txt_not_root_nested(self):
        self.container("res/validator/job_txt_config_not_root_nested", True)

    def test_check_container_xml_valid(self):
        self.container("res/validator/job_xml_config", True)

    def test_check_container_xml_bad_config_01(self):
        self.container("res/validator/job_xml_config_bad_1", False)

    def test_check_container_xml_bad_config_02(self):
        self.container("res/validator/job_xml_config_bad_2", False)

    def test_check_container_xml_bad_config_03(self):
        self.container("res/validator/job_xml_config_bad_3", False)

    def test_check_container_xml_bad_config_04(self):
        self.container("res/validator/job_xml_config_bad_4", False)

    def test_check_container_xml_not_root(self):
        self.container("res/validator/job_xml_config_not_root", True)

    def test_check_container_xml_not_root_nested(self):
        self.container("res/validator/job_xml_config_not_root_nested", True)

if __name__ == '__main__':
    unittest.main()



