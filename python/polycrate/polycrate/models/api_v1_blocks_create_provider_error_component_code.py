from typing import Literal

ApiV1BlocksCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_BLOCKS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[ApiV1BlocksCreateProviderErrorComponentCode] = {
    "invalid_choice",
    "null",
}


def check_api_v1_blocks_create_provider_error_component_code(value: str) -> ApiV1BlocksCreateProviderErrorComponentCode:
    if value in API_V1_BLOCKS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
