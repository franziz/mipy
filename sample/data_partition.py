import numpy as np
from data_source import DataSource
from copy import deepcopy

class DataPartition(object):
	_imported_data = None
	_exported_data = None
	def __init__(self, data=None, train=0.6, valid=0.3, test=0.1):
		if data is not None:
			_imported_data = deepcopy(data)
			if type(data) is DataSource:
				np.random.shuffle(data._data._raw._data)
				total_data = len(data._data._raw._data)
				new_data = deepcopy(data)
				#print new_data._raw._data
				new_data._data._train._data = data._data._raw._data[:train*total_data]
				new_data._data._valid._data = data._data._raw._data[train*total_data:((train*total_data)+(valid*total_data))]
				new_data._data._test._data = data._data._raw._data[((train*total_data)+(valid*total_data)):] # assume the last test data is the remaining, so no need to speciy the end
				self._exported_data = new_data
			#end if
		#end if
	#enddef
#endclass
