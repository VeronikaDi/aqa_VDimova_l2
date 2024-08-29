import xml.etree.ElementTree as ET
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def find_incoming_value(file, group_number):
    tree = ET.parse(file)
    root = tree.getroot()

    for group in root.findall('group'):
        number = group.find('number').text
        if number == group_number:
            incoming = group.find('timingExbytes/incoming').text
            return incoming

    return None


if __name__ == "__main__":
    xml_file = 'ideas_for_test/work_with_xml/groups.xml'
    group_number = '3'

    incoming_value = find_incoming_value(xml_file, group_number)

    if incoming_value:
        logger.info(f"Incoming value for group {group_number}: {incoming_value}")
    else:
        logger.info(f"Group with number {group_number} not found.")
