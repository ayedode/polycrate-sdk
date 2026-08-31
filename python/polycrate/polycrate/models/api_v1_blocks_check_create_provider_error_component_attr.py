from typing import Literal

ApiV1BlocksCheckCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_BLOCKS_CHECK_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksCheckCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_blocks_check_create_provider_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateProviderErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
