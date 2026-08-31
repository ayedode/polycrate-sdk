from typing import Literal

ApiV1ConditionsArchiveCreateSeverityErrorComponentAttr = Literal["severity"]

API_V1_CONDITIONS_ARCHIVE_CREATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionsArchiveCreateSeverityErrorComponentAttr
] = {
    "severity",
}


def check_api_v1_conditions_archive_create_severity_error_component_attr(
    value: str,
) -> ApiV1ConditionsArchiveCreateSeverityErrorComponentAttr:
    if value in API_V1_CONDITIONS_ARCHIVE_CREATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_ARCHIVE_CREATE_SEVERITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
