from typing import Literal

ApiV1LoadbalancersRegionsPartialUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersRegionsPartialUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_loadbalancers_regions_partial_update_archived_error_component_code(
    value: str,
) -> ApiV1LoadbalancersRegionsPartialUpdateArchivedErrorComponentCode:
    if value in API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
