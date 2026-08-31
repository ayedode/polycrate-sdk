from typing import Literal

ApiV1BlocksRunDiscoveryCreateVersionErrorComponentAttr = Literal["version"]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_VERSION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateVersionErrorComponentAttr
] = {
    "version",
}


def check_api_v1_blocks_run_discovery_create_version_error_component_attr(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateVersionErrorComponentAttr:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_VERSION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_VERSION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
