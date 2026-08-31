from typing import Literal

ApiV1ComplianceReportsGenerateCreateForceErrorComponentCode = Literal["invalid", "null"]

API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_FORCE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ComplianceReportsGenerateCreateForceErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_compliance_reports_generate_create_force_error_component_code(
    value: str,
) -> ApiV1ComplianceReportsGenerateCreateForceErrorComponentCode:
    if value in API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_FORCE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_FORCE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
