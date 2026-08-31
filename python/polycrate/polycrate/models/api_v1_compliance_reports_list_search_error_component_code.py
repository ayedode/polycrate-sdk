from typing import Literal

ApiV1ComplianceReportsListSearchErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_COMPLIANCE_REPORTS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ComplianceReportsListSearchErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_compliance_reports_list_search_error_component_code(
    value: str,
) -> ApiV1ComplianceReportsListSearchErrorComponentCode:
    if value in API_V1_COMPLIANCE_REPORTS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES!r}"
    )
