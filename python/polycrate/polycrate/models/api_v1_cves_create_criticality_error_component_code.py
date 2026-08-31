from typing import Literal

ApiV1CvesCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_CVES_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[ApiV1CvesCreateCriticalityErrorComponentCode] = {
    "invalid_choice",
}


def check_api_v1_cves_create_criticality_error_component_code(
    value: str,
) -> ApiV1CvesCreateCriticalityErrorComponentCode:
    if value in API_V1_CVES_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
