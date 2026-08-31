from typing import Literal

ApiV1ComplianceReportsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_COMPLIANCE_REPORTS_LIST_STATE_VALUES: set[ApiV1ComplianceReportsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_compliance_reports_list_state(value: str) -> ApiV1ComplianceReportsListState:
    if value in API_V1_COMPLIANCE_REPORTS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_LIST_STATE_VALUES!r}")
