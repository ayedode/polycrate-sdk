from typing import Literal

ComplianceReportLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

COMPLIANCE_REPORT_LAST_STATE_VALUES: set[ComplianceReportLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_compliance_report_last_state(value: str) -> ComplianceReportLastState:
    if value in COMPLIANCE_REPORT_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMPLIANCE_REPORT_LAST_STATE_VALUES!r}")
