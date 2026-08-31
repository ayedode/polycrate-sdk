from typing import Literal

ApiV1ComplianceReportsGenerateCreateOrganizationErrorComponentAttr = Literal["organization"]

API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ComplianceReportsGenerateCreateOrganizationErrorComponentAttr
] = {
    "organization",
}


def check_api_v1_compliance_reports_generate_create_organization_error_component_attr(
    value: str,
) -> ApiV1ComplianceReportsGenerateCreateOrganizationErrorComponentAttr:
    if value in API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_ORGANIZATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
