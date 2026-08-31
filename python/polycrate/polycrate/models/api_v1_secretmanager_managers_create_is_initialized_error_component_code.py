from typing import Literal

ApiV1SecretmanagerManagersCreateIsInitializedErrorComponentCode = Literal["invalid", "null"]

API_V1_SECRETMANAGER_MANAGERS_CREATE_IS_INITIALIZED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1SecretmanagerManagersCreateIsInitializedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_secretmanager_managers_create_is_initialized_error_component_code(
    value: str,
) -> ApiV1SecretmanagerManagersCreateIsInitializedErrorComponentCode:
    if value in API_V1_SECRETMANAGER_MANAGERS_CREATE_IS_INITIALIZED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_CREATE_IS_INITIALIZED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
