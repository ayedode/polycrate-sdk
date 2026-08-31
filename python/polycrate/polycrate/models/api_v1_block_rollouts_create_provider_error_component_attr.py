from typing import Literal

ApiV1BlockRolloutsCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_BLOCK_ROLLOUTS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_block_rollouts_create_provider_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsCreateProviderErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
