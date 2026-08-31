from typing import Literal

ApiV1HostsDiscoverCreateProductIdErrorComponentAttr = Literal["product_id"]

API_V1_HOSTS_DISCOVER_CREATE_PRODUCT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsDiscoverCreateProductIdErrorComponentAttr
] = {
    "product_id",
}


def check_api_v1_hosts_discover_create_product_id_error_component_attr(
    value: str,
) -> ApiV1HostsDiscoverCreateProductIdErrorComponentAttr:
    if value in API_V1_HOSTS_DISCOVER_CREATE_PRODUCT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_DISCOVER_CREATE_PRODUCT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
