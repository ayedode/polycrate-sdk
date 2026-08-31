from typing import Literal

ApiV1ComplianceReportsListOrganizationsErrorComponentAttr = Literal["organizations"]

API_V1_COMPLIANCE_REPORTS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ComplianceReportsListOrganizationsErrorComponentAttr
] = {
    "organizations",
}


def check_api_v1_compliance_reports_list_organizations_error_component_attr(
    value: str,
) -> ApiV1ComplianceReportsListOrganizationsErrorComponentAttr:
    if value in API_V1_COMPLIANCE_REPORTS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_LIST_ORGANIZATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
