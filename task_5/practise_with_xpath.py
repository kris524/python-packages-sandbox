# Question: Extract and Print the Component Details from the IP-XACT file

# Write a Python script to extract and print the vendor, library,
# name, and version details of the component described in the CHI-D-RND
# IP-XACT file. For this, you will need to parse the XML file and locate the relevant information.
import lxml.etree as etree
from typing import List
from lxml.etree import Element

doc = etree.parse("CHI_D_RND_rtl.xml")

ns = {"spirit": "http://www.spiritconsortium.org/XMLSchema/SPIRIT/1685-2009"}


attributes = ["library", "vendor", "version", "name"]
res_attr = []
for attr in attributes:
    via_attributes = doc.xpath(f"//@spirit:{attr}", namespaces=ns)
    res_attr.append(via_attributes[0])

res_dict = dict(zip(attributes, res_attr))

# TODO: Use a for loop to iterate over the elements, makes it look better
direct_access_vendor = doc.xpath("//spirit:vendor/text()", namespaces=ns)
direct_access_library = doc.xpath("//spirit:library/text()", namespaces=ns)
direct_access_version = doc.xpath("//spirit:version/text()", namespaces=ns)
direct_access_name = doc.xpath("//spirit:name/text()", namespaces=ns)


logical_name = doc.xpath("//spirit:logicalName/text()", namespaces=ns)

# Wildcard usage, only get vendorExtensions inside ports, total is 10 but we only get 9
clock_enable = doc.xpath(
    "//spirit:ports/spirit:port/spirit:vendorExtensions/*", namespaces=ns
)

# One way to do it, a bit longer and needs to dig a bit in the xml
requires_driver: List[str] = doc.xpath("//spirit:ports/spirit:port/spirit:wire/spirit:requiresDriver/@spirit:driverType", namespaces=ns)

# Second way much quicker
# requires_driver = doc.xpath("//spirit:requiresDriver/@spirit:driverType", namespaces=ns)


if __name__ == "__main__":
    print(res_dict)
    for key, value in res_dict.items():
        print(f"{key} name from busType attibute", value)

    print(direct_access_vendor)
    print(direct_access_library)
    print(direct_access_version)
    print(direct_access_name)

    print("Logical name first one: ", logical_name[0])

    for c in clock_enable:
        print(c.text)

    print(requires_driver)

    
