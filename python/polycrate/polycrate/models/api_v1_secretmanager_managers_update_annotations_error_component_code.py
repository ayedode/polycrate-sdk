from typing import Literal

ApiV1SecretmanagerManagersUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_SECRETMANAGER_MANAGERS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1SecretmanagerManagersUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_secretmanager_managers_update_annotations_error_component_code(
    value: str,
) -> ApiV1SecretmanagerManagersUpdateAnnotationsErrorComponentCode:
    if value in API_V1_SECRETMANAGER_MANAGERS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
