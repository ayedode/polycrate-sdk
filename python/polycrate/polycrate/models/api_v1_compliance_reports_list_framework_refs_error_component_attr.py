from typing import Literal

ApiV1ComplianceReportsListFrameworkRefsErrorComponentAttr = Literal["framework_refs"]

API_V1_COMPLIANCE_REPORTS_LIST_FRAMEWORK_REFS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ComplianceReportsListFrameworkRefsErrorComponentAttr
] = {
    "framework_refs",
}


def check_api_v1_compliance_reports_list_framework_refs_error_component_attr(
    value: str,
) -> ApiV1ComplianceReportsListFrameworkRefsErrorComponentAttr:
    if value in API_V1_COMPLIANCE_REPORTS_LIST_FRAMEWORK_REFS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_LIST_FRAMEWORK_REFS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
