from typing import Literal

ApiV1ProvidersUpdateActiveErrorComponentCode = Literal["invalid", "null"]

API_V1_PROVIDERS_UPDATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ProvidersUpdateActiveErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1_providers_update_active_error_component_code(
    value: str,
) -> ApiV1ProvidersUpdateActiveErrorComponentCode:
    if value in API_V1_PROVIDERS_UPDATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_UPDATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
