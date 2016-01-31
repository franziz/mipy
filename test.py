from sample.file_import import FileImport
from sample.data_partition import DataPartition
from model.regression import Regression
from data_source import Role

file_import = FileImport("data.csv")
file_import._exported_data.edit_meta("G1",role=Role._TARGET)
print file_import._exported_data._meta
#data_partition = DataPartition(file_import._exported_data, train=0.8, valid=0, test=0.2)
#regression = Regression(data=data_partition._exported_data, type=Regression.LINEAR_REGRESSION)
