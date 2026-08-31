from typing import Literal

ApiV1CvesUpdateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_CVES_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesUpdateProviderIdErrorComponentAttr] = {
    "provider_id",
}


def check_api_v1_cves_update_provider_id_error_component_attr(
    value: str,
) -> ApiV1CvesUpdateProviderIdErrorComponentAttr:
    if value in API_V1_CVES_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_UPDATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
