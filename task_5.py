from task_4 import *


colun1 = trigonometry_array[::,0] 
colun2 = trigonometry_array[::, 1] 



trigonometry_array[0][0], trigonometry_array[0][1] = trigonometry_array[0][1], trigonometry_array[0][0]
trigonometry_array[1][0], trigonometry_array[1][2] = trigonometry_array[1][2], trigonometry_array[1][0]
trigonometry_array[2][0], trigonometry_array[2][2] = trigonometry_array[2][2], trigonometry_array[2][0]

print(trigonometry_array)