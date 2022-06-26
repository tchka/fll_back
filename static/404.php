<!doctype html>
<html lang="ru">
<head>
	<title>Страница не найдена</title>

	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">

	<link href="https://fonts.googleapis.com/css?family=Open+Sans:300,400,700&display=swap&subset=cyrillic" rel="stylesheet">

	<link rel="stylesheet" href="/files/design19/css/reset.css">
	<link rel="stylesheet" href="/files/design19/css/style.css">

	<script src="/files/design19/js/jquery-3.2.1.min.js"></script>
	<script src="/files/design19/js/app.js"></script>
</head>

<body>

	<header>
		<div class="wrapper">
			<div class="row">
				<div class="col contacts">
				</div>
				<div class="col">
					<a href="/" class="logo"></a>
				</div>
				<div class="col user">
				</div>
			</div>
		</div>
	</header>

	<div class="banner">
		<div class="data">
			<div class="txt1">Ошибка <?= $code ?></div>
			<div class="txt2">Страница не найдена</div>
			<div class="txt3">
				Страница, которую Вы ищите, не найдена. Попробуйте начать <a href="/">с главной страницы</a>.<br />
				Так же вы можете <a href="/contacts">написать нам</a> о найденной ошибке <a href="/contacts">в разделе контакты</a>.<br />
				Попробуйте найти нужную информацию в <a href="/faq">разделе FAQ</a>.
			</div>
			<div class="txt4">
				<a href="/" class="btn">На главную</a>
			</div>
		</div>
	</div>

</body>
</html>
