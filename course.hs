data Scientist 	 	= Sc String
newtype Database 	= Db [([Scientist], PaperTitle)]
type PaperTitle  	= String
type Path 		= [Scientist]

instance Eq Scientist where
	(Sc name1) == (Sc name2) = (name1 == name2)

instance Show Scientist where
	show (Sc name) = show name

db = Db [
    ([Sc "M. Smith", Sc "G. Martin", Sc "P. Erdos"],"Newtonian Forms of Prime Factors"),
	([Sc "P. Erdos", Sc "W. Reisig"], "Stuttering in Petri Nets"),
	([Sc "M. Smith", Sc "X. Chen"], "First Order Derivates in Structured Programming"),
	([Sc "T. Jablonski",Sc "Z. Hsueh"], "Selfstabilizing Data Structures"),
	([Sc "X. Chen",Sc "L. Li"], "Prime Numbers and Beyond")]

neighbours :: Database -> Scientist -> [Scientist]
neighbours (Db []) _ = []
neighbours (Db ((a,_):xs)) (Sc name) = filter (/= (Sc name)) ((neighbour a) ++ (neighbours (Db xs) (Sc name)))
	where neighbour a
		| (Sc name) `elem` a = a
		| otherwise = []

paths :: Database -> Scientist -> [Path]
paths db start = paths' [] db start
	where paths' visited db start
		| start == (Sc "P. Erdos") = [[start]]
		| start `notElem` visited   = [start:rest | next <- neighbours db start,
													rest <- paths' (start:visited) db next]
		| otherwise		    = []

get_erdos_num :: Database -> Scientist -> Int
get_erdos_num db sc
	| length (paths db sc) == 0 = -1
	| otherwise = minimum (map length (paths db sc)) -1
