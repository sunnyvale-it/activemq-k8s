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

python3 queue_receiver.py


for i in {1..100}; do python3 queue_sender.py $i; done

Ref: https://developers.redhat.com/articles/2021/06/30/implementing-apache-activemq-style-broker-meshes-apache-artemis#configuring_the_artemis_broker_mesh



python3 amqp_queue_receiver.py amqp://localhost /queue/test-anycast

python3 amqp_queue_sender.py amqp://localhost /queue/test-anycast hello


for i in {1..10000}; do python3 amqp_queue_sender.py amqp://localhost /queue/test-anycast $i; done



# Prometheus

```console
$ helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
$ helm repo update
$ helm install prometheus-stack prometheus-community/kube-prometheus-stack --values prometheus-stack-values.yaml -n monitoring  --create-namespace
```



kubectl run -ti --rm busybox --image busybox -- /bin/sh