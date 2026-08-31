from typing import Literal

ApiV1CvesUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_CVES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesUpdateCriticalityErrorComponentAttr] = {
    "criticality",
}


def check_api_v1_cves_update_criticality_error_component_attr(
    value: str,
) -> ApiV1CvesUpdateCriticalityErrorComponentAttr:
    if value in API_V1_CVES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
