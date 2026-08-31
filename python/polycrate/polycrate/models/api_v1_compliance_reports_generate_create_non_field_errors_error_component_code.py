from typing import Literal

ApiV1ComplianceReportsGenerateCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ComplianceReportsGenerateCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_compliance_reports_generate_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1ComplianceReportsGenerateCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
