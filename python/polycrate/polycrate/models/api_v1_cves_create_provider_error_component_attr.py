from typing import Literal

ApiV1CvesCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_CVES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesCreateProviderErrorComponentAttr] = {
    "provider",
}


def check_api_v1_cves_create_provider_error_component_attr(value: str) -> ApiV1CvesCreateProviderErrorComponentAttr:
    if value in API_V1_CVES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
