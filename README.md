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





2022-01-13 22:02:58,469 WARNING [org.jgroups.protocols.kubernetes.KUBE_PING] Problem getting Pod json from Kubernetes Client[masterUrl=https://10.96.0.1:443/api/v1, headers={}, connectTimeout=5000, readTimeout=30000, operationAttempts=3, operationSleep=1000, streamProvider=org.openshift.ping.common.stream.TokenStreamProvider@63da207f] for cluster [active_broadcast_channel], namespace [default], labels [app=activemq-artemis]; encountered [java.lang.Exception: 3 attempt(s) with a 1000ms sleep to execute [OpenStream] failed. Last failure was [java.io.IOException: Server returned HTTP response code: 403 for URL: https://10.96.0.1:443/api/v1/namespaces/default/pods?labelSelector=app%3Dactivemq-artemis]]




2022-01-13 22:03:07,807 WARN  [org.apache.activemq.artemis.core.protocol.stomp] AMQ332069: Sent ERROR frame to STOMP client /192.168.65.3:58522: AMQ229014: Did not receive data from /192.168.65.3:58522 within the 60,000ms connection TTL. The connection will now be closed.
2022-01-13 22:03:07,807 WARN  [org.apache.activemq.artemis.core.server] AMQ222067: Connection failure has been detected: AMQ229014: Did not receive data from /192.168.65.3:58522 within the 60,000ms connection TTL. The connection will now be closed. [code=CONNECTION_TIMEDOUT]





