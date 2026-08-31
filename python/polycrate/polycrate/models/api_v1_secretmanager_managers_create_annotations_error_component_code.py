from typing import Literal

ApiV1SecretmanagerManagersCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_SECRETMANAGER_MANAGERS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1SecretmanagerManagersCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_secretmanager_managers_create_annotations_error_component_code(
    value: str,
) -> ApiV1SecretmanagerManagersCreateAnnotationsErrorComponentCode:
    if value in API_V1_SECRETMANAGER_MANAGERS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
