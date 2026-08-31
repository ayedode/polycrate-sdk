from typing import Literal

ApiV1LoadbalancersRegionsCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_LOADBALANCERS_REGIONS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_loadbalancers_regions_create_archived_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsCreateArchivedErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
