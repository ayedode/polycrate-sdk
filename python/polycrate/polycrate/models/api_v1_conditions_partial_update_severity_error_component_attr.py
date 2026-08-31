from typing import Literal

ApiV1ConditionsPartialUpdateSeverityErrorComponentAttr = Literal["severity"]

API_V1_CONDITIONS_PARTIAL_UPDATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionsPartialUpdateSeverityErrorComponentAttr
] = {
    "severity",
}


def check_api_v1_conditions_partial_update_severity_error_component_attr(
    value: str,
) -> ApiV1ConditionsPartialUpdateSeverityErrorComponentAttr:
    if value in API_V1_CONDITIONS_PARTIAL_UPDATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_PARTIAL_UPDATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
