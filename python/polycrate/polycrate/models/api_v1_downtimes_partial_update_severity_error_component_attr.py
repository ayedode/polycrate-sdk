from typing import Literal

ApiV1DowntimesPartialUpdateSeverityErrorComponentAttr = Literal["severity"]

API_V1_DOWNTIMES_PARTIAL_UPDATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DowntimesPartialUpdateSeverityErrorComponentAttr
] = {
    "severity",
}


def check_api_v1_downtimes_partial_update_severity_error_component_attr(
    value: str,
) -> ApiV1DowntimesPartialUpdateSeverityErrorComponentAttr:
    if value in API_V1_DOWNTIMES_PARTIAL_UPDATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_PARTIAL_UPDATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
