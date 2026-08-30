# conftest.py
import os
import xml.etree.ElementTree as ET

def pytest_sessionfinish(session, exitstatus):
    """
    Core pytest hook that executes at the end of the session.
    Regroups testcases into separate suites based on their test module.
    """
    xmlpath = session.config.option.xmlpath
    
    if not xmlpath or not os.path.exists(xmlpath):
        return

    tree = ET.parse(xmlpath)
    root = tree.getroot()
    testcases = root.findall(".//testcase")

    if not testcases:
        return

    suites_by_file = {}

    for testcase in testcases:
        # Fall back to checking the classname attribute (always present)
        # formats like: 'src.my_module.test_logic' or 'tests.test_api'
        class_name = testcase.get('classname', '')
        
        if class_name:
            # Extract the actual test file module name (the last part before a class name)
            # e.g., 'src.my_module.test_logic.TestClass' -> 'test_logic'
            parts = class_name.split('.')
            # Filter out generic test class names to get the module name
            module_parts = [p for p in parts if not p.startswith('Test')]
            suite_name = f"{module_parts[-1]}.py" if module_parts else "unknown_suite.py"
        else:
            # Absolute fallback to the file attribute if it does exist
            file_attr = testcase.get('file', 'unknown_suite.py')
            suite_name = os.path.basename(file_attr)

        # Initialize the suite if it's the first time seeing it
        if suite_name not in suites_by_file:
            suites_by_file[suite_name] = ET.Element('testsuite', name=suite_name)

        suites_by_file[suite_name].append(testcase)

    # Restructure into a clean root containing individual suites
    root.clear()
    root.tag = 'testsuites'

    for suite_element in suites_by_file.values():
        root.append(suite_element)

    tree.write(xmlpath, encoding='utf-8', xml_declaration=True)
