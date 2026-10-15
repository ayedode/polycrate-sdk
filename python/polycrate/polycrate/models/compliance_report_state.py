from typing import Literal

ComplianceReportState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

COMPLIANCE_REPORT_STATE_VALUES: set[ComplianceReportState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_compliance_report_state(value: str) -> ComplianceReportState:
    if value in COMPLIANCE_REPORT_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMPLIANCE_REPORT_STATE_VALUES!r}")
