from typing import Literal

ApiV1SecretmanagerManagersCreatePlatformServiceErrorComponentCode = Literal["invalid", "null"]

API_V1_SECRETMANAGER_MANAGERS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1SecretmanagerManagersCreatePlatformServiceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_secretmanager_managers_create_platform_service_error_component_code(
    value: str,
) -> ApiV1SecretmanagerManagersCreatePlatformServiceErrorComponentCode:
    if value in API_V1_SECRETMANAGER_MANAGERS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
