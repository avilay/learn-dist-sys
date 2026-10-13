# Pydantic Summary

* Use `BaseModel` as the super class.
* Model creation, serialization, and validation using -
  * Simple ctor with kwargs
  * `model_validate()`
  * `model_validate_json()`
  * `model_validate_strings()`
* No validation is performed after the object has been initialized.
* Model deserialization using -
  * `model_dump()`
  * `model_dump_json([indent=n])`
  * `model_json_schema()`
* Can use [custom types](https://docs.pydantic.dev/latest/api/types/#pydantic.types) as field types which give a bunch of validation and ser/der capabilities OOB.
* Can use any Python stdlib type or another `BaseModel` type as a field type.
* Generic models work pretty much like standard generic Python types.
* Customize default model behavior by -
  * Set model level constraints via [`ConfigDict`](https://docs.pydantic.dev/latest/api/config/) by adding a `model_config=ConfigDict(...)` attribute to the model.
  * Set field level constraints by initializing the field with [`Field`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field)
  * Set per instance constraints by passing appropriate params to `model_validate` family of functions including `(config=ConfigDict(...))`.
* Default model behavior which can be changed by adding constraints -
  * Loss-less data conversion upon initialization.
  * Mutable objects.
  * Extra attrs are silently ignored upon initialization.
* Copy model objects using `model_copy([deep=True|False])` method.
* Customize serialization with `@model_serializer()` and `@field_serializer()`.
* Can support both camel case and snake case with aliasing.
* Customize validation by using `@field_validator()` or `@model_validator()` which can be run before object initialization, after object initialization, or can wrap the default validation that is performed during initialization.

