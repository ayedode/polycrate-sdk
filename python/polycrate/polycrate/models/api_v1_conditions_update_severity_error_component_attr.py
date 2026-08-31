from typing import Literal

ApiV1ConditionsUpdateSeverityErrorComponentAttr = Literal["severity"]

API_V1_CONDITIONS_UPDATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ConditionsUpdateSeverityErrorComponentAttr] = {
    "severity",
}


def check_api_v1_conditions_update_severity_error_component_attr(
    value: str,
) -> ApiV1ConditionsUpdateSeverityErrorComponentAttr:
    if value in API_V1_CONDITIONS_UPDATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_UPDATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
