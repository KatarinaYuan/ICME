with open('/home1/tsy/AutoInt_test/final_track2_test_no_answer.txt','r') as fin:
	with open('final_track2_test_user_item.txt','w') as f_user_item:
		with open('final_track2_test_finish.txt','w') as f_finish:
			with open('final_track2_test_like.txt','w') as f_like:
				with open('final_track2_test_data.txt','w') as f_data:
					for line in fin:
						lst = line.split('\t')
						f_user_item.write(lst[0]+' '+lst[2]+'\n')
						f_finish.write(lst[6]+'\n')
						f_like.write(lst[7]+'\n')
						f_data.write(' '.join([lst[1],lst[3],lst[4],lst[5],lst[8],lst[9],lst[10],lst[11]])+'\n')
