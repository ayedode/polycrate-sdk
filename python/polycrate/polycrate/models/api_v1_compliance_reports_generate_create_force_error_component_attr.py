from typing import Literal

ApiV1ComplianceReportsGenerateCreateForceErrorComponentAttr = Literal["force"]

API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_FORCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ComplianceReportsGenerateCreateForceErrorComponentAttr
] = {
    "force",
}


def check_api_v1_compliance_reports_generate_create_force_error_component_attr(
    value: str,
) -> ApiV1ComplianceReportsGenerateCreateForceErrorComponentAttr:
    if value in API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_FORCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_FORCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
