
import business_logic as bl
import configs
import helpers
def main():
	#validate the input arguments
	args=helpers.validate_arguments()
	#get the connection parameters from config file .
	user, password, host, port, serviceName = [configs.db_config[key] for key in ('username', 'password','host', 'port', 'serviceName')]
	#connect to Oracle database
	con = helpers.connect_db(user, password, host, port, serviceName)
	#Initialize the cursor and execute the query.
	cur=con.cursor()
	print ("Executing the Query")
	cur.execute('select job,sum(SAL) as total_salary from emp group by job')

	if (args.fName):
		#write the output to a file
		bl.wirteToFile(args.fName,cur)
	if (args.wName):
		#write the output to a workbook
		bl.wirteToWorkbook(args.wName,cur)

	#close cursor and db connection
	cur.close()
	con.close()
	return

if __name__ == "__main__":
    main()