from typing import Literal

ApiV1RegionsArchiveCreateRepairTaskMetaErrorComponentAttr = Literal["repair_task_meta"]

API_V1_REGIONS_ARCHIVE_CREATE_REPAIR_TASK_META_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsArchiveCreateRepairTaskMetaErrorComponentAttr
] = {
    "repair_task_meta",
}


def check_api_v1_regions_archive_create_repair_task_meta_error_component_attr(
    value: str,
) -> ApiV1RegionsArchiveCreateRepairTaskMetaErrorComponentAttr:
    if value in API_V1_REGIONS_ARCHIVE_CREATE_REPAIR_TASK_META_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_ARCHIVE_CREATE_REPAIR_TASK_META_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
