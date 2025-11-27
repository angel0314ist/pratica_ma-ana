# Proyecto Flask con Traefik, Docker Swarm y CI/CD (GitHub Actions)

Este proyecto muestra cómo desplegar una aplicación Flask detrás de Traefik, funcionando como proxy inverso y balanceador de carga dinámico, utilizando Docker Swarm como orquestador y un pipeline automatizado con GitHub Actions para construir, publicar y desplegar el servicio en un servidor remoto.

## ¿Qué hace este proyecto?
- Expone una aplicación Flask simple (app.py).
- Empaqueta la aplicación como imagen Docker.
- Publica automáticamente la imagen en GitHub Container Registry (GHCR).
- Copia y despliega un stack Docker Swarm en un servidor VPS.
- Utiliza Traefik para enrutar tráfico por dominio, redirigir HTTP → HTTPS y generar certificados SSL automáticamente.

## 1Arquitectura General
Arquitectura básica: Usuario → Traefik (proxy inverso + SSL) → Servicio Flask.  
Traefik detecta automáticamente el servicio usando labels del archivo stack.yml.

## 2¿Cómo funciona Traefik en este proyecto?
Traefik actúa como proxy inverso mediante la regla: traefik.http.routers.angel.rule=Host('angel.byronrm.com').  
Maneja certificados SSL con: traefik.http.routers.angel-secure.tls=true y certresolver.  
Cuando el servicio se despliega, Traefik lo detecta automáticamente y enruta el tráfico. También puede balancear carga si el servicio tiene varias réplicas.

## 3Integración con Docker Swarm
El archivo stack.yml define la imagen Docker, las labels de Traefik, la red traefik-public y el puerto interno del servicio. Ejemplo de labels: traefik.enable=true, traefik.http.routers.angel.rule=Host('angel.byronrm.com'), traefik.http.services.angel.loadbalancer.server.port=80.

## 4Pipeline CI/CD con GitHub Actions
El archivo .github/workflows/build.yml realiza:  
1. Build de la aplicación Flask  
2. Construcción de la imagen Docker  
3. Push a GitHub Container Registry  
4. Conexión SSH al servidor  
5. Copia del stack.yml  
6. Despliegue automático con: docker stack deploy -c stack.yml --with-registry-auth angel  
Cualquier cambio enviado a main despliega una nueva versión sin intervención manual.

## 5Estructura del Proyecto
- app.py → Aplicación Flask  
- dockerfile → Imagen Docker  
- requirements.txt → Dependencias  
- stack.yml → Configuración del stack Docker Swarm  
- makefile → Comandos útiles  
- .github/workflows/ → Pipeline CI/CD  

## 6Ejecución local
Build: make build  
Ejecución con Docker: docker run -p 80:80 angel  

## 7Despliegue manual (opcional)
docker stack deploy -c stack.yml --with-registry-auth angel

## Resultado final
Tu aplicación Flask queda disponible en: https://angel.byronrm.com  
Con HTTPS automático, servicio desplegado en Docker Swarm y CI/CD funcionando sin intervención manual.
