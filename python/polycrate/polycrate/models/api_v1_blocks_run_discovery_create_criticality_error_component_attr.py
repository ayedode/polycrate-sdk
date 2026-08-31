from typing import Literal

ApiV1BlocksRunDiscoveryCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_blocks_run_discovery_create_criticality_error_component_attr(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateCriticalityErrorComponentAttr:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
