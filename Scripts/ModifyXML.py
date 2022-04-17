import json

#Setup Globals
EMAIL_FILTERS = open("./Templates/EmailFilters.xml", "r").read()


INPUT_DICT = None
with open("./Inputs/Inputs.json", "r") as file:
	INPUT_DICT = json.load(file)


EMAIL_1_INPUT = INPUT_DICT.get("primary_email")
EMAIL_2_INPUT = INPUT_DICT.get("secondary_email")
FIRST_NAME_INPUT = INPUT_DICT.get("first_name")
LAST_NAME_INPUT = INPUT_DICT.get("last_name")

EMAIL_1_TEMPLATE = "_TEMP_EMAIL_1_"
EMAIL_2_TEMPLATE = "_TEMP_EMAIL_2_"
FIRST_NAME_TEMPLATE = "_TEMP_FIRST_NAME_"
LAST_NAME_TEMPLATE = "_TEMP_LAST_NAME_"


def copy_xml_email_filters(xml_output_file):
	print("Copying XML...")
	print()

	xml_output_file = xml_output_file.replace(".xml", "")
	xml_output_file = xml_output_file + ".xml"

	with open("./Outputs/" + xml_output_file, "w") as file:
	    file.write(EMAIL_FILTERS)

	print("Copying XML Email Filters")
	print("=========")

	return xml_output_file


def modify_xml_file(xml_filename):
	print("Modifying XML file...")
	print()

	xml_filename = xml_filename.replace(".xml", "")
	xml_filename = xml_filename + ".xml"

	xml_contents = None

	with open("./Outputs/" + xml_filename, "r") as file:
		xml_contents = file.read()

	xml_contents = xml_contents.replace(EMAIL_1_TEMPLATE, EMAIL_1_INPUT)
	xml_contents = xml_contents.replace(EMAIL_2_TEMPLATE, EMAIL_2_INPUT)
	xml_contents = xml_contents.replace(FIRST_NAME_TEMPLATE, FIRST_NAME_INPUT)
	xml_contents = xml_contents.replace(LAST_NAME_TEMPLATE, LAST_NAME_INPUT)

	print("Finished modifying XML file!")
	print()

	with open("./Outputs/" + xml_filename, "w") as file:
	    file.write(xml_contents)

	print("Recorded Modified XML to output")
	print("=========")
	print()

	return xml_filename