import os 

path="~/../..//bess19/Image_fusion/download/GK2A/RAD/VI006/"
os.system('cd {}'.format(path))   
os.system('nohup python {0}DN2RAD.py > {0}log_DN2RAD.txt &'.format(path))
