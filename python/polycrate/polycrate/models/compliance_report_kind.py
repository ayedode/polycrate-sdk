from typing import Literal

ComplianceReportKind = Literal["generic"]

COMPLIANCE_REPORT_KIND_VALUES: set[ComplianceReportKind] = {
    "generic",
}


def check_compliance_report_kind(value: str) -> ComplianceReportKind:
    if value in COMPLIANCE_REPORT_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {COMPLIANCE_REPORT_KIND_VALUES!r}")
