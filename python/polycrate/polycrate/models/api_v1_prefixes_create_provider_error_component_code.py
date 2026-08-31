from typing import Literal

ApiV1PrefixesCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PREFIXES_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PrefixesCreateProviderErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_prefixes_create_provider_error_component_code(
    value: str,
) -> ApiV1PrefixesCreateProviderErrorComponentCode:
    if value in API_V1_PREFIXES_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PREFIXES_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
