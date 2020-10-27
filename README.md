# foodPriceScraper
## EspaÃ±ol

Extrea datos estadísticos de jugadores de distintas ligas profesionales de balonesto

Para ejecutar el script es necesario instalar la siguientes bibliotecas:
```

pip install beautifulsoup4
```

El script se debe ejecutar de la siguiente manera:
```
python main.py --startSeason 2019 --endSeason 2020 --league acb
```

Donde **startSeason** es la temporada de inicio y **endSeason** es la temporada de fin de las que se van a extraer los datos. Los registros se almacenan en un archivo de tipo CSV, 
con el nombre "players_[league]_[startSeason]_[endSeason].csvç2

El csv tiene los siguientes campos:


*'league': Liga de la que se extraen los datos
*'game_date': Fecha en la que se jugó el partido,
*'local_team': Nombre del equipo local
*'local_team_points': Puntos del equipo local
*'visit_team': Nombre del equipo visitante
*'visit_team_points': Puntos del equipo visitante
*'player_team': Indica si el juegador jugaba en el equipo local o visitante
*'player_name': Nombre del jugador
*'player_total_points': Total de puntos del jugador
*'time': Minutos y segundos jugados en el formato mm:ss
*'one_point_shots_get': Tiros de un punto conseguidos
*'one_point_shots_made': Tiros de un punto realizados
*'two_point_shots_get': Tiros de dos puntos conseguidos
*'two_point_shots_made': Tiros de dos puntos realizados
*'three_point_shots_get': Tiros de tres puntos conseguidos
*'three_point_shots_made': Tiros de tres puntos realizados
*'rebouts': Rebotes capturados
*'assists': Asistencias repartidas
*'faults': Faltas cometidas
*'received_faults': Faltas recibidas

## English

...
