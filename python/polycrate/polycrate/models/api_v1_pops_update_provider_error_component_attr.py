from typing import Literal

ApiV1PopsUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_POPS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1PopsUpdateProviderErrorComponentAttr] = {
    "provider",
}


def check_api_v1_pops_update_provider_error_component_attr(value: str) -> ApiV1PopsUpdateProviderErrorComponentAttr:
    if value in API_V1_POPS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
