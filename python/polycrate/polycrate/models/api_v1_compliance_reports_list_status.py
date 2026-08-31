from typing import Literal

ApiV1ComplianceReportsListStatus = Literal["archived", "failed", "generating", "ready"]

API_V1_COMPLIANCE_REPORTS_LIST_STATUS_VALUES: set[ApiV1ComplianceReportsListStatus] = {
    "archived",
    "failed",
    "generating",
    "ready",
}


def check_api_v1_compliance_reports_list_status(value: str) -> ApiV1ComplianceReportsListStatus:
    if value in API_V1_COMPLIANCE_REPORTS_LIST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_LIST_STATUS_VALUES!r}")
