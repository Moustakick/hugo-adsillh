# Etude de cas
## Question 1

La société *ToutPetitLogiciel* a raison sur le fait que si ils intègrent le code objet de Mlle Lechamp à leur programme, le code binaire résultant serait une œuvre dérivée de la bibliothèque. Hors contrairement aux contraintes imposées par la GPL classique qu'ils semblent avoir comprise, qui dit que toute œuvre dérivée d'un programme sous cette licence doit disposer des mêmes droits, la LGPLv2.1 (ou licence publique générale GNU **amoindrie** version 2.1) permets une intégration plus permissive, comme le dit le texte en anglais ci-dessous :

> When a program is linked with a library, whether statically or using a shared library, the combination of the two is legally speaking a combined work, a derivative of the original library. The ordinary General Public License therefore permits such linking only if the entire combination fits its criteria of freedom. The Lesser General Public License permits more lax criteria for linking other code with the library.

Ceci signifie que tout œuvre dérivée d'une œuvre possédant une licence LGPLv2.1 peut conserver sa licence, la seule obligation avec cette licence est de rediffuser le code source du logiciel sous licence LGPLv2.1 quand celui-ci est modifié : "Ce qui était libre le reste".

Par conséquent Mlle Lechamp peut leur répondre qu'il y a eu une erreur de compréhension sur la licence de la bibliothèque à intégrer et que s'il y a intégration de celle-ci dans le logiciel, cela ne remettra pas en cause la licence privative sous laquelle se trouve l'original.

\newpage
## Question 2

Un greffon est toujours couvert par le mode d'action d'une licence libre, dans notre cas, sous licence LGPLv2.1 la licence va avoir le même impact et cette solution, juridiquement, ne diffère pas de la précédente.
Pour le cas de l'assemblage de deux bibliothèques la licence LGPLv2.1 indique la chose suivante :

> As an exception to the Sections above, you may also combine or link a "work that uses the Library" with the Library to produce a work containing portions of the Library, and distribute that work under terms of your choice, provided that the terms permit modification of the work for the customer's own use and reverse engineering for debugging such modifications.

Dans notre cas si on assemble deux bibliothèques, une sous licence LGPLv2 et une sous licence privative, cela est autorisé et la personne qui créer la modification peut définir les termes de son choix pour la distribution. La seule contrainte est la suivante :

> You must give prominent notice with each copy of the work that the Library is used in it and that the Library and its use are covered by this License. You must supply a copy of this License. If the work during execution displays copyright notices, you must include the copyright notice for the Library among them, as well as a reference directing the user to the copy of this License. [...] (voir partie 6 de TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION)

Concrètement les seules restrictions sont une notice de l'utilisation de la bibliothèque, de fournir une copie de la licence. Donc la fusion des bibliothèques est possible dans le cas où la licence de la seconde bibliothèque n'empêche pas l'exercice des droits de la LGPLv2.1.

\newpage
## Question 3

L'œuvre a été rééditée dans son intégralité en 1954, soit pendant que le pays est sous l'influence de la Convention de Berne sur la protection des œuvres littéraires
et artistiques. D'après cette [source](https://www.wipo.int/treaties/fr/ip/berne/summary_berne.html) la convention indique que tant que l'œuvre possède pour origine un des Etats contractants à la convention, celle-ci dispose de la protection. Même si cette œuvre a été éditée pendant une période où l'État n'était pas contractant de cette convention, le texte indique aussi que la protection est indépendante de l'existence de la protection dans le pays d'origine, c'est-à-dire que la protection est désormais appliquée, particulièrement dans le cas d'une réédition après la mort de l'auteur.

Cette protection fournit plusieurs droits exclusifs relatifs l'œuvre, notamment quelqu'une qui nous intéressent dans notre cas (voir [source](https://www.wipo.int/treaties/fr/ip/berne/summary_berne.html)) :

+ le droit de faire des adaptations et des arrangements de l'œuvre
+ le droit de faire des reproductions
+ le droit d'utiliser une œuvre comme point de départ d'une œuvre audiovisuelle

Avec les doits fournis ci-dessus, nous pouvons estimer que Mlle Lechamp n'est pas dans son tort de réutiliser la table des accords syldaves réguliers et irréguliers extraite du livre "Jof djn gljt Djusz djn Syldavskj Tzjakorr" et a par conséquent raison de le faire.

<!-- Vérifier ses dires-là je suis fatigué -->

\newpage
## Question 4

Elle devrait lui répondre de vérifier d'abord les dispositions légales quant à la réutilisation des données disponibles sur le dictionnaire en ligne djn-roburt.sy.\newline
S'il s'agit simplement des accords réguliers et irréguliers d'un langage cela fait partie du domaine des idées et n'est par conséquent pas une œuvre. Un langage n'est pas une œuvre.
Cependant les outils liés à un langage appartiennent à quelqu'un, peuvent être considérés comme des œuvres et par conséquent disposer d'une protection légale dans ce cas un script qui récupérerait ces données serait un acte de vol.

Pour moi la meilleure solution serait de demander directement au propriétaire du dictionnaire une autorisation de réutilisation.

\newpage
## Question 5

Une des solutions serait de leur dire d'utiliser le logiciel sous licence LGPLv2.1 et de créditer l'auteur pour son travail. Ainsi ils profiteraient de toute la communauté pour le développement du logiciel et pourraient aussi y participer.

Sinon elle peut choisir l'alternative du multi-licenciage, d'éditer son logiciel en mode "Double Licence". Solution choisie par beaucoup d'éditeurs, comme Visual Paradigm. Même si la version open source du logiciel n'est pas une licence à copyleft fort (comme la GPLv3) ce qui est souvent le cas dans le multi-licenciage. Cela permettrait de faire payer pour une version v2 du logiciel, à l'entreprise, sous une autre licence à copyleft faible du type BSD comme ils le demandaient. Cependant ça ne permettra pas à l'acheteur d'obtenir le support de la communauté mais au moins le logiciel conservera son intégrité open-source originale.


\newpage
## Question 6

Au préalable elle doit prendre un compte les champs d'application. Le site web avec la création de comptes et le traitement de texte rentre dans le champ d'application matériel de l'automatisation dont nous fait part l'article 2.1. Pour ce qui est du champ d'application territorial l'article 3.1 englobe les centres d'activités des établissements sur le territoire de l'Union, ce qui est le cas dans la présente. Ces conditions réunies, elle est légitime à l'application de la RGPD pour l'utilisation des données à caractère personnel dans le contexte d'activité de son site web.

Elle devrait prendre conscience des informations quant au traitement des données à caractère personnel, transcrites dans l'Article 5. Elle va principalement devoir définir une finalité par rapport au stockage et à l'utilisation des données, dans son cas par exemple, il peut s'agir de dire qu'elle stock les adresses mail des comptes pour un usage informatif comme les newsletters ou pour envoyer les textes après traduction.\newline
Les autres parties de l'Article 5 parlent de notions importantes. Elle va devoir être transparente quant au stockage des données. Elle va devoir faire en sorte de conserver des données au maximum à jour, cela concerne dans son cas surtout les données relatives à la personne directement comme le nom ou le prénom par exemple. Les données permettant l'identification d'une personne ne doivent pas être conservées plus longtemps que le temps nécessaire au regard des finalités. Et finalement, elle va devoir mettre en place une sécurité appropriée par rapport au vol, à l'utilisation illicite ou à la dégradation de ces données.

Ensuite elle va devoir à l'inscription ou lors de changements des finalités établir un accord consenti entre elle et l'utilisateur du site web, qui indique concrètement quelles données vont être stockées et quelle utilisation va être faite de ces données (finalités). Dans son cas cela peut-être fait par exemple dans un texte suivi d'un "j'ai lu et j'accepte les conditions d'utilisation".\newline
Selon l'article 7, il est indiqué qu'elle devra être capable de démontrer que la personne a donné son consentement au traitement de ces données à caractère personnel.

Finalement en plus d'être totalement transparent quant à la communication et les modalités de l'exercice des droits d'une personne concernée, comme indiquées dans l'article 12. Étant responsable du traitement des données à caractère personnel elle devra donner différentes informations lui concernant comme indiquer dans l'article 13.

\newpage
## Question 7

Selon les parties 1.b et 1.c de l'article 5 du RGPD, constituer une telle base serait légitime dans le cadre où l'exploitation de ces données à caractère personnel ont des finalités explicites et légitimes, et ne sont pas traitées ultérieurement d'une manière incompatible avec ces finalités. De plus il faut que ces données soient 	
adéquates, pertinentes et limitées à ce qui est nécessaire au regard des finalités pour lesquelles elles sont traitées.

Dans le cas de Mlle Lechamp, la finalité de l'exploitation de ces données à caractère personnel est déjà déterminée : elle veut pouvoir les utiliser pour tester des améliorations successives de son logiciel. Le tout ensuite est de trouver une manière adéquate de les stocker, comme par exemple anonymement car dans le contexte de cette finalité l'identification d'une personne ne sert à rien. Et finalement il faut faire en sorte que ces données ne soient pas conserver, et utiliser en dehors de ces finalités.

Finalement la dernière chose qu'elle aurait à faire c'est d'établir une communication avec l'utilisateur pour que, conformément à l'article 6 et 7, il accepte les termes d'utilisation de ces données dans le cadre de cette finalité.

En conclusion, elle dispose du droit de constituer une telle base de données mais pour cela il va falloir qu'elle revoie les finalités d'emploi des données et ce que cela engage. De plus l'utilisateur devra donner son consentement pour cette nouvelle utilisation de ces données qui va être faite.
