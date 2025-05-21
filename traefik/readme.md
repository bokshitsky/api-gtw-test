Выглядит как весьма годная штука.


Конфиг делитя на 2 части: статический и динамический
Поддерживает configuration discovery
https://doc.traefik.io/traefik/providers/overview/

consulCatalog - регает сервисы из консула в трафик
consul - позволяет сам конфиг traefik-а хранить в консуле

Чтобы забрал сервис из консула должна быть метка "traefik.enable=true" в консуле. (либо флаг "забирать всё")

плагины можно писать:
1) go-плагины интерпретируются через https://github.com/traefik/yaegi
2) http-wasm хз как работают

forwardAuth не позволяет сослаться на service, только на DNS имя 


запускать
```
docker run --rm -p 8080:8080 -p 8081:8081 -v $PWD/traefik.yml:/etc/traefik/traefik.yml -v $PWD/dyncofigs:/etc/traefik/dyncofigs traefik
```

https://doc.traefik.io/traefik/middlewares/http/forwardauth/

```
curl -H 'Host: hhapi' '127.0.0.1:8080/status'
```


