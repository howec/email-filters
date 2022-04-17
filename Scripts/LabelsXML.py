#Load Label Templates
TEMPLATE_BODY = open("./Templates/TemplateBody.xml", "r").read()
TEMPLATE_LABEL = open("./Templates/TemplateLabel.xml", "r").read()


FILLER = "0_TEMP_INPUT_LABELS_"
FILLER_LABEL = "1_TEMP_INPUT_LABEL_"
FILLER_LABEL_NESTING = "2_TEMP_INPUT_LABEL_NESTING_"


def count_indent(label_line):
	#Create new indentation in line
	count = 0
	for char in label_line:
		if char == "\t":
			count = count + 1
	return count

def indent_label(label_line):
	#Create new indentation in line
	indent_count = count_indent(label_line)

	count = 0
	new_indentation = ""
	while count < indent_count:
		count = count + 1
		new_indentation = new_indentation + "\t"
	return new_indentation


def fill_template_label(label_line):
	#Fill label template
	labels_xml = TEMPLATE_LABEL
	labels_xml = labels_xml.replace(FILLER_LABEL, label_line)

	return labels_xml


def fill_template_label_nesting(label_xml, label_line_nesting):
	#Fill label nesting template
	labels_xml = label_xml
	labels_xml = labels_xml.replace(FILLER_LABEL_NESTING, label_line_nesting)

	return labels_xml


def generate_label_xml(label_line):
	#Create label function

	indents = indent_label(label_line)
	templated = fill_template_label(label_line.strip())

	split = templated.splitlines()

	temp = ""
	for line in split:
		temp = temp + indents + line + "\n"

	return temp.rstrip("\n") #exclude trailing '\n' character


def generate_label_xml_body(filename):
	def format_nesting(labels_list):
		nesting = ""
		for label in labels_list:
			nesting = nesting + "/" + label
		return nesting.lstrip("/")

	output = ""
	with open(filename) as f:
		stack = []

		for line in f:
			print(f">>> Creating label: {line.strip()}")

			count = count_indent(line)

			if count >= len(stack):
				stack.append(line.strip())
			elif count < len(stack):
				while count < len(stack):
					stack.pop()
				stack.append(line.strip())

			print(f"	stack: {stack}")


			line_nesting = format_nesting(stack)

			xml = generate_label_xml(line.rstrip())
			output = output + fill_template_label_nesting(xml, line_nesting) + "\n"

	print()
	return output.rstrip("\n")



def generate_label_xml_file(txt_label_file, xml_output_file):
	xml_output_file = xml_output_file.replace(".xml", "")
	xml_output_file_name = xml_output_file + ".xml"

	print("Generating Label XML...")
	print()

	body = TEMPLATE_BODY
	xml = generate_label_xml_body(txt_label_file)
	body = body.replace(FILLER, xml)

	print("Finished creating Label XML!")
	print()

	with open("./Outputs/" + xml_output_file_name, "w") as file:
		file.write(body)

	print("Recorded Label XML to output")
	print("=========")

	return xml_output_file
