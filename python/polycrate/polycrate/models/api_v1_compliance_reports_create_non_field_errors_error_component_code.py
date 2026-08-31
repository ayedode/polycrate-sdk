from typing import Literal

ApiV1ComplianceReportsCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_COMPLIANCE_REPORTS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ComplianceReportsCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_compliance_reports_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1ComplianceReportsCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_COMPLIANCE_REPORTS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
