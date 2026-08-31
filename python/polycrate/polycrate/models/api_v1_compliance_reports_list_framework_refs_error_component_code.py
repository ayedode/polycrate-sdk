from typing import Literal

ApiV1ComplianceReportsListFrameworkRefsErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_COMPLIANCE_REPORTS_LIST_FRAMEWORK_REFS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ComplianceReportsListFrameworkRefsErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_compliance_reports_list_framework_refs_error_component_code(
    value: str,
) -> ApiV1ComplianceReportsListFrameworkRefsErrorComponentCode:
    if value in API_V1_COMPLIANCE_REPORTS_LIST_FRAMEWORK_REFS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_LIST_FRAMEWORK_REFS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
