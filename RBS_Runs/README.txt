Na câmara de RBS do acelerador Van de Graaff contamos com 3 detetores (idênticos), dispostos
como mostra na figura "camara.jpg" (cuidado com os ângulos!). Eles são nomeados "ERD" "RBS1" e "RBS2".
Em cada medição adquirimos dados dos três detertores sendo que estes ficam identificados
no início do nome do ficheiro. Estes são os ficheiros ".dat" que têm um formato um pouco estranho.
O que nos interessa são os valores que se encontram em 128 linhas * 8 colunas = 1024 canais.
O código "camdat2dat.py" cria um novo ficheiro com o formato ASCii que o SIMNRA gosta.


Um índice, mais ou menos resumido, do que podes encontrar em cada medição

2022_02Set_CaF2+Formvar&CaF2+C:
Feixe de alfas, 1500 keV;
Alvos: Au, Pb, C, CaF2 em substrato de formvar e CaF2 em substrato de carbono;


2022_07Set_Au&Pb&C:
Feixe de alfas, 2000 keV;
Calibrações com dois alvos: V:Nb:Ta em substrato de Si (contém oxigénio) e Yb:Ge:O em substrato de Si;
Alvos analisados de Au ~ 150 nm


2022_23Nov_Pb:
Os mesmo alvos de Pb foram analisados com alfas e protões de 2000 keV;


2022_29Ago_Formvar:
Feixe alfas 1500 keV;
Alvos: formvar diferentes espessuras;


2023_21Jan_Pb:
Feixe: protões 2000 keV;
Alvos: Pb evaporado em substrato de formvar que foi depois removido por dissolução em clorofórmio;
alvos com diferentes concentrações de formavar e alguns standalone;
Filme de formavar para referência;


2023_21Mar_Pb:
Feixe: protões 2000 keV;
Alvos: Pb Pb evaporado em substrato de formvar, depois de removido o último (alguns contém contaminação);
Calibração com Ta:Nb:V


2023_24Abr_Sn+Al:
Feixe: protões 2000 keV;
Alvos: Sn + Al (um dos alvos é apenas Sn)
Calib. Ta:Nb:V