from typing import Literal

ApiV1RegionsArchiveCreateRepairRunningErrorComponentAttr = Literal["repair_running"]

API_V1_REGIONS_ARCHIVE_CREATE_REPAIR_RUNNING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsArchiveCreateRepairRunningErrorComponentAttr
] = {
    "repair_running",
}


def check_api_v1_regions_archive_create_repair_running_error_component_attr(
    value: str,
) -> ApiV1RegionsArchiveCreateRepairRunningErrorComponentAttr:
    if value in API_V1_REGIONS_ARCHIVE_CREATE_REPAIR_RUNNING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_ARCHIVE_CREATE_REPAIR_RUNNING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
