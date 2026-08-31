from typing import Literal

ApiV1BlockRolloutsPartialUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsPartialUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_block_rollouts_partial_update_provider_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsPartialUpdateProviderErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
