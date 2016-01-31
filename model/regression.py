from sklearn import linear_model
from data_source import Role

class Regression(object):
	LINEAR_REGRESSION = 0
	LOGISTIC_REGRESSION = 1
	
	def __init__(self, data=None,type=LINEAR_REGRESSION):
		if data is not None:
			meta = data._meta # getting metadata to select the input and target variable
			# building index of data used for input and target
			input_index = []
			target_index = None
			input_index = [idx for idx,val in enumerate(meta) if val["role"] == Role._INPUT]
			print input_index
			#end for
			train = data._data._train._data
			valid = data._data._valid._data
			test = data._data._test._data
			if len(train) > 0 : # check if there is enough training data or not. You cannot do this things using raw dataset
				regression = linear_model.LinearRegression()
			#end if
		#end if
		print len(data._data._train._data)
	#end def
#end class
