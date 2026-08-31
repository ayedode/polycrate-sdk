from typing import Literal

ApiV1CvesUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_CVES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesUpdateProviderErrorComponentAttr] = {
    "provider",
}


def check_api_v1_cves_update_provider_error_component_attr(value: str) -> ApiV1CvesUpdateProviderErrorComponentAttr:
    if value in API_V1_CVES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
