from typing import Literal

ApiV1LoadbalancersRegionsCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_LOADBALANCERS_REGIONS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1LoadbalancersRegionsCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_loadbalancers_regions_create_archived_error_component_code(
    value: str,
) -> ApiV1LoadbalancersRegionsCreateArchivedErrorComponentCode:
    if value in API_V1_LOADBALANCERS_REGIONS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
