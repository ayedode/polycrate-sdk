from typing import Literal

ApiV1ComplianceReportsUpdateNameErrorComponentAttr = Literal["name"]

API_V1_COMPLIANCE_REPORTS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ComplianceReportsUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_compliance_reports_update_name_error_component_attr(
    value: str,
) -> ApiV1ComplianceReportsUpdateNameErrorComponentAttr:
    if value in API_V1_COMPLIANCE_REPORTS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
