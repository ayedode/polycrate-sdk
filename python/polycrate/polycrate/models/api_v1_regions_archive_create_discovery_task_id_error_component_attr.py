from typing import Literal

ApiV1RegionsArchiveCreateDiscoveryTaskIdErrorComponentAttr = Literal["discovery_task_id"]

API_V1_REGIONS_ARCHIVE_CREATE_DISCOVERY_TASK_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsArchiveCreateDiscoveryTaskIdErrorComponentAttr
] = {
    "discovery_task_id",
}


def check_api_v1_regions_archive_create_discovery_task_id_error_component_attr(
    value: str,
) -> ApiV1RegionsArchiveCreateDiscoveryTaskIdErrorComponentAttr:
    if value in API_V1_REGIONS_ARCHIVE_CREATE_DISCOVERY_TASK_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_ARCHIVE_CREATE_DISCOVERY_TASK_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
