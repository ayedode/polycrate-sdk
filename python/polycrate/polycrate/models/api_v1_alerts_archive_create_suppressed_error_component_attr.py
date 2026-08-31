from typing import Literal

ApiV1AlertsArchiveCreateSuppressedErrorComponentAttr = Literal["suppressed"]

API_V1_ALERTS_ARCHIVE_CREATE_SUPPRESSED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertsArchiveCreateSuppressedErrorComponentAttr
] = {
    "suppressed",
}


def check_api_v1_alerts_archive_create_suppressed_error_component_attr(
    value: str,
) -> ApiV1AlertsArchiveCreateSuppressedErrorComponentAttr:
    if value in API_V1_ALERTS_ARCHIVE_CREATE_SUPPRESSED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTS_ARCHIVE_CREATE_SUPPRESSED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
