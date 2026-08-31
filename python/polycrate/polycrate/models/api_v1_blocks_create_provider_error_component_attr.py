from typing import Literal

ApiV1BlocksCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_BLOCKS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksCreateProviderErrorComponentAttr] = {
    "provider",
}


def check_api_v1_blocks_create_provider_error_component_attr(value: str) -> ApiV1BlocksCreateProviderErrorComponentAttr:
    if value in API_V1_BLOCKS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
