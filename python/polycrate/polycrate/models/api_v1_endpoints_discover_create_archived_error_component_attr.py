from typing import Literal

ApiV1EndpointsDiscoverCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_ENDPOINTS_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsDiscoverCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_endpoints_discover_create_archived_error_component_attr(
    value: str,
) -> ApiV1EndpointsDiscoverCreateArchivedErrorComponentAttr:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
