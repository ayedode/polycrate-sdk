from typing import Literal

ApiV1DowntimesArchiveCreateNameErrorComponentAttr = Literal["name"]

API_V1_DOWNTIMES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DowntimesArchiveCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_downtimes_archive_create_name_error_component_attr(
    value: str,
) -> ApiV1DowntimesArchiveCreateNameErrorComponentAttr:
    if value in API_V1_DOWNTIMES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOWNTIMES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
