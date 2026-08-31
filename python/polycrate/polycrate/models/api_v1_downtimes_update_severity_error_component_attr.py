from typing import Literal

ApiV1DowntimesUpdateSeverityErrorComponentAttr = Literal["severity"]

API_V1_DOWNTIMES_UPDATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1DowntimesUpdateSeverityErrorComponentAttr] = {
    "severity",
}


def check_api_v1_downtimes_update_severity_error_component_attr(
    value: str,
) -> ApiV1DowntimesUpdateSeverityErrorComponentAttr:
    if value in API_V1_DOWNTIMES_UPDATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_UPDATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
