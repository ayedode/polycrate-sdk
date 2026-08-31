from typing import Literal

ApiV1PopsUpdateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_POPS_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PopsUpdateProviderErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pops_update_provider_error_component_code(value: str) -> ApiV1PopsUpdateProviderErrorComponentCode:
    if value in API_V1_POPS_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
