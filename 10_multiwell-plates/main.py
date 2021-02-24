import math


class Plate:
	rowLabels="ABCDEFGHIJKLMNOPQRSTUVWXY"
	mapPositions={'position1D':0,'position2D':1,'wellID':2}

	def __init__(self,id,rows,columns):
		self.id=id
		self.rows=rows
		self.columns=columns
		self.size = self.rows * self.columns
		self.validate={}
		self.data={}
		
		for key in Plate.mapPositions:
			self.validate[key]=[]

		for n in range(1,self.size+1):
			self.data[n]={}
			m=self.map(n,check=False)
			for key in Plate.mapPositions:
				self.validate[key].append(m[Plate.mapPositions[key]])


	def map(self,loc,check=True):

		if(type(loc)==type(15)):
			if(check):
				if not loc in self.validate['position1D']:
					raise Exception("Invalid 1D Plate Position: %s"%str(loc))

			row = int(math.ceil(float(loc)/float(self.columns))) - 1
			col = loc - (row * self.columns) - 1
		elif type(loc) == type((3,2)):
			if check:
				if not loc in self.validate['position2D']:
					raise Exception('Invalid 2D Plate Position: %s' %str(loc))
			row = loc[0] - 1
			col = loc[1] - 1
		elif type(loc) == type('A07'):
			if check:
				if not loc in self.validate['wellID']:
					raise Exception('Invalid Well ID: %s' % str(loc))
			row = Plate.rowLabels.index(loc[0])
			col = int(loc[1:]) - 1
		else:
			raise Exception('Unrecognized Plate Location Type: %s' %str(loc))
		pos = self.columns * row + col + 1
		id = "%s%02d" % (Plate.rowLabels[row],col+1)

		#return a tuple.
		return (pos,(row+1,col+1),id)

	def set(self,loc,propertyName,value):
		m=self.map(loc)
		pos=m[Plate.mapPositions['position1D']]
		self.data[pos][key]=value	

	def get(self,loc,propertyName):
		m=self.map(loc)
		pos=m[Plate.mapPositions['position1D']]

		if(propertyName in self.data[pos]):
			return self.data[pos][propertyName]
		else:
			return




p=Plate("Assay 42",8,12)
print(p.map(1))
print(p.map(96))
print(p.map(97))

