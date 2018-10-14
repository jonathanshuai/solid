"""This Exporter class is to look at Dependency Inversion Principle.

The dependency inversion principle says that a dependency should be on 
abstractions not concretions.

A. High-level modules should not depend upon low-level modules. Both should 
depend upon abstractions.
B. Abstractions should not depend on details. Details should depend upon 
abstractions.

Here's an example to drive the point home:
"""


class FileSaver:
    def __init__(self, pdf_exporter):
        self.pdf_exporter = pdf_exporter

    def save_file(self):
        self.pdf_exporter.convert_to_pdf()
        self.pdf_exporter.pdf_export()
        print("Saving file...")


class PDFExporter:
    def __init__(self):
        pass

    def convert_to_pdf(self):
        print("Converting to pdf...")

    def pdf_export(self):
        print("Exporting as pdf...")

pdf_exporter = PDFExporter()
file_saver = FileSaver(pdf_exporter)
file_saver.save_file()

print('-' * 15)

# Here's an example of an FileSaver class which takes a PDFExporter. It then 
# depends on the low-level module and calls things like convert_to_pdf and pdf_export.

# Instead of relying on that, we should abstract the process, and have the
# lower level modules implement these abstractions.

class FileSaver:
    def __init__(self, exporter):
        self.exporter = exporter

    def save_file(self):
        print("Saving file...")
        self.exporter.export()

class Exporter:
    def __init__(self):
        pass

    def export(self):
        pass

class PDFExporter(Exporter):
    def __init__(self):
        super(PDFExporter, self).__init__()

    def convert_to_pdf(self):
        print("Converting to pdf...")

    def export(self):
        self.convert_to_pdf()
        print("Exporting as pdf...")

class CSVExporter(Exporter):
    def __init__(self):
        super(CSVExporter, self).__init__()

    def export(self):
        print("Exporting as csv...")


pdf_exporter = PDFExporter()
file_saver = FileSaver(pdf_exporter)
file_saver.save_file()

csv_exporter = CSVExporter()
file_saver = FileSaver(csv_exporter)
file_saver.save_file()

# Now, we can see that instead of FileSaver having to know about the details of different
# export methods, we can abstract them as an Exporter and implement them separately.
# Our high level FileSaver no longer has to think about how these exports are going to be 
# implemented, and we've successfully moved dependencies out.