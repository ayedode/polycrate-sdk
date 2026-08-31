from typing import Literal

ApiV1CvesCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_CVES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesCreateCriticalityErrorComponentAttr] = {
    "criticality",
}


def check_api_v1_cves_create_criticality_error_component_attr(
    value: str,
) -> ApiV1CvesCreateCriticalityErrorComponentAttr:
    if value in API_V1_CVES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
