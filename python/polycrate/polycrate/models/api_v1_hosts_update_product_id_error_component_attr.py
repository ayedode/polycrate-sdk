from typing import Literal

ApiV1HostsUpdateProductIdErrorComponentAttr = Literal["product_id"]

API_V1_HOSTS_UPDATE_PRODUCT_ID_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1HostsUpdateProductIdErrorComponentAttr] = {
    "product_id",
}


def check_api_v1_hosts_update_product_id_error_component_attr(
    value: str,
) -> ApiV1HostsUpdateProductIdErrorComponentAttr:
    if value in API_V1_HOSTS_UPDATE_PRODUCT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_UPDATE_PRODUCT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
