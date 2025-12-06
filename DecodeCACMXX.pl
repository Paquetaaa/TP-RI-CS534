 ## _______________________________________________________________ ##
 ## Auteurs Haarlemmer Eric, Greneche Lucas
 ## 
 ## Nom : DecodeCACMXX.pl
 ## Date : 11/2025
 ## But : Ouvre le fichier cacm.all et cree les fichiers de contenu de type CACM-XX, selon les balise .I
 ## _________________________________________________________________ ##


   open(F,"cacm.all") || die "Erreur d'ouverture du fichier $FileName\n";
   my $str="";
   my $Num=0;
   my $Path="Collection";

   open(COL,">$Path/Collection") || die "Erreur de creation de Collection\n";
   while(!eof(F)){
      ## Ce if permet de detecter le debut d'un nouveau document, en regardant la presence de la balise .I
     if($str =~m /\.I\s/){ # On regarde si s$tr contient la chaine .I
        close(NF);
        $str =~s/\.I\s//g; # Dans $str, on supprime la chaine .I avant le numero de document
        $Num=$str;
        print COL "CACM-$Num\n";
        print "Processing ... CACM-$Num\n";
        open(NF,">$Path/CACM-$Num"); ## On cree le fichier CACM-XX
     }
     if(($str=~ m/\.T/) || ($str=~ m/\.A/) || ($str=~ m/\.W/) || ($str=~ m/\.B/)) { # Si $str contient une des balises que l'on veut (.T, .A, .W, .B)
        $Go=1;
        while($Go==1){  # Tant que l'on ne rencontre pas une nouvelle balise
           chop($str=<F>);
           if(($str eq "\.W") || ($str eq "\.B") || ($str eq "\.N") || ($str eq "\.A") || ($str eq "\.X") || ($str eq "\.K") || ($str eq "\.T") || ($str eq "\.I")){
             $Go=0;
             break;
           }
           else{
             print NF "$str "; # On ecrit le contenu dans le fichier CACM-XX
           }
        }
     }
     else{
       chop($str=<F>);
     }
  }
  close(F);


