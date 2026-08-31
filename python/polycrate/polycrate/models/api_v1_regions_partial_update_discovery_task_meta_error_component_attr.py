from typing import Literal

ApiV1RegionsPartialUpdateDiscoveryTaskMetaErrorComponentAttr = Literal["discovery_task_meta"]

API_V1_REGIONS_PARTIAL_UPDATE_DISCOVERY_TASK_META_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1RegionsPartialUpdateDiscoveryTaskMetaErrorComponentAttr
] = {
    "discovery_task_meta",
}


def check_api_v1_regions_partial_update_discovery_task_meta_error_component_attr(
    value: str,
) -> ApiV1RegionsPartialUpdateDiscoveryTaskMetaErrorComponentAttr:
    if value in API_V1_REGIONS_PARTIAL_UPDATE_DISCOVERY_TASK_META_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_PARTIAL_UPDATE_DISCOVERY_TASK_META_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
