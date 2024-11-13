all:
	python ./plot_rdf.py ../data/poly_ACNCa/poly_ACNCa{,-1}_rdf_Ca_O.csv -l 1:6 -a '2:3:1.2,3:5.5:2.5' '2:3:1.2,3:5.5:2' -n 'Ca-O(P) [Ca$$_2$$Zn$$_2$$P]' 'Ca-O(P) [CaZn$$_2$$P]' -o ../FigureS1a.pdf
	python ./plot_rdf.py ../data/poly_ACNCa/poly_ACNCa{,-1}_rdf_Ca_ACN_N.csv -l 1:6 -a '2:3.2:1.2' '2:3.2:1.2' -n 'Ca-N(ACN) [Ca$$_2$$Zn$$_2$$P]' 'Ca-N(ACN) [CaZn$$_2$$P]' -o ../FigureS1b.pdf
	python ./plot_rdf.py ../data/poly_ACNCa/poly_ACNCa{,-1,-2}_rdf_Zn_Px_N.csv -l 1:5 -a '1.5:2.5:1.2,3:4:10' '1.5:2.5:1.3' '1.5:2.5:1.4' -n 'Zn-N(P) [Ca$$_2$$Zn$$_2$$P]' 'Zn-N(P) [CaZn$$_2$$P]' 'Zn-N(P) [Zn$$_2$$P]' -o ../FigureS2a.pdf
	python ./plot_rdf.py ../data/poly_ACNCa/poly_ACNCa{,-1,-2}_rdf_Zn_O.csv -l 1:6 -a '1.7:2.7:9,2.7:5:1.55' '2.4:3.8:1.3,3.8:5:1.3' '2.4:3.8:1.4,3.8:5:1.4' -n 'Zn-O(P) [Ca$$_2$$Zn$$_2$$P]' 'Zn-O(P) [CaZn$$_2$$P]' 'Zn-O(P) [Zn$$_2$$P]' -o ../FigureS2b.pdf
