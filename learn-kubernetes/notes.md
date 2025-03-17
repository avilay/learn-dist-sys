## K8 Objects
K8 objects are a higher level abstraction of resources that represent my stuff running in the cluster. Every K8 object includes two nested object fields - **spec** and **status**. **spec** defines the goal (or desired) state of the object, **status** is its current state. At any point, K8 master is actively trying to drive the object from its actual state to its goal state. An object is defined in a yaml file that needs - at the very minimum - the following fields:

  * `apiVersion`: The K8 version in use.
  * `kind`: The kind of object, whether it is a Pod or a Deployment or some other kind of object.
  * `metadata`: Must include a `name` but can have other metadata info as well like `label`s and `annotation`s.
  * `spec`: The goal state of the object.

## Kubernetes Object Management
https://kubernetes.io/docs/concepts/overview/object-management-kubectl/overview/
Use **declarative object configuration** so that the K8 master can drive my resources (K8 objects) to their goal state without me having to specify individual operations. From the documentation -
>When using declarative object configuration, a user operates on object configuration files stored locally, however the user does not define the operations to be taken on the files. Create, update, and delete operations are automatically detected per-object by kubectl. This enables working on directories, where different operations might be needed for different objects.

Process all object configuration in files in the `configs` directory.
```
$ kubectl apply -f configs/
```

Recursively process directories:
```
$ kubectl apply -R -f configs/
```

To apply a single file
```
$ kubectl apply -f <filename>
```

However, the declarative approach to updates will only work when I want to change the image or tolerations. Not sure if it will work when I want to change the scaling. But, e.g., if I want to add ports to my container spec, it will not work. The only way I can think of is to delete the Pod and then re-create it with the new config.

To delete a Pod use the pod-name specified in the Pod's yaml.
```
$ kubectl delete pod <pod-name>
```

To get both the spec and status of a specific object defined in `my-object.yaml`
```
$ kubectl get -f my-object.yaml -o yaml
```

## Metadata
### Names and Namespaces
Each K8 object has to have a unique name. Namnespaces provide a way to partition names s.t names within a namespace need to be unique but across namespaces do not need to be unique.

### Labels
Key-value pairs inside the `metadata` that serves to provide some sort of identifying information about the K8 object. These do not need to be unique. These are used to select objects or find collections of related objects.

### Annotations
Key-value pairs inside the `metadata` that serves to provide a way to set structured data for the K8 objects to use. This can be build information like git tags, logging/monitoring endpoints, lightweight config, human owner information, etc.

## Pods
The simplest `kind` of K8 object is a `Pod` which is usually a single Docker container, e.g., `nginx-simple-pod.yaml`. A Pod can have volumes mounted on it.

