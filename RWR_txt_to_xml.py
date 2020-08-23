import os
import re
import time

def txt_to_xml():
	for filename in os.listdir("text"):
		if filename.endswith(".txt"):
			filename = filename[:-4]
			print(os.path.join("text", filename))
			new_filename = filename.lower()
			new_filename = new_filename.replace(" ","")
			new_filename = new_filename.replace("_","")
			new_filename = new_filename.replace("-","") 			
			with open("text"+"/"+filename+".txt","r") as text_file, open("xml"+"/"+new_filename+".xml","w+") as xml_file, open("default_skeleton.txt","r") as default_skeleton_file:
				xml_file.truncate(0)
				xml_file.write("<model>\n")
				xml_file.write("\t<voxels>\n")
				for text_line in text_file:
					stripped_text_line = text_line.strip()
					print(stripped_text_line)
					stripped_text_line = stripped_text_line.replace(" ","")
					print(stripped_text_line)
					voxel_values = stripped_text_line.split(sep=",")
					print(voxel_values)
					xml_file.write("\t\t<voxel x=\""+voxel_values[0]+"\" y=\""+voxel_values[1]+"\" z=\""+voxel_values[2]+"\" r=\""+str(float(voxel_values[3])/255)+"\" g=\""+str(float(voxel_values[4])/255)+"\" b=\""+str(float(voxel_values[5])/255)+"\" a=\"1.000000\" />\n")
				xml_file.write("\t</voxels>\n")
				time.sleep(1)
				for default_skeleton_line in default_skeleton_file:
					xml_file.write(default_skeleton_line)
				xml_file.write("</model>\n")
	time.sleep(1)		

def organise_xml():
	for filename in os.listdir("xml"):
		print(filename)
		if filename.endswith(".xml"):
			x_min = 0
			x_max = 0
			y_min = 0
			y_max = 0
			z_min = 0
			z_max = 0
			new_content = ""
			filename = filename[:-4]
			print(os.path.join("xml", filename+".xml"))
			time.sleep(1)
			with open("xml"+"/"+filename+".xml","r+") as xml_file:
				for xml_line in xml_file:
					voxel_values = re.findall(r'[+-]?\d+', xml_line)
					voxel_values = [int(voxel_value) for voxel_value in voxel_values]
					xml_line = xml_line.strip()
					if xml_line.startswith("<voxel x"):
						if voxel_values[0] < x_min:
							x_min = voxel_values[0]
						if voxel_values[0] > x_max:
							x_max = voxel_values[0]
						if voxel_values[1] < y_min:
							y_min = voxel_values[1]
						if voxel_values[1] > y_max:
							y_max = voxel_values[1]
						if voxel_values[2] < z_min:
							z_min = voxel_values[2]
						if voxel_values[2] > z_max:
							z_max = voxel_values[2]
				print("x_min = "+str(x_min))
				print("x_max = "+str(x_max))
				print("y_min = "+str(y_min))
				print("y_max = "+str(y_max))
				print("z_min = "+str(z_min))
				print("z_max = "+str(z_max))
			time.sleep(1)	
			with open("xml"+"/"+filename+".xml","r+") as xml_file:
				for xml_line in xml_file:
					voxel_values = re.findall(r'[+-]?\d+', xml_line)
					voxel_values = [int(voxel_value) for voxel_value in voxel_values]
					xml_check_line = xml_line.strip()
					if xml_check_line.startswith("<voxel x"):
						#print("before: "+xml_line)
						xml_line = xml_line.replace("x=\""+str(voxel_values[0])+"\"","x=\""+str(voxel_values[0] - x_max/2)+"\"")
						#xml_line = xml_line.replace("y=\""+str(voxel_values[1])+"\"","y=\""+str(voxel_values[1] - y_max/2)+"\"")
						xml_line = xml_line.replace("z=\""+str(voxel_values[2])+"\"","z=\""+str(voxel_values[2] - z_max/2)+"\"")
						#print("after: "+xml_line)
					new_content += xml_line
				print(new_content.strip())
				xml_file.truncate(0)
				xml_file.seek(0)
				time.sleep(1)
				xml_file.write(new_content.strip())

txt_to_xml()
organise_xml()			