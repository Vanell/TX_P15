# TX P15

Ensemble formant un post-processeur, pour réaliser des pièces par assemblage avec un robot fanuc.

- Macro catia
- Script python

##Macro Catia

A partir d'un fichier CAO, un assemblage plus particulièrement. Un fichier XML est généré.

####Syntaxe XML
    <PRODUCT>
	    <POSI config_data="N, ,0,0" p="0.0" r="0.0" w="0.0" x="0.0" y="0.0" z="0.0" />
	    <POSI config_data="N, ,0,0" p="0.0" r="37.5" w="180.0" x="2.59" y="-5.14" z="2.5" />
	    <POSI config_data="N, ,0,0" p="0.0" r="142.5" w="0.0" x="9.6" y="-4.22" z="2.5" />
	</PRODUCT>