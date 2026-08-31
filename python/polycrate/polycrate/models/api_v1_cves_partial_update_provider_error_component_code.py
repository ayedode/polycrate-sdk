from typing import Literal

ApiV1CvesPartialUpdateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_CVES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CvesPartialUpdateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_cves_partial_update_provider_error_component_code(
    value: str,
) -> ApiV1CvesPartialUpdateProviderErrorComponentCode:
    if value in API_V1_CVES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
