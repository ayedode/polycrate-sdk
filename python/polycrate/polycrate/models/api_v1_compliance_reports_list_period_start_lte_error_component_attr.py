from typing import Literal

ApiV1ComplianceReportsListPeriodStartLteErrorComponentAttr = Literal["period_start_lte"]

API_V1_COMPLIANCE_REPORTS_LIST_PERIOD_START_LTE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ComplianceReportsListPeriodStartLteErrorComponentAttr
] = {
    "period_start_lte",
}


def check_api_v1_compliance_reports_list_period_start_lte_error_component_attr(
    value: str,
) -> ApiV1ComplianceReportsListPeriodStartLteErrorComponentAttr:
    if value in API_V1_COMPLIANCE_REPORTS_LIST_PERIOD_START_LTE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_LIST_PERIOD_START_LTE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
