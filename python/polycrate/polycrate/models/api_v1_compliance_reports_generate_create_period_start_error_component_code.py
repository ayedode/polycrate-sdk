from typing import Literal

ApiV1ComplianceReportsGenerateCreatePeriodStartErrorComponentCode = Literal["datetime", "invalid", "null"]

API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_PERIOD_START_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ComplianceReportsGenerateCreatePeriodStartErrorComponentCode
] = {
    "datetime",
    "invalid",
    "null",
}


def check_api_v1_compliance_reports_generate_create_period_start_error_component_code(
    value: str,
) -> ApiV1ComplianceReportsGenerateCreatePeriodStartErrorComponentCode:
    if value in API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_PERIOD_START_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_PERIOD_START_ERROR_COMPONENT_CODE_VALUES!r}"
    )
