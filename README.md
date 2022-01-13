# activemq-k8s

```console
$ docker buildx create --name mybuilder
$ docker buildx use mybuilder
$ docker buildx inspect --bootstrap

$ docker login
$ export ACTIVEMQ_ARTEMIS_VERSION=2.16.0
$ docker buildx build --build-arg ACTIVEMQ_ARTEMIS_VERSION=$ACTIVEMQ_ARTEMIS_VERSION -f ./docker/Dockerfile.artemis -t sunnyvaleit/activemq-artemis:$ACTIVEMQ_ARTEMIS_VERSION  --push ./docker 
$ kubectl apply -f . 
```









