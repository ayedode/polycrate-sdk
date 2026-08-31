from typing import Literal

ApiV1CvesPartialUpdateSeverityErrorComponentAttr = Literal["severity"]

API_V1_CVES_PARTIAL_UPDATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CvesPartialUpdateSeverityErrorComponentAttr
] = {
    "severity",
}


def check_api_v1_cves_partial_update_severity_error_component_attr(
    value: str,
) -> ApiV1CvesPartialUpdateSeverityErrorComponentAttr:
    if value in API_V1_CVES_PARTIAL_UPDATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_PARTIAL_UPDATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
