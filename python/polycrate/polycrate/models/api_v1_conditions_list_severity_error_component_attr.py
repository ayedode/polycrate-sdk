from typing import Literal

ApiV1ConditionsListSeverityErrorComponentAttr = Literal["severity"]

API_V1_CONDITIONS_LIST_SEVERITY_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ConditionsListSeverityErrorComponentAttr] = {
    "severity",
}


def check_api_v1_conditions_list_severity_error_component_attr(
    value: str,
) -> ApiV1ConditionsListSeverityErrorComponentAttr:
    if value in API_V1_CONDITIONS_LIST_SEVERITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_LIST_SEVERITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
