from typing import Literal

ApiV1SecretmanagerManagersCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_SECRETMANAGER_MANAGERS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1SecretmanagerManagersCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_secretmanager_managers_create_kind_error_component_code(
    value: str,
) -> ApiV1SecretmanagerManagersCreateKindErrorComponentCode:
    if value in API_V1_SECRETMANAGER_MANAGERS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
