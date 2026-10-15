from typing import Literal

ComplianceReportStatus = Literal["archived", "failed", "generating", "ready"]

COMPLIANCE_REPORT_STATUS_VALUES: set[ComplianceReportStatus] = {
    "archived",
    "failed",
    "generating",
    "ready",
}


def check_compliance_report_status(value: str) -> ComplianceReportStatus:
    if value in COMPLIANCE_REPORT_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMPLIANCE_REPORT_STATUS_VALUES!r}")
