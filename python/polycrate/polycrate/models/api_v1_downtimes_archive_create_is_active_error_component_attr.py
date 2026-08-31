from typing import Literal

ApiV1DowntimesArchiveCreateIsActiveErrorComponentAttr = Literal["is_active"]

API_V1_DOWNTIMES_ARCHIVE_CREATE_IS_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DowntimesArchiveCreateIsActiveErrorComponentAttr
] = {
    "is_active",
}


def check_api_v1_downtimes_archive_create_is_active_error_component_attr(
    value: str,
) -> ApiV1DowntimesArchiveCreateIsActiveErrorComponentAttr:
    if value in API_V1_DOWNTIMES_ARCHIVE_CREATE_IS_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_ARCHIVE_CREATE_IS_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
