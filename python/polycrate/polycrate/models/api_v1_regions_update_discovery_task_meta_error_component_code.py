from typing import Literal

ApiV1RegionsUpdateDiscoveryTaskMetaErrorComponentCode = Literal["invalid"]

API_V1_REGIONS_UPDATE_DISCOVERY_TASK_META_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegionsUpdateDiscoveryTaskMetaErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_regions_update_discovery_task_meta_error_component_code(
    value: str,
) -> ApiV1RegionsUpdateDiscoveryTaskMetaErrorComponentCode:
    if value in API_V1_REGIONS_UPDATE_DISCOVERY_TASK_META_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_UPDATE_DISCOVERY_TASK_META_ERROR_COMPONENT_CODE_VALUES!r}"
    )
