from typing import Literal

ApiV1PopsDiscoverCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_POPS_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsDiscoverCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_pops_discover_create_archived_error_component_attr(
    value: str,
) -> ApiV1PopsDiscoverCreateArchivedErrorComponentAttr:
    if value in API_V1_POPS_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
