from jinja2 import Environment, FileSystemLoader
import pdfkit

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("myreport.html")

template_vars = {"title" : "Lesión X - Paciente X","imagen" : "img1.jpg","leyenda" : "Lesión talámica","Autor" : "Enrique"}

html_out = template.render(template_vars)
#print(html_out)

Html_file = open("report.html","w")
Html_file.write(html_out)
Html_file.close()

pdfkit.from_string('html_out', 'report1.pdf')
pdfkit.from_file('report.html', 'report.pdf')


