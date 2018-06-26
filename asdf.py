import jinja2
from newDb import my_list
#
# t = Template("Hello {{ something }}!")
# t.render(something="World")
# t = Template("My favorite numbers: {% for n in range(1,10) %}{{n}} " "{% endfor %}")
# print t.render()



templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "document.html"
template = templateEnv.get_template(TEMPLATE_FILE)
outputText = template.render({'something':my_list})  # this is where to put args to the template renderer

# from jinja2 import Template
# with open('template.html.jinja2') as file_:
#     template = Template(file_.read())
# outputText = template.render(my_list)  # this is where to put args to the template renderer

print(outputText)

