
import random
x = random.randint(1,6)
print "Vvedite chislo"
n = raw_input ("> ")
if n > 6:
	print "Vvedite ot 1 do 6"
if x == n:
	y = x - n 
	ball = 6
	print "Kolichestvo ballov: "
	print ball
if x > n:
	y = x - n
	abs(y)
	if y == 1:
		ball = ball + 5
		print "Kolichestvo ballov: "
		print ball
	if y == 2:
		ball = ball + 4
		print "Kolichestvo ballov: "
		print ball
	if y == 3:
		ball = ball + 3
		print "Kolichestvo ballov: "
		print ball
	if y == 4:
		ball = ball + 2
		print "Kolichestvo ballov: "
		print ball
	if y == 5:
		ball = ball + 1
		print "Kolichestvo ballov: "
		print ball
if x < n:
	y = x - n
	abs(x)
	if y == 1:
		ball = ball + 5
		print "Kolichestvo ballov: "
		print ball
	if y == 2:
		ball = ball + 4
		print "Kolichestvo ballov: "
		print ball
	if y == 3:
		ball = ball + 3
		print "Kolichestvo ballov: "
		print ball
	if y == 4:
		ball = ball + 2
		print "Kolichestvo ballov: "
		print ball
	if y == 5:
		ball = ball + 1
		print "Kolichestvo ballov: "
		print ball

	


	



	

