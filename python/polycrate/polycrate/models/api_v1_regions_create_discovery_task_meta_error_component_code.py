from typing import Literal

ApiV1RegionsCreateDiscoveryTaskMetaErrorComponentCode = Literal["invalid"]

API_V1_REGIONS_CREATE_DISCOVERY_TASK_META_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegionsCreateDiscoveryTaskMetaErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_regions_create_discovery_task_meta_error_component_code(
    value: str,
) -> ApiV1RegionsCreateDiscoveryTaskMetaErrorComponentCode:
    if value in API_V1_REGIONS_CREATE_DISCOVERY_TASK_META_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_CREATE_DISCOVERY_TASK_META_ERROR_COMPONENT_CODE_VALUES!r}"
    )
