# Title: x3d-validator
# Version: 1.0.0
# Publisher: NFDI4Culture
# Publication date: January 5, 2024
# License: CC BY 4.0

from __future__ import print_function
import json
import subprocess
import sys
from lxml import etree

SUCCESS_CODE = 0
ERROR_CODE = 1

class X3DValidatorException(Exception):
    pass

def format_event_outcome_detail_note(format, version, result):
    note = 'format="{}";'.format(format)
    if version is not None:
        note = note + ' version="{}";'.format(version)
    if result is not None:
        note = note + ' result="{}"'.format(result)

    return note

def main(target):
    try:
        try:
            target_xml_tree = etree.parse(target, parser=etree.XMLParser(huge_tree=True))
        except etree.XMLSyntaxError as e:
            raise X3DValidatorException(e)
        target_xml_root = target_xml_tree.getroot()
        format = 'X3D'
        version = target_xml_root.attrib.get('version')
        xsd_path = '/usr/share/schemes/x3d/x3d-'+version+'.xsd'
        # try:
        xsd_schema = etree.XMLSchema(etree.parse(xsd_path))
        # except etree.XMLSchemaParseError as e:
            # raise X3DValidatorException(e)
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

if __name__ == '__main__':
    target = sys.argv[1]
    sys.exit(main(target))
