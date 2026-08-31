from typing import Literal

ApiV1ComplianceReportsListStatusErrorComponentAttr = Literal["status"]

API_V1_COMPLIANCE_REPORTS_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ComplianceReportsListStatusErrorComponentAttr
] = {
    "status",
}


def check_api_v1_compliance_reports_list_status_error_component_attr(
    value: str,
) -> ApiV1ComplianceReportsListStatusErrorComponentAttr:
    if value in API_V1_COMPLIANCE_REPORTS_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_LIST_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
