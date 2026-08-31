from typing import Literal

ApiV1ComplianceReportsGenerateCreatePeriodEndErrorComponentAttr = Literal["period_end"]

API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_PERIOD_END_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ComplianceReportsGenerateCreatePeriodEndErrorComponentAttr
] = {
    "period_end",
}


def check_api_v1_compliance_reports_generate_create_period_end_error_component_attr(
    value: str,
) -> ApiV1ComplianceReportsGenerateCreatePeriodEndErrorComponentAttr:
    if value in API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_PERIOD_END_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_PERIOD_END_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
