from typing import Literal

ApiV1RegionsArchiveCreateStateErrorComponentAttr = Literal["state"]

API_V1_REGIONS_ARCHIVE_CREATE_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsArchiveCreateStateErrorComponentAttr
] = {
    "state",
}


def check_api_v1_regions_archive_create_state_error_component_attr(
    value: str,
) -> ApiV1RegionsArchiveCreateStateErrorComponentAttr:
    if value in API_V1_REGIONS_ARCHIVE_CREATE_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_ARCHIVE_CREATE_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
