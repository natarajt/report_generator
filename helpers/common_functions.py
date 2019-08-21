import argparse
import os.path
import cx_Oracle

def parse_arguments():

	parser = argparse.ArgumentParser(description='Generate Salary Report')

	parser.add_argument('reportName', choices=['salary_aggregate'],metavar='Report_Name',
						help='Name of the report to be generated . (Ex.salary_aggregate) ')

	parser.add_argument('--file', dest='fName', nargs='?',const='salary_aggregate.csv',metavar='Output_File_Name',
						help='Output File name with path (Default = salary_aggregate.csv ) ')
						
	parser.add_argument('--excel', dest='wName', nargs='?',const='salary_aggregate.xlsx',metavar='Output_Workbook_Name',
						help='Output Excel workbook name with path (Default = salary_aggregate.xlsx) ')
						
	parser.add_argument('--table', dest='tName', nargs='?',const='salary_aggregate',metavar='Database_Table_Name',
						help='Output database table name . ')
						
	parser.add_argument('-f','--froce', dest='overwrite', action='store_true',                    
						help='Destination object will be over-written if already present')

	return parser

def validate_arguments():
	parser = parse_arguments()
	args = parser.parse_args()

	if not (args.fName or args.wName or args.tName):
		parser.error('Any one of the output destination needs to be specified')
		
	if (args.fName and os.path.exists(args.fName)):
		if ( not args.overwrite):
			parser.error('File already present . Use Force option to overwrite the file')
	elif (args.fName and args.fName != "salary_aggregate.csv" ) :
		# get dir part of path
		path=os.path.dirname(args.fName)
		if (not os.path.isdir(path)):
			parser.error('Given path is not present , please specify a valid path')

	if (args.wName and os.path.exists(args.wName)):
		if ( not args.overwrite):
			parser.error('Worbook already present . Use Force option to overwrite the file')
	elif (args.wName and args.wName != "salary_aggregate.xlsx") :
		# get dir part of path
		path=os.path.dirname(args.wName)
		if (not os.path.isdir(path)):
			parser.error('Given path is not present , please specify a valid path')
	
	return args

def connect_db(username,password,host,port,serviceName):
	dsn_tns = cx_Oracle.makedsn(host, port, service_name=serviceName)
	con = cx_Oracle.connect(user=username, password=password, dsn=dsn_tns)
	print ("Connected to Database")
	return con