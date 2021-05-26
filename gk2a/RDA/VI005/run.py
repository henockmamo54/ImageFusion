import os 

path="~/../..//bess19/Image_fusion/download/GK2A/RAD/VI005/"
os.system('cd {}'.format(path))   
os.system('nohup python {0}DN2RAD.py > {0}logVI005_DN2RAD.txt &'.format(path))
