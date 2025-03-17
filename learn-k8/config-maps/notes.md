# Configmaps
Configmaps can be created from files or from literals. They can be loaded into the pod as environment variables or mounted on a file path. A configmap is a K8 object, and like all K8 objects it has a name. Its "spec" is essentially a bunch of key/value pairs. While the key is usually a small string, typically a single word, the corresponding value can be arbitrarily long.

## Creating Configmaps
### From files
If I already have a directory with a bunch of files all of which need to go into the configmap I can use the following imperative command to create the configmap. This command works with both a directory and with a file. The generated configmap will have the filename(s) as the key(s) and the entire contents of the file as the corresponding value(s). They key names can be configured to be something else than the filename if needed (not shown in the examples below).
```
kubectl create configmap game-config --from-file=./confs/properties/
kubectl create configmap app-config --from-file=./confs/inis/app.ini
```

```
$ kubectl describe configmap game-config
Name:         game-config
Namespace:    learn-k8
Labels:       <none>
Annotations:  <none>

Data
====
game.properties:
----
enemies=aliens
lives=3
enemies.cheat=true
enemies.cheat.level=noGoodRotten
secret.code.passphrase=UUDDLRLRBABAS
secret.code.allowed=true
secret.code.lives=30
ui.properties:
----
color.good=purple
color.bad=yellow
allow.textmode=true
how.nice.to.look=fairlyNice
```

### From ENV files
If instead of having the entire contents of the file as the value, if I want K8 to be a bit "smart" about the interpreting the contents and make each name=prop entry in the file as a top level key=value for my configmap, I can use `--from-env-file` instead of `--from-file`.
```
kubectl create configmap gamevars --from-env-file=./confs/game.env
```

Now instead of the key being "game.env" and the value being the entire contents of this file, the keys and values are more "sensible".
```
$ kubectl describe configmap gamevars
Name:         gamevars
Namespace:    learn-k8
Labels:       <none>
Annotations:  <none>

Data
====
allowed:
----
"true"
enemies:
----
aliens
lives:
----
3
```

### From YAML files
I can also use my usual declarative way of creating config maps by creating a YAML file with a configmap kind, e.g., cm.yaml and then apply this file as usual.
```
kubectl apply -f cm.yaml
```
The imperative counterpart to this is to use the `--from-literal` flag.

## Using Configmaps
### Environment Variables
I can create environment variables in my pod spec and map each variable name to the value of a key from some configmap.

I can also use the entire configmap as my environment variables without having to map individual env names. Details [here](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/#configure-all-key-value-pairs-in-a-configmap-as-container-environment-variables)

These environment variables can be used to parameterize the pod container commands. Details [here](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/#use-configmap-defined-environment-variables-in-pod-commands).

### As Volume mounts
When I have created a configmap from a file, it would make sense to make that config file available to the Pod. For this scenario I can use Volume mounts. As I would expect, each key in the config map will show up as a file in the mounted volume and the value of that key will be the contents of the file.