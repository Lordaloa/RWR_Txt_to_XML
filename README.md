pyinstaller --onefile RWR_txt_to_xml.py
rwr_editor.exe models/imperialguard001.xml

README:
This little script allows you to convert raw .txt voxels files generated here: https://drububu.com/miscellaneous/voxelizer/?out=obj
to be converted to correct .xml files for RWR_editor_0.14

HOW TO USE:
1) put .txt files which look like this on the inside:
	21, 0, 5, 0, 0, 0
	22, 0, 5, 0, 0, 0
	23, 0, 5, 0, 0, 0
	28, 0, 5, 0, 0, 0
	29, 0, 5, 0, 0, 0
	...
   In the text folder
2) run rwrtx.bat file by either typing in the command prompt run rwrtx.bat or by double clicking the .bat file
   running the python script directly is also possible.