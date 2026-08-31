from typing import Literal

ApiV1ComplianceReportsListKindItem = Literal["generic"]

API_V1_COMPLIANCE_REPORTS_LIST_KIND_ITEM_VALUES: set[ApiV1ComplianceReportsListKindItem] = {
    "generic",
}


def check_api_v1_compliance_reports_list_kind_item(value: str) -> ApiV1ComplianceReportsListKindItem:
    if value in API_V1_COMPLIANCE_REPORTS_LIST_KIND_ITEM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_LIST_KIND_ITEM_VALUES!r}")
