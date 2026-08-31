from typing import Literal

ComplianceReportStatusEnum = Literal["archived", "failed", "generating", "ready"]

COMPLIANCE_REPORT_STATUS_ENUM_VALUES: set[ComplianceReportStatusEnum] = {
    "archived",
    "failed",
    "generating",
    "ready",
}


def check_compliance_report_status_enum(value: str) -> ComplianceReportStatusEnum:
    if value in COMPLIANCE_REPORT_STATUS_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMPLIANCE_REPORT_STATUS_ENUM_VALUES!r}")
