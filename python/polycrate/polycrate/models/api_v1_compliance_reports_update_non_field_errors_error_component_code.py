from typing import Literal

ApiV1ComplianceReportsUpdateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_COMPLIANCE_REPORTS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ComplianceReportsUpdateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_compliance_reports_update_non_field_errors_error_component_code(
    value: str,
) -> ApiV1ComplianceReportsUpdateNonFieldErrorsErrorComponentCode:
    if value in API_V1_COMPLIANCE_REPORTS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
