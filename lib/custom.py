class Collection():
	def __init__(self, path):
		self.path = path
		self.objs = []
		self.parse()
	def parse(self):
		lines = [l.rstrip("\n").strip() for l in open(self.path, "r").readlines()]
		obj = ""
		for line in lines:
			if len(line) == 0: continue
			if line[0:1] == "#": continue
			if line.find("BEGIN") > -1:
				tag = line.split("::")[1]
				obj = Custom(tag)
				continue
			elif line == "ENDDEF":
				self.objs.append(obj)
				tag = ""
				obj = None
				continue
			elif tag != "":
				if line.find(":=") == -1: continue
				sl = [s.strip() for s in line.split(":=")]
				if   sl[0].strip() == "name": continue
				if   sl[0][-1] == "+": self.parseAppend (obj, sl)
				elif sl[0][-1] == "#": self.parseSpecial(obj, sl)
				else: setattr(obj, sl[0].strip(), sl[1].strip())
	def parseAppend(self, obj, sl):
		sl[0] = sl[0].rstrip("+").strip()
		vals  = [s.strip() for s in sl[1].split(";")]
		if hasattr(obj, sl[0]): getattr(obj, sl[0]).extend(vals)
		else: setattr(obj, sl[0], vals)
	def parseSpecial(self, obj, sl):
		sl[0] = sl[0].rstrip("#").strip()
		fullline = sl[1].strip("{").strip("}")
		key = fullline.split(":")[0].strip()
		val = fullline.split(":")[1].strip().split(";")
		if hasattr(obj, sl[0]): getattr(obj, sl[0])[key] = [v.strip() for v in val]
		else: setattr(obj, sl[0], {key:[v.strip() for v in val]})
	def get(self, tag):
		thelist = [o.name for o in self.objs]
		if not tag in thelist: raise RuntimeError, "Object '" + tag + "' does not exist in collection '" + self.path + "'"
		return self.objs[thelist.index(tag)]
	def getAllNames(self):
		return [o.name for o in self.obj]

class Custom():
	def __init__(self, name):
		self.name = name
	def setDefault(self, key, value=""):
		if hasattr(self, key): return
		setattr(self, key, value)
	def fillDefaults(self, type="model"):
		if type != "model": return
		self.setDefault("xsecfile"                     )
		self.setDefault("brcorr"                       )
		self.setDefault("noNllNlo"                     )
		self.setDefault("excludeDM"         , "0"      )
		self.setDefault("deltaM"            , "1"      )
		self.setDefault("interpolsize"      , "5"      )
		self.setDefault("histoDeltaM"       , []       )
		self.setDefault("smoothCont"        , "False"  )
		self.setDefault("smoothAlgo"                   )
		self.setDefault("preAlgo"                      )
		self.setDefault("nSmooth"           , "3"      )
		self.setDefault("mode"              , "xsec"   )
		self.setDefault("paramX"            , "mass1"  )
		self.setDefault("paramY"            , "mass2"  )
		self.setDefault("binningX"                     )
		self.setDefault("binningY"                     )
		self.setDefault("rangeX"                       )
		self.setDefault("rangeY"                       )
		self.setDefault("rangeZ"            , "0.001,2")
		self.setDefault("legendX"                      )
		self.setDefault("legendY"                      )
		self.setDefault("nDivX"             , "105"    )
		self.setDefault("nDivY"             , "105"    )
		self.setDefault("plane"             , "obs_xs" )
		self.setDefault("basis"             , "mu"     )
		self.setDefault("skipContour"       , []       )
		self.setDefault("skipContourSmooth" , []       )
		self.setDefault("gr_obs"                       )
		self.setDefault("gr_op1s"                      )
		self.setDefault("gr_om1s"                      )
		self.setDefault("gr_exp"                       )
		self.setDefault("gr_ep1s"                      )
		self.setDefault("gr_em1s"                      )
		self.setDefault("cutGraphsX"        , "0"      )
		self.setDefault("cutGraphsY"        , "0"      )
		self.setDefault("text"              , []       )
		self.setDefault("diag"              , []       )
		

