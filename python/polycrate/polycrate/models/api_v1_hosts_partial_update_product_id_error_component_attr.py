from typing import Literal

ApiV1HostsPartialUpdateProductIdErrorComponentAttr = Literal["product_id"]

API_V1_HOSTS_PARTIAL_UPDATE_PRODUCT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsPartialUpdateProductIdErrorComponentAttr
] = {
    "product_id",
}


def check_api_v1_hosts_partial_update_product_id_error_component_attr(
    value: str,
) -> ApiV1HostsPartialUpdateProductIdErrorComponentAttr:
    if value in API_V1_HOSTS_PARTIAL_UPDATE_PRODUCT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_PARTIAL_UPDATE_PRODUCT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
