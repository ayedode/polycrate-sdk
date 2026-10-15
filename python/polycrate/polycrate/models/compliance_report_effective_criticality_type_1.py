from typing import Literal

ComplianceReportEffectiveCriticalityType1 = Literal["high", "low", "medium"]

COMPLIANCE_REPORT_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[ComplianceReportEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_compliance_report_effective_criticality_type_1(value: str) -> ComplianceReportEffectiveCriticalityType1:
    if value in COMPLIANCE_REPORT_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMPLIANCE_REPORT_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
