from typing import Literal

ComplianceReportListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

COMPLIANCE_REPORT_LIST_STATE_VALUES: set[ComplianceReportListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_compliance_report_list_state(value: str) -> ComplianceReportListState:
    if value in COMPLIANCE_REPORT_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMPLIANCE_REPORT_LIST_STATE_VALUES!r}")
