from Data_Finder import DataFinder
from Form_Filler import FormFiller
from Create_Excel import ExcelMaker


data = DataFinder()
form = FormFiller()
excel = ExcelMaker()

data_dic = data.data_scraping()
form.fill_form(data_dic)

