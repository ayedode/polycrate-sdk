from typing import Literal

ApiV1ComplianceReportsGenerateCreatePeriodStartErrorComponentAttr = Literal["period_start"]

API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_PERIOD_START_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ComplianceReportsGenerateCreatePeriodStartErrorComponentAttr
] = {
    "period_start",
}


def check_api_v1_compliance_reports_generate_create_period_start_error_component_attr(
    value: str,
) -> ApiV1ComplianceReportsGenerateCreatePeriodStartErrorComponentAttr:
    if value in API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_PERIOD_START_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_PERIOD_START_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
