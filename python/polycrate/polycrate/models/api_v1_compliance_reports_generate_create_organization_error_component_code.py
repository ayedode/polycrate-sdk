from typing import Literal

ApiV1ComplianceReportsGenerateCreateOrganizationErrorComponentCode = Literal["invalid", "null", "required"]

API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ComplianceReportsGenerateCreateOrganizationErrorComponentCode
] = {
    "invalid",
    "null",
    "required",
}


def check_api_v1_compliance_reports_generate_create_organization_error_component_code(
    value: str,
) -> ApiV1ComplianceReportsGenerateCreateOrganizationErrorComponentCode:
    if value in API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_ORGANIZATION_ERROR_COMPONENT_CODE_VALUES!r}"
    )
