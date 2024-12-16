# Title: x3d-validator
# Version: 1.0.0
# Publisher: NFDI4Culture
# Publication date: December 5, 2024
# Author: Joerg Heseler
# License: CC BY-SA 4.0

from __future__ import print_function
import json
import sys
from lxml import etree

SUCCESS_CODE = 0
ERROR_CODE = 1
DEFAULT_X3D_SCHEMES_PATH = '/usr/share/schemes/x3d' 


class X3DValidatorException(Exception):
    pass

def format_event_outcome_detail_note(format, version, result):
    note = 'format="{}";'.format(format)
    if version is not None:
        note = note + ' version="{}";'.format(version)
    if result is not None:
        note = note + ' result="{}"'.format(result)

    return note

def get_schemes_path_from_arguments():
    for arg in sys.argv:
        if arg.lower().startswith("--schemes-path="):
            return arg.split("=", 1)[1].rstrip('/\\')
    return DEFAULT_X3D_SCHEMES_PATH

def validate_x3d_file(target):
    try:
        try:
            target_xml_tree = etree.parse(target, parser=etree.XMLParser(huge_tree=True))
        except etree.XMLSyntaxError as e:
            raise X3DValidatorException(e)
        target_xml_root = target_xml_tree.getroot()
        format = 'X3D (Extensible 3D)'
        version = target_xml_root.attrib.get('version')
        xsd_path = get_schemes_path_from_arguments() + '/x3d-' + version + '.xsd'
        try:
            xsd_schema = etree.XMLSchema(etree.parse(xsd_path))
        except OSError:
            raise Exception("X3D schemes path not found. Use --schemes-path= to specify its path.")
        validation_successful = xsd_schema.validate(target_xml_tree)
        if not validation_successful:
            error_log = '\n'.join([str(error) for error in xsd_schema.error_log])
            raise X3DValidatorException(error_log)
        
        note = format_event_outcome_detail_note(format, version, '')

        print(
            json.dumps(
                {
                    "eventOutcomeInformation": "pass",
                    "eventOutcomeDetailNote": note,
                    "stdout": target + " validates.",
                }
            )
        )

        return SUCCESS_CODE
    except X3DValidatorException as e:
        print(
            json.dumps(
                {
                    "eventOutcomeInformation": "fail",
                    "eventOutcomeDetailNote": str(e),
                    "stdout": None,
                }
            ),
            file=sys.stderr,
        )
        return ERROR_CODE
    except Exception as e:
        print(e, file=sys.stderr)
        return ERROR_CODE

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'X3D Validator, version 1.0.0')
        print()
        print(f'This script validates X3D files against schemas provided by https://www.web3d.org/specifications/.')
        print()
        print(f'Usage: python x3d-validator.py <X3D file> [options]')
        print()        
        print(f'--schemes-path=<path to X3D schemes>    path to X3D schemes, default={DEFAULT_X3D_SCHEMES_PATH}')
        sys.exit(0)

    target = sys.argv[1]
    sys.exit(validate_x3d_file(target))
