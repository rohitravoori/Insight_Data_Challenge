import time
import bisect

# Opening the files
input_file = open("./input/itcont.txt", "r")
percentile_file = open("./input/percentile.txt","r")
output_file = open("./output/repeat_donors.txt","w")

donations_records = {}
repeat_donations_dict={}
percentile = int(percentile_file.read())


def repeat_donor_check(data):
	# Unpacking the data
	cmte_id,candidate_name,zip_code,t_date,t_amount,individual_id = data
	# First 5 digits of zipcode
	zip_code= (str(zip_code)[:5])
	# Add donation records from new entries
	if (candidate_name,zip_code) not in donations_records:
		donations_records[candidate_name, zip_code]= [cmte_id, t_date, t_amount]
	# Repeat donations
	else :
		cmte_id2,t_date2,t_amount2 = donations_records[candidate_name, zip_code]
		new_date1 = t_date2[0:2]+"/"+t_date2[2:4]+"/"+t_date2[4:]
		new_date2 = t_date[0:2]+"/"+t_date[2:4]+"/"+t_date[4:]
		newdate1 = time.strptime(new_date1, "%m/%d/%Y")
		newdate2 = time.strptime(new_date2, "%m/%d/%Y")
		# Check to see that first and later donations
		if newdate2>newdate1:
			year = t_date[4:]
			# Adding repeated donations
			if (cmte_id,zip_code,year) in repeat_donations_dict:
				amount,count,amount_list = repeat_donations_dict[(cmte_id, zip_code, year)]
				amount=int(t_amount) + int(amount)
				count+=1
				repeat_donations_dict[(cmte_id, zip_code, year)]=[amount, count, bisect.insort(amount_list, int(t_amount))]
				index = (float(percentile) / 100) * float(len(amount_list))
				index=int(index)
				percentile_value = amount_list[index]
			else :
				amount = int(t_amount)
				count = 1
				repeat_donations_dict[(cmte_id, zip_code, year)] = [amount, count, [amount]]
				percentile_value = amount
			output_file.write(str(cmte_id) + "|" +str(zip_code)+ "|" + str(year)  + "|" +  str(percentile_value) + "|"+ str(amount) +  "|" + str(count) +"\n")
		else :
			year = t_date2[4:]
			if (cmte_id2, zip_code, year) in repeat_donations_dict:
				amount, count,amount_list = repeat_donations_dict[(cmte_id2, zip_code, year)]
				amount = int(t_amount2) + int (amount)
				count += 1
				repeat_donations_dict[(cmte_id2, zip_code, year)] = [amount, count, bisect.insort(amount_list, int(t_amount2))]
				print amount_list
				index = (float(percentile) / 100) * float(len(amount_list))
				index = int(index)
				percentile_value = amount_list[index]
			else:
				amount = t_amount2
				count = 1
				repeat_donations_dict[(cmte_id2, zip_code, year)] = [amount, count, [amount]]
				percentile_value = amount
			output_file.write(str(cmte_id2) + "|" +str(zip_code)+ "|" + str(year)  + "|" + str(percentile_value) + "|" + str(amount) + "|" + str(count) + "\n")
			donations_records[candidate_name, zip_code]= [cmte_id, t_date, t_amount]


def check_data(data):
	cmte_id,candidate_name,zip_code,t_date,t_amount,individual_id = data
	# Checking for individual and non-empty entries
	if individual_id or not t_amount or not cmte_id:
		return False
	# Checking Name Validity
	k = unicode(candidate_name,'utf-8')
	if k.isnumeric() or (not candidate_name) :
		return False
	# Checking Data Validity
	k = unicode(t_date,'utf-8')
	if (not k.isnumeric()) or (not t_date) or len(t_date)!=8:
		return False
	# Checking Zip Code Validity
	k = unicode(zip_code,'utf-8')
	if (not k.isnumeric()) or (not zip_code) or len(zip_code) < 5:
		return False
	else :
		return True


for line in input_file:
	data = line.split("|")
	# Retrieving the required data
	req_data = [data[0],data[7],data[10],data[13],data[14],data[15]]
	# Check for clean data
	if check_data(req_data):
		repeat_donor_check(req_data)

