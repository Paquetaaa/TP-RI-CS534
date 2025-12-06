##AMC
 ## _______________________________________________________________ ##
 ## Author Haarlemmer Eric, Greneche Lucas
 ## 
 ## Nom : remove.pl
 ## Date : 11/2025
 ## But : Enlever les stop-words des fichiers CACM-XX.flt, en utilisant la stop-list common-words, le resultat du filtrage est mis dans des fichiers CACM-XX.stp
 ## _________________________________________________________________ ##


# Indication: On pourra utiliser une table de hash en parcourant le fichier common-words 
# et en associant à chaque terme de fichier pris comme une clé de la table, la valeur 1. 
# Le filtrage se fera en regardant si un terme des fichiers CACM-XX.flt est une clé de cette table de hash ou non. 

#parcours de common-words

my %swords;
open(STOPW,"/Users/lucas/Desktop/Travail/5A/S7/CS534/TP/TP2/TPRIEtu2020/cacm/common_words") || die ("Erreur d'ouverture du fichier de fichierAlire") ;
while (<STOPW>) {
	$_ =~ s/\n//g;
	$swords{$_}=1;
}

while ( my ($cle,$val)=each(%swords) ) {
		 print "motvide: $cle, value: $val\n";
		
}

open(COLL,"<Collection/Collection") || die ("Erreur d'ouverture du fichier de fichierAlire") ;
while (<COLL>) {
	$_ =~ s/\n//g;
	$fic = $_;
	
	open(F,"<Collection/$fic.flt") || die ("Erreur d'ouverture du fichier de fichierALire") ;
	open(STP,">Collection/$fic.stp") || die ("Erreur d'ouverture du fichier de fichierAEcrire") ;

	while (<F>) {
		$_ =~ s/\n//g;
		$_ =~ s/\s+/ /;
	 
	#enlever les stop words
	@tab=split(/ /,$_);
	$nbvide = 0;
	foreach my $v (@tab) { #if exists $hash{$key}
		if (!$swords{$v}) { 		#le mot courant exist dans le hash, on ne l'écrit pas sinon on l'ecrit
			print STP $v . " ";
		}
		else { $nbvide++; print "(**". $v . " ";}
	}
	print $fic . " " . $nbvide . "\n";

	}
	close(F);
	close(STP);
 }
 close(COLL);
