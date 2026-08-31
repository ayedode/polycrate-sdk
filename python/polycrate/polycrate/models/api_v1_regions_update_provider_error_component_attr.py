from typing import Literal

ApiV1RegionsUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_REGIONS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1RegionsUpdateProviderErrorComponentAttr] = {
    "provider",
}


def check_api_v1_regions_update_provider_error_component_attr(
    value: str,
) -> ApiV1RegionsUpdateProviderErrorComponentAttr:
    if value in API_V1_REGIONS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
