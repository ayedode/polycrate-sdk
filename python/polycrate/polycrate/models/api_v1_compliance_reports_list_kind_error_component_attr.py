from typing import Literal

ApiV1ComplianceReportsListKindErrorComponentAttr = Literal["kind"]

API_V1_COMPLIANCE_REPORTS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ComplianceReportsListKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_compliance_reports_list_kind_error_component_attr(
    value: str,
) -> ApiV1ComplianceReportsListKindErrorComponentAttr:
    if value in API_V1_COMPLIANCE_REPORTS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
