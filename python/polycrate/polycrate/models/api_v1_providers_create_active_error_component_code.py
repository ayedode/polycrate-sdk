from typing import Literal

ApiV1ProvidersCreateActiveErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDERS_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ProvidersCreateActiveErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_providers_create_active_error_component_code(
    value: str,
) -> ApiV1ProvidersCreateActiveErrorComponentCode:
    if value in API_V1_PROVIDERS_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
