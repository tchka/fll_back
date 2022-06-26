
var api = '/_api_/v1/?';
var plagInterval = null;
var plagCheckPercent = 0;

$(function(){

	$('.block-clients').each(function(){
		var block = $(this);

		block
			.append('<i class="navi prev"></i>')
			.append('<i class="navi next"></i>')
		;

		$('i.navi', block).click(function(){
			var inner = $('.clients-inner', block);

			if ($(this).hasClass('next')) {
				$('.clients-inner', block).animate({'margin-left': '-100%'}, 200, function(){
					for (var i = 0; i < 5; i++) {
						$('div', this).first().appendTo(this);
					}

					$(this).css('margin-left', '0');
				});
			}

			else {
				$(inner).css('margin-left', '-100%');

				for (var i = 0; i < 5; i++) {
					$('div', inner).last().prependTo(inner);
				}

				$('.clients-inner', block).animate({'margin-left': '0'}, 200);
			}

		});
	});

	$('.block-reviews').each(function(){
		var $this = $(this);
		var reviews = $('.reviews-data', this);
		var autoScroll = null;

		var autoScrollFn = function(r){
			var prev = $('i.dot.active', r);

			if (prev.next().length) {
				prev.next().click();
			}
			else {
				$('i.dot', r).first().click();
			}
		};

		$('.review', this).first().addClass('active');

		$('.reviews', this)
			.append('<div class="reviews-navi"></div>')
		;

		for (var j = 0; j < $('.review', this).length; j++) {
			$('.reviews-navi', this).append('<i class="dot"></i>');
		}

		$('.reviews-navi i.dot', this).first().addClass('active');

		$('.reviews-navi i.dot', this).click(function(){
			$(this).parent().find('.active').removeClass('active');
			$(this).addClass('active');

			var n = $(this).index();

			$('.review.active', reviews).removeClass('active');
			$('.review', reviews).eq(n).addClass('active');

			clearTimeout(autoScroll);
			autoScroll = setTimeout(autoScrollFn, 5000, $this);
		});

		autoScroll = setTimeout(autoScrollFn, 5000, $this);
	});

	$('.text-check').each(function(){
		var form = $(this);
		var text = $('textarea', this);

		text.keyup(function(){
			var total = text.val().length;
			var symbols = text.val().replace(/\s/g, '').length;

			var words_total = 0;
			var words = text.val().split(/\s/g);

			for (var i = 0; i < words.length; i++) {
				var w = words[i];

				if (w.length > 0) {
					words_total++;
				}
			}

			$('#textCheckTotal').html(total);
			$('#textCheckSymbol').html(symbols);
			$('#textCheckWord').html(words_total);
		});

		$('button.jSubmit', form).click(function(){
			var button = $(this);

			$.post(api + 'action=plag.submit', {text: text.val()}, function(r){
				$('.error', form).remove();

				if (r.status) {
					if (r.data.result) {
						if (r.data.id) {
							$('.buttons', form).before('<div class="status">Текст отправлен. Ожидайте результат...</div>');
							plagInterval = setInterval(plagCheckResult, 3000, r.data.id, form);
							button.replaceWith('<i class="wait"></i>');
						}
						else {
							$('.buttons', form).before('<div class="error">Ошибка. Попробуйте ещё раз.</div>');
						}
					}
					else {
						$('.buttons', form).before('<div class="error">Ошибка. Попробуйте ещё раз.</div>');
					}
				}
				else {
					$('.buttons', form).before('<div class="error">Ошибка. Попробуйте ещё раз.</div>');
				}
			}, 'json');
		});
	});

});

var plagCheckResult = function(id, form) {
	$.get(api, {
		'action': 'plag.status',
		'id': id,
	}, function(r){
		$('.error', form).remove();

		if (r.status) {
			if (r.data.result) {
				if (r.data.status == 4) {
					$('.status', form).remove();

					if (r.data.compare) {
						$('textarea', form).replaceWith('<div class="marked-text">' + r.data.marked_text + '</div>' +
							'<div class="info"><span>Уникальность: ' + r.data.percent + '%</span> ' +
							'<span>' + r.data.url + '</span></div>');

						$('.buttons', form).before('<div class="error">Найдены дубликаты</div>');
					}
					else {
						if (r.data.marked_text) {
							$('textarea', form).replaceWith('<div class="marked-text">' + r.data.marked_text + '</div>');

							$('.buttons', form).before('<div class="done">В тексте отмечены найденные фрагменты</div>');
						}
						else {
							$('.buttons', form).before('<div class="done">Текст уникальный</div>');
						}
					}

					$('.wait', form).remove();

					clearInterval(plagInterval);
				}
				else if (r.data.status == 3) {
					plagCheckPercent += (plagCheckPercent < 50) ? 7 : ((plagCheckPercent < 90) ? 3 : 1);

					if (plagCheckPercent > 99) {
						plagCheckPercent = 99;
					}

					$('.status', form).html('Обработка результатов ' + plagCheckPercent + '%...');
				}
				else if (r.data.status == 2) {
					plagCheckPercent = 0;
					$('.status', form).html('Поиск совпадений...');
				}
			}
			else {
				$('.buttons', form).before('<div class="error">Ошибка. Попробуйте ещё раз.</div>');
			}
		}
		else {
			$('.buttons', form).before('<div class="error">Ошибка. Попробуйте ещё раз.</div>');
		}
	}, 'json');
}
