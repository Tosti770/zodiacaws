<head>
	<title>Projecte Zodiac</title>
</head>
<div align="center">

<h1>Projecte ${project}</h1>
<p> Entra el teu aniversari</p>
<form name="form" action="elmeu" method="POST">
	Dia:<input type="text" name="dia" /> <br>
	Mes:<input type="text" name="mes" /> <br>
	<input type="submit" value="Enviar" />
	
</form>
% if signo:
	Ets ${signo} <br><br>
	<img src=${imagen} width="60" height="60" /><br>
	${frase}
% endif
</div>
