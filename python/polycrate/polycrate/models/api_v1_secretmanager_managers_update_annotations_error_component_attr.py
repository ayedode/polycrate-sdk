from typing import Literal

ApiV1SecretmanagerManagersUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_SECRETMANAGER_MANAGERS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_secretmanager_managers_update_annotations_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersUpdateAnnotationsErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
