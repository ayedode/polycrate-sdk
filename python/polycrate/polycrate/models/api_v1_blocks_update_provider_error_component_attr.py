from typing import Literal

ApiV1BlocksUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_BLOCKS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksUpdateProviderErrorComponentAttr] = {
    "provider",
}


def check_api_v1_blocks_update_provider_error_component_attr(value: str) -> ApiV1BlocksUpdateProviderErrorComponentAttr:
    if value in API_V1_BLOCKS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
