 #!/usr/bin/perl -w
 ## _______________________________________________________________ ##
 ## Author Haarlemmer Eric, Greneche Lucas
 ## 
 ## Nom : clean.pl
 ## Date : 11/2025
 ## But : Nettoyer les fichiers d'une collection en enlevant les accents, les 
 ## retours à la ligne, les ponctuations, et les espaces créés inutiles.
 ## _________________________________________________________________ ##
use utf8;

# A paramétrer sur le répertoire et fichier à ouvrir et l'extension de sortie
#clean.pl
 #ouvre la liste des fichiers dans Collection
 #ouvre le contenu de chaque fichier et le passe en minuscule sans accents et pontuactions
 use open ':locale';
 
 open(COLL,"./Collection/Collection") || die ("Erreur d'ouverture du fichier de fichierAlire") ;
 
 while (<COLL>) {
	$_ =~ s/\n//g;
	$fic = $_;
	
	open(CACM,"<./Collection/$fic") || die ("Erreur d'ouverture du fichier de fichier A lire") ;
	open(F,">./Collection/$fic.flt") || die ("Erreur d'ouverture du fichier de fichier A Ecrire") ;
	while (<CACM>) {
		$_ =~ s/\n/ /g; # on remplace les retours à la ligne par des espaces
		$_ =~ tr/àâäéèêëîïù/aaaeeeeiiu/; # on enleve les accents
		$_ =~ s/(\"|\,|\=|\/|\.|\?|\'|\(|\)|\_|\$|\%|\+|\[|\]|\{|\}|\&|\;|\:|\~|\!|\@|\#|\^|\*|\||\<|\>|\-|\\s|\\)/ /g; # on enleve la ponctuation
		$_ =~ s/\s+/ /g; # on enleve les espaces crees qui ne servent à rien
		
		print F lc($_);
	}
	close(CACM);
	close(F);
 }
 close(COLL);
 
