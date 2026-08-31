from typing import Literal

ApiV1HostsArchiveCreateProductIdErrorComponentAttr = Literal["product_id"]

API_V1_HOSTS_ARCHIVE_CREATE_PRODUCT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1HostsArchiveCreateProductIdErrorComponentAttr
] = {
    "product_id",
}


def check_api_v1_hosts_archive_create_product_id_error_component_attr(
    value: str,
) -> ApiV1HostsArchiveCreateProductIdErrorComponentAttr:
    if value in API_V1_HOSTS_ARCHIVE_CREATE_PRODUCT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_ARCHIVE_CREATE_PRODUCT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
