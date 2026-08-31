from typing import Literal

ApiV1ComplianceReportsCreateNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_COMPLIANCE_REPORTS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ComplianceReportsCreateNameErrorComponentCode
] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_compliance_reports_create_name_error_component_code(
    value: str,
) -> ApiV1ComplianceReportsCreateNameErrorComponentCode:
    if value in API_V1_COMPLIANCE_REPORTS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
