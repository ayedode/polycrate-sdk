from typing import Literal

ComplianceReportEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

COMPLIANCE_REPORT_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[ComplianceReportEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_compliance_report_effective_criticality_type_2_type_1(
    value: str,
) -> ComplianceReportEffectiveCriticalityType2Type1:
    if value in COMPLIANCE_REPORT_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMPLIANCE_REPORT_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
