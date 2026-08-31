from typing import Literal

ApiV1ConditionsCreateSeverityErrorComponentAttr = Literal["severity"]

API_V1_CONDITIONS_CREATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ConditionsCreateSeverityErrorComponentAttr] = {
    "severity",
}


def check_api_v1_conditions_create_severity_error_component_attr(
    value: str,
) -> ApiV1ConditionsCreateSeverityErrorComponentAttr:
    if value in API_V1_CONDITIONS_CREATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_CREATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
