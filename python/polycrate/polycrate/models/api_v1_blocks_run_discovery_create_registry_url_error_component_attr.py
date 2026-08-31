from typing import Literal

ApiV1BlocksRunDiscoveryCreateRegistryUrlErrorComponentAttr = Literal["registry_url"]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_REGISTRY_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateRegistryUrlErrorComponentAttr
] = {
    "registry_url",
}


def check_api_v1_blocks_run_discovery_create_registry_url_error_component_attr(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateRegistryUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_REGISTRY_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_REGISTRY_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
