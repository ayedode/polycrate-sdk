from typing import Literal

ComplianceReportScope = Literal["system", "user"]

COMPLIANCE_REPORT_SCOPE_VALUES: set[ComplianceReportScope] = {
    "system",
    "user",
}


def check_compliance_report_scope(value: str) -> ComplianceReportScope:
    if value in COMPLIANCE_REPORT_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMPLIANCE_REPORT_SCOPE_VALUES!r}")
