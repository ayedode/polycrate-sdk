from typing import Literal

ApiV1ComplianceReportsListPeriodEndGteErrorComponentAttr = Literal["period_end_gte"]

API_V1_COMPLIANCE_REPORTS_LIST_PERIOD_END_GTE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ComplianceReportsListPeriodEndGteErrorComponentAttr
] = {
    "period_end_gte",
}


def check_api_v1_compliance_reports_list_period_end_gte_error_component_attr(
    value: str,
) -> ApiV1ComplianceReportsListPeriodEndGteErrorComponentAttr:
    if value in API_V1_COMPLIANCE_REPORTS_LIST_PERIOD_END_GTE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_LIST_PERIOD_END_GTE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
