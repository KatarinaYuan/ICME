with open('/home1/tsy/AutoInt_test/final_track2_test_no_answer.txt','r') as fin:
	with open('/home1/tsy/AutoInt_test/final_track2_test_user_item.txt','w') as f_user_item:
		with open('/home1/tsy/AutoInt_test/final_track2_test_finish.txt','w') as f_finish:
			with open('/home1/tsy/AutoInt_test/final_track2_test_like.txt','w') as f_like:
				for line in fin:
					lst = line.split('\t')
					f_user_item.write(lst[0]+' '+lst[2]+'\n')
					data = ' '.join([lst[1],lst[3],lst[4],lst[5],lst[8],lst[9],lst[10],lst[11]])
					f_finish.write(lst[6]+' '+data+'\n')
					f_like.write(lst[7]+' '+data+'\n')
