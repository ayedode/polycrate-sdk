from typing import Literal

ApiV1BlocksRunDiscoveryCreateDocumentationUrlErrorComponentAttr = Literal["documentation_url"]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_DOCUMENTATION_URL_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateDocumentationUrlErrorComponentAttr
] = {
    "documentation_url",
}


def check_api_v1_blocks_run_discovery_create_documentation_url_error_component_attr(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateDocumentationUrlErrorComponentAttr:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_DOCUMENTATION_URL_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_DOCUMENTATION_URL_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
