from typing import Literal

ApiV1ComplianceReportsArchiveCreateNameErrorComponentAttr = Literal["name"]

API_V1_COMPLIANCE_REPORTS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ComplianceReportsArchiveCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_compliance_reports_archive_create_name_error_component_attr(
    value: str,
) -> ApiV1ComplianceReportsArchiveCreateNameErrorComponentAttr:
    if value in API_V1_COMPLIANCE_REPORTS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_COMPLIANCE_REPORTS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
