from typing import Literal

ApiV1SecretmanagerManagersCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_SECRETMANAGER_MANAGERS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_secretmanager_managers_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
