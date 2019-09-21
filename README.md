# Кориснички Интерфејси Проект

## 60. Веб Апликација за Новости

<hr>

<h1>1TV</h1>

---

### Содржина

   * [Краток опис на страната](#Краток-опис-на-страната)
   * [Делови од кодот](#Делови-од-кодот)
   * [Користени Библиотеки](#Користени-библиотеки)
   * [Изработиле](#Изработиле)

<hr>
<br>


### Краток опис на страната

Веб страница за новости каде што се објавуваат најновите новости во врска со Македонија, Светот, Политиката, Спортот и Игрите.
Почетната (Home) страница се издвојуваат три најнови и најпосетувани новости од сите области. Постојат страници за секоја од горе наведените области каде се објавени новостите, на секоа од страните може да се прикажат 5 новости а доколку има повеќе поделени се во посебни страни каде што може да се вртат со помош на javascript и jQuery. Во областа на Games постојат страница за новости, за Live Stream и страница за игри каде има неколку игри за играње. Постои страна Аbout и Contact каде што има оставено број за контакт, адреса и со внесување на име, презиме, маил и порака може да не исконтактираат.

<hr>

### Делови од кодот

* Страната функционира со помош на Flask каде при внесување на некоја акција не пренесува на акцијата што сакаме да ја извршиме.

Дел од кодот

```
	from flask import Flask
	from flask import render_template

	@app = Flask(__name__)


	@app.route('/')
		def index():
    		return render_template("index.html")


	@app.route('/Home')
		def home():
    		return render_template("index.html")


	@app.route('/MacedonianNews')
		def macedonian_news():
    		return render_template("pages/MacedonianNews.html")

    ##Истиот пример се однесува со останатите страни

    @app.route('/WorldNews/<page>')
		def world_news_pages(page):
   			return render_template("pages/WorldNews/" + page + ".html")

   	##Истиот пример се однесува и со останатите страни


```

* Страниците се full-responsive со помош на bootstrap 4 и неговите опции како :
```
	col-sm-[1-12]	p-sm-[1-5]	m-sm-[1-5]
	col-md-[1-12]	p-md-[1-5]	m-md-[1-5]
	col-lg-[1-12]	p-lg-[1-5]	m-lg-[1-5]
```

исто така и голема помош имаше и
```
	@media only screen and (max-width: <width>) {
            iframe{
                width: 100%;
                height: 100%;
            }

        }
```

* Исто така за страната да изгледа подобро и подбри функции користевме и јаваскрипт.

Дел од кодот за вртење на страниците за новости:
```
<script type="text/javascript" >

    $(document).ready(function () {

        $('.page-1').show();
        $('.page-2').hide();


        $('#first-page').click(function () {

            $('.page-1').show();
            $('.page-2').hide();
            $('#previous').disable;
            $('#next').enable;

        });

        $('#second-page').click(function () {
            $('.page-2').show();
            $('.page-1').hide();
            $('#next').disable;
            $('#previous').enable;


        });

        $('#previous').click(function () {
            if ($('.page-1').is(':hidden')){
                $('.page-1').show();
                $('.page-2').hide();
                $('#previous').disable;
                $('#next').enable;

            }
        });

        $('#next').click(function () {
            console.log($('.page-2').hidden);
            if ($('.page-2').is(':hidden')){
                $('.page-2').show();
                $('.page-1').hide();
                $('#previous').enable;
                $('#next').disable;

            }
        });
    });

</script>

```


### Користени Библиотеки

1. http://courses.finki.ukim.mk
2. https://getbootstrap.com/docs/4.1/getting-started/introduction/
3. https://www.w3schools.com/


### Изработиле:
1. Кирил Ристов (173217)
2. Давид Петков (173206)
