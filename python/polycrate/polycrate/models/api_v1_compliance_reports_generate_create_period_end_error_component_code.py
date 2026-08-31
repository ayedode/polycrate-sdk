from typing import Literal

ApiV1ComplianceReportsGenerateCreatePeriodEndErrorComponentCode = Literal["datetime", "invalid", "null"]

API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_PERIOD_END_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ComplianceReportsGenerateCreatePeriodEndErrorComponentCode
] = {
    "datetime",
    "invalid",
    "null",
}


def check_api_v1_compliance_reports_generate_create_period_end_error_component_code(
    value: str,
) -> ApiV1ComplianceReportsGenerateCreatePeriodEndErrorComponentCode:
    if value in API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_PERIOD_END_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_GENERATE_CREATE_PERIOD_END_ERROR_COMPONENT_CODE_VALUES!r}"
    )
