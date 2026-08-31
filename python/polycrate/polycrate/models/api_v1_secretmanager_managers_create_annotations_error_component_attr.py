from typing import Literal

ApiV1SecretmanagerManagersCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_SECRETMANAGER_MANAGERS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_secretmanager_managers_create_annotations_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersCreateAnnotationsErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
