from typing import Literal

ApiV1PopsPartialUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_POPS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsPartialUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_pops_partial_update_provider_error_component_attr(
    value: str,
) -> ApiV1PopsPartialUpdateProviderErrorComponentAttr:
    if value in API_V1_POPS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
