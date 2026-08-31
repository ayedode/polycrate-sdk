from typing import Literal

ApiV1SecretmanagerManagersCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_SECRETMANAGER_MANAGERS_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1SecretmanagerManagersCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_secretmanager_managers_create_tolerations_error_component_code(
    value: str,
) -> ApiV1SecretmanagerManagersCreateTolerationsErrorComponentCode:
    if value in API_V1_SECRETMANAGER_MANAGERS_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
