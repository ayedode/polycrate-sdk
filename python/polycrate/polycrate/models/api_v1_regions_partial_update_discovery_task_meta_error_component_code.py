from typing import Literal

ApiV1RegionsPartialUpdateDiscoveryTaskMetaErrorComponentCode = Literal["invalid"]

API_V1_REGIONS_PARTIAL_UPDATE_DISCOVERY_TASK_META_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegionsPartialUpdateDiscoveryTaskMetaErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_regions_partial_update_discovery_task_meta_error_component_code(
    value: str,
) -> ApiV1RegionsPartialUpdateDiscoveryTaskMetaErrorComponentCode:
    if value in API_V1_REGIONS_PARTIAL_UPDATE_DISCOVERY_TASK_META_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_PARTIAL_UPDATE_DISCOVERY_TASK_META_ERROR_COMPONENT_CODE_VALUES!r}"
    )
