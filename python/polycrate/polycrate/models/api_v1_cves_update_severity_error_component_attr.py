from typing import Literal

ApiV1CvesUpdateSeverityErrorComponentAttr = Literal["severity"]

API_V1_CVES_UPDATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesUpdateSeverityErrorComponentAttr] = {
    "severity",
}


def check_api_v1_cves_update_severity_error_component_attr(value: str) -> ApiV1CvesUpdateSeverityErrorComponentAttr:
    if value in API_V1_CVES_UPDATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_UPDATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
