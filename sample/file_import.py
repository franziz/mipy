from data_source import DataSource
from data_source import Document
import numpy as np
import os

class FileImport(object):
	_imported_data = None
	_exported_data = None
	
	''' Accepted parameters:
	file_location | string | None | the file location of the imported file. eg: /root/data.csv
	delimiter     | string | None | string delimiter for csv data
	'''
	def __init__(self, file_location=None, delimiter=None):
		if file_location is not None:
			file_extension = os.path.splitext(file_location)[1] # get file extension
			file_in = open(file_location,"r")
			lines = file_in.readlines()
			file_in.close()
			
			# choose delimiter based on file extension if delimiter is None
			if delimiter is None:
				delimiter = "," if ".csv" in file_extension else ";" if ".tsv" in file_extenstion else None
			#endif
			
			if delimiter is not None:
				# assuming the first line is the header
				header = np.array(lines[0].split(delimiter))
				header = self.string_cleaning(header)
				raw_data = [line.split(delimiter) for line in lines]
				raw_data = np.array(raw_data)
				raw_data = self.string_cleaning(raw_data)
				
				# building meta data for exported data
				self._exported_data = DataSource()
				#print header
				for column_name in header:
					self._exported_data._meta.append({"variable_name":column_name, "role":DataSource.ROLE._INPUT, "level":DataSource.LEVEL._INTERVAL})
				#end for

				document = Document()
				document._data = raw_data[1:]
				self._exported_data._data._raw = document
			#endif
		#end if
	#end def
	
	def string_cleaning(self,string=None):
		if type(string) is np.ndarray:
			if type(string[0]) is np.string_:
				# format [col1,col2,col3]
				string = [row.replace("\n","") for row in string]
			else:
				# format [[col1,col2,col3],[col1,col2,col3]]
				string = [[cell.replace("\n","") for cell in row] for row in string]
			#endif
		#end if
		return np.array(string)
	#end def
#end class

# test script
#file_import = FileImport(file_location="data.csv")
#print type(file_import._exported_data._data._raw._data)
