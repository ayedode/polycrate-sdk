from typing import Literal

ComplianceReportListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

COMPLIANCE_REPORT_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[ComplianceReportListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_compliance_report_list_effective_criticality_type_1(
    value: str,
) -> ComplianceReportListEffectiveCriticalityType1:
    if value in COMPLIANCE_REPORT_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {COMPLIANCE_REPORT_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
