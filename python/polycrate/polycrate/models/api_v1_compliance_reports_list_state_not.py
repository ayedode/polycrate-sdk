from typing import Literal

ApiV1ComplianceReportsListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_COMPLIANCE_REPORTS_LIST_STATE_NOT_VALUES: set[ApiV1ComplianceReportsListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_compliance_reports_list_state_not(value: str) -> ApiV1ComplianceReportsListStateNot:
    if value in API_V1_COMPLIANCE_REPORTS_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_LIST_STATE_NOT_VALUES!r}")
