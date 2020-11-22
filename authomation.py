import os
import getpass
os.system("tput setaf 5")
print("\t\t\tWelcome to the Menu!!")
os.system("tput setaf 7")


password = getpass.getpass("Enter your password")
if password !="Ritesh":
	print("Password incorrect.....")
	print("Try again...")

r = input("Where to want to run this menu ? (local/remote) : ")
print(r)


while True:
	os.system("clear")
	print("""
	\n
	Press 1 :To run date
	Press 2:To cal
	Press 3:To reboot
	Press 4:To create user
	Press 5:To Run Docker
	press 6:To configure Webserver
	Press 7:To Exit
	""")
	
	ch = input("Enter your choice :")
	print(ch)

	if r == "local":
		 if int(ch) == 1:
			 os.system("date")
			 
		 elif int(ch) == 2:
			 os.system("cal")
		 elif int(ch) ==3:
			 os.system("reboot")
		 elif int(ch) ==4:
			 os.system("useradd")
		 elif int(ch) ==5:
				while True:
					os.system("clear")
					print("""\n1 .To start docker service\n2 .docker running os \n3 .To see docker images \n4 .To stop docker service\n5 .To Pull image from docker hub\n6 .To remove image from local OS\n7 .To run os in docker form available images\n8 .To exit from docker\n9. To enter to help menu of docker""")
					ch1 = int(input("Enter your choice:"))
					print(ch1)
					
					if ch1 == 3:
						os.system("docker images")
					elif ch1 == 2:
						os.system("docker ps")
					elif ch1 == 1:
						os.system("systemctl start docker")
					elif ch1 ==4:
						os.system("systemctl stop docker")
					elif ch1 ==5:
						i=input('Enter image name you want to pull from docker hub')
						os.system("docker pull {}".format(i))
					elif ch1 ==6:
						i=input('To remove image from the local os')
						os.system("docker rmi {}".format(i))
					elif ch1 ==7:
						i=input('Enter Os name from images')
						os.system("docker  run -it {}".format(i))	 					
					elif ch1 ==8:
							break
					elif ch1 ==9:
						os.system("docker --help")
					
					else:
					 	print("Thank you")
					
					
					input("\n Press enter to continue")		
			
		 elif int(ch) == 6:
				while True:
					os.system('clear')
					print('''\n1. To install Apache server and start service \n2. To enable webserver permanetly \n3 To check the status of server\n4. To exit form web server''')
					ch2 = int(input('Enter you choice'))
					print(ch2)
					if ch2 == 1:
						os.system("yum install httpd")
						os.system("systemctl start httpd")
					elif ch2 == 2:
						
						os.system('systemctl enable httpd')
						

					elif ch2 == 3:
						
						os.system("systemctl status httpd")
						
					elif ch2 == 4:
							break
					else:
						print("Thank you")
					input("\n Press enter to continue.....")
		 elif int(ch) == 7:
					while True:
						os.system('clear')
						print('''\n1. To Create key pair\n2.To create security Group\n3.To Launch Instance on cloud\n4.To create EBS volume\n5. To attach EBS volume to Ec2 instance\n6.To create s3 bucket\n7.To put object in s3 bucket\n8.To start instance\n9. To stop instance\n10.To exit from AWS''')
						ch3 = int(input('Enter your choice'))
						print(ch3) 
						if ch3 == 1:
							print('Enter key name to create :- ',end='')
							key_name=input()
							os.system("aws ec2 create-key-pair --key-name {}".format(key_name))
						elif ch3 == 2:
							print('Enter security Name :-  ',end=' ')
							sg_name=input()
							print("Enter VPC id:- ",end='')						
							os.system('aws ec2 create-security-group --group-name {} --description "SG created" --vpc-id      {}'.format(sg_name, vpc_id))
						elif ch3 == 3:
							print('Enter AMI id to Launch Instance :-  ', end='')
								   ami=input()
								   print('Enter Instance type :-  ', end='')
								   itype=input()
								   print('Enter Number of Instances to launch :-  ', end='')
								   count=input()
								   print('Enter Security Group Id to attach to the Instance :-  ', end='')
								   sg_id=input()
								   print('Enter Key to attach to ec2 Instance :-  ', end='')
								   key=input()
								   os.system('aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id subnet-0892eab4da13f00a5 --security-group-ids {} --key-name {}'.format(ami , itype , count , sg_id , key))						









							
						elif ch3 ==4:
							print('Enter Availablity Zone to Create EBS Volume :-  ', end='')
								    az=input()
								    print('Enter Size to create EBS Volume :-  ', end='')
								    ebs_size=input()
								    os.system('aws ec2 create-volume --availability-zone {} --size {}'.format(az , ebs_size))
							




							
						elif ch3 ==5:
							print('Enter EBS Volume ID to Attach to EC2 Instance :-  ', end='')
								    ebs_vid=input()
								    print('Enter EC2 Instance ID to attach EBS Volume :-  ', end='')
								    ec2_id=input()
								    os.system('aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf'.format(ebs_vid , ec2_id))


							
						elif ch3 ==6:
							print('Enter S3 bucket name that must be unique :-  ', end='')
								    s3_name=input()
								    os.system('aws s3api create-bucket --bucket {} --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1'.format(s3_name))

							
						elif ch3 ==7:
							print('Enter Object name to put inside S3 bucket :-  ', end='')
								    object_name=input()
								    print('Enter S3 Bucket name :-  ', end='')
								    s3_name=input()
								    os.system('aws s3 cp /root/{} s3://{} --acl public-read'.format(object_name , s3_name))


								 					
						elif ch3 ==8:
							print('Enter Instance id to start Ec2 instances :-  ', end='')
								    id=input()
								    os.system('aws ec2 start-instances --instance-ids {}'.format(id))


								
						elif ch3 ==9:

							print('Enter Instance id to stop Ec2 instances :-  ', end='')
								    id=input()
								    os.system('aws ec2 stop-instances --instance-ids {}'.format(id))


							
						elif ch3 ==10:
								break
						
						else:
						 	print("Thank you")
						
						
						input("\n Press enter to continue")













		elif r== "remote":
			ip = input("Enter remote ip: ")
			print(ip)
			if int(ch) == 1:
				os.system("ssh {} date".format(ip))
			elif int(ch) == 2:
				os.system("ssh {} cal".format(ip))
			elif int(ch) == 3:
				os.system("ssh {} reboot".format(ip))
			elif int(ch) == 4:
			 	os.system("ssh {}useradd".format(ip))



			elif int(ch) ==5:
					while True:
						os.system("clear")
						print("""\n1 .To start docker service\n2 .docker running os \n3 .To see docker images \n4 .To stop docker service\n5 .To Pull image from docker hub\n6 .To remove image from local OS\n7 .To run os in docker form available images\n8 .To exit from docker\n9. To enter to help menu of docker""")
						ch1 = int(input("Enter your choice:"))
						print(ch1)
						
						if ch1 == 3:
							os.system("ssh {}docker images".format(ip))
						elif ch1 == 2:
							os.system("ssh {}docker ps".format (ip))
						elif ch1 == 1:
							os.system("ssh {}systemctl start docker".format(ip))
						elif ch1 ==4:
							os.system("ssh {} systemctl stop docker".format(ip))
						elif ch1 ==5:
							i=input('Enter image name you want to pull from docker hub')
							os.system("ssh {} docker pull {}".format(ip,i))
						elif ch1 ==6:
							i=input('To remove image from the local os')
							os.system("ssh {} docker rmi {}".format(ip,i))
						elif ch1 ==7:
							i=input('Enter Os name from images')
							os.system("ssh {} docker  run -it {}".format(ip,i))	 					
						elif ch1 ==8:
								break
						elif ch1 ==9:
							os.system("docker --help")
						
						else:
						 	print("Thank you")
						
						
						input("\n Press enter to continue")
				
			 	
			 elif int(ch) == 6:
					while True:
						os.system('clear')
						print('''\n1. To install Apache server and start service \n2. To enable webserver permanetly \n3 To check the status of server\n4. To exit form web server''')
						ch2 = int(input('Enter you choice'))
						print(ch2)
						if ch2 == 1:
							os.system("ssh {} yum install httpd".format(ip))
							os.system("ssh {} systemctl start httpd".format(ip))
						elif ch2 == 2:
							
							os.system('ssh {} systemctl enable httpd'.fromat(ip))
							

						elif ch2 == 3:
							
							os.system("ssh {} systemctl status httpd".format(ip))
							
						elif ch2 == 4:
								break
						else:
							print("Thank you")
						input("\n Press enter to continue.....")





			elif int(ch) == 7:
							while True:
								os.system('clear')
								print('''\n1. To Create key pair\n2.To create security Group\n3.To Launch Instance on cloud\n4.To create EBS volume\n5. To attach EBS volume to Ec2 instance\n6.To create s3 bucket\n7.To put object in s3 bucket\n8.To start instance\n9. To stop instance\n10.To exit from AWS''')
								ch3 = int(input('Enter your choice'))
								print(ch3) 
								if ch3 == 1:
									print('Enter key name to create :- ',end='')
									key_name=input()
									os.system("ssh {} aws ec2 create-key-pair --key-name {}".format(ip ,key_name))
								elif ch3 == 2:
									print('Enter security Name :-  ',end=' ')
									sg_name=input()
									print("Enter VPC id:- ",end='')						
									os.system("ssh {} aws ec2 create-security-group --group-name {} --description "SG created" --vpc-id {}".format(ip,sg_name, vpc_id)
								elif ch3 == 3:
									print('Enter AMI id to Launch Instance :-  ', end='')
										    ami=input()
										    print('Enter Instance type :-  ', end='')
										    itype=input()
										    print('Enter Number of Instances to launch :-  ', end='')
										    count=input()
										    print('Enter Security Group Id to attach to the Instance :-  ', end='')
										    sg_id=input()
										    print('Enter Key to attach to ec2 Instance :-  ', end='')
										    key=input()
										    os.system('ssh {} aws ec2 run-instances --image-id {} --instance-type {} --count {} --subnet-id subnet-0892eab4da13f00a5 --security-group-ids {} --key-name {}'.format(ip,ami , itype , count , sg_id , key))						









									
								elif ch3 ==4:
									print('Enter Availablity Zone to Create EBS Volume :-  ', end='')
										    az=input()
										    print('Enter Size to create EBS Volume :-  ', end='')
										    ebs_size=input()
										    os.system('ssh {} aws ec2 create-volume --availability-zone {} --size {}'.format(ip, az , ebs_size))
									




									
								elif ch3 ==5:
									print('Enter EBS Volume ID to Attach to EC2 Instance :-  ', end='')
										    ebs_vid=input()
										    print('Enter EC2 Instance ID to attach EBS Volume :-  ', end='')
										    ec2_id=input()
										    os.system('ssh {} aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf'.format(ip,ebs_vid , ec2_id))


									
								elif ch3 ==6:
									print('Enter S3 bucket name that must be unique :-  ', end='')
										    s3_name=input()
										    os.system('ssh {} aws s3api create-bucket --bucket {} --region ap-south-1 --create-bucket-configuration LocationConstraint=ap-south-1'.format(ip ,s3_name))

									
								elif ch3 ==7:
									print('Enter Object name to put inside S3 bucket :-  ', end='')
										    object_name=input()
										    print('Enter S3 Bucket name :-  ', end='')
										    s3_name=input()
										    os.system('ssh {} aws s3 cp /root/{} s3://{} --acl public-read'.format(ip ,object_name , s3_name))


										 					
								elif ch3 ==8:
									print('Enter Instance id to start Ec2 instances :-  ', end='')
										    id=input()
										    os.system('ssh {} aws ec2 start-instances --instance-ids {}'.format(ip ,id))


										
								elif ch3 ==9:

									print('Enter Instance id to stop Ec2 instances :-  ', end='')
										    id=input()
										    os.system('ssh {] aws ec2 stop-instances --instance-ids {}'.format(ip , id))


									
								elif ch3 ==10:
										break
								
								else:
								 	print("Thank you")
								
								
								input("\n Press enter to continue")







						
			 	
		 elif int(ch) == 7:
			 	exit()
		 else: 
			 print("not supported")
	else:
		print("Not supported ")
		#break

	input("\nPlease enter to cont....")

  
