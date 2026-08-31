from typing import Literal

ApiV1ComplianceReportsListPeriodStartLteErrorComponentCode = Literal["invalid"]

API_V1_COMPLIANCE_REPORTS_LIST_PERIOD_START_LTE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ComplianceReportsListPeriodStartLteErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_compliance_reports_list_period_start_lte_error_component_code(
    value: str,
) -> ApiV1ComplianceReportsListPeriodStartLteErrorComponentCode:
    if value in API_V1_COMPLIANCE_REPORTS_LIST_PERIOD_START_LTE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_LIST_PERIOD_START_LTE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
