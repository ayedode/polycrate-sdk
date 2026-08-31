from typing import Literal

ApiV1ProvidersPartialUpdateCcmBlockErrorComponentAttr = Literal["ccm_block"]

API_V1_PROVIDERS_PARTIAL_UPDATE_CCM_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersPartialUpdateCcmBlockErrorComponentAttr
] = {
    "ccm_block",
}


def check_api_v1_providers_partial_update_ccm_block_error_component_attr(
    value: str,
) -> ApiV1ProvidersPartialUpdateCcmBlockErrorComponentAttr:
    if value in API_V1_PROVIDERS_PARTIAL_UPDATE_CCM_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_PARTIAL_UPDATE_CCM_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
