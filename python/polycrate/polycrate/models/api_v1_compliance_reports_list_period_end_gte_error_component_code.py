from typing import Literal

ApiV1ComplianceReportsListPeriodEndGteErrorComponentCode = Literal["invalid"]

API_V1_COMPLIANCE_REPORTS_LIST_PERIOD_END_GTE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ComplianceReportsListPeriodEndGteErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_compliance_reports_list_period_end_gte_error_component_code(
    value: str,
) -> ApiV1ComplianceReportsListPeriodEndGteErrorComponentCode:
    if value in API_V1_COMPLIANCE_REPORTS_LIST_PERIOD_END_GTE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_LIST_PERIOD_END_GTE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
