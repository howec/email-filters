from Scripts import LabelsXML #CREATES a new file
from Scripts import ModifyXML #MODIFIES file in place


label_file_location = "./Inputs/EmailLabels.txt"
labels_xml_name = "1_OutputLabels"
output_labels = LabelsXML.generate_label_xml_file(label_file_location, labels_xml_name)
output_labels = ModifyXML.modify_xml_file(output_labels)


filters_xml_name = "2_OutputFilters"
output_filters = ModifyXML.copy_xml_email_filters(filters_xml_name)
output_filters = ModifyXML.modify_xml_file(output_filters)