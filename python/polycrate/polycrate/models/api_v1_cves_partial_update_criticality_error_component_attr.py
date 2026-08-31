from typing import Literal

ApiV1CvesPartialUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_CVES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CvesPartialUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_cves_partial_update_criticality_error_component_attr(
    value: str,
) -> ApiV1CvesPartialUpdateCriticalityErrorComponentAttr:
    if value in API_V1_CVES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
