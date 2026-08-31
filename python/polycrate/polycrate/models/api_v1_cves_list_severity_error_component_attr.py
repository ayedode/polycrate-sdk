from typing import Literal

ApiV1CvesListSeverityErrorComponentAttr = Literal["severity"]

API_V1_CVES_LIST_SEVERITY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1CvesListSeverityErrorComponentAttr] = {
    "severity",
}


def check_api_v1_cves_list_severity_error_component_attr(value: str) -> ApiV1CvesListSeverityErrorComponentAttr:
    if value in API_V1_CVES_LIST_SEVERITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_LIST_SEVERITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
