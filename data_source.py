import numpy as np

class Level(object):
	_NOMINAL = 0
	_INTERVAL = 1
#end class

class Role(object):
	_INPUT = 0
	_TARGET = 1
	_ID = 2
	_REJECTED = 3
#end class

class Document(object):
	_data = np.array([])
#end class

class Collection(object):
	_raw = Document()
	_train = Document()
	_valid = Document()
	_test = Document()
	_score = Document()

class DataSource(object):
	LEVEL = Level()
	ROLE = Role()
	_meta = []
	_data = Collection()
	
	def __init__(self):
		self._meta = []
		self._data = Collection()
	#end def
	
	'''Editing meta data based. Only can edit Role and Level
	'''
	def edit_meta(self,variable_name=None, role=None, level=None):
		if variable_name is not None:
			index = [idx for idx,val in enumerate(self._meta) if variable_name in val["variable_name"]]
			if role is not None: self._meta[index].update({"role":role})
			if level is not None: self._meta[index].update({"level":level})
		#endif
	#end def
#end class
