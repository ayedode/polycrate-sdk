from typing import Literal

ApiV1HostsUpdateProductIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_HOSTS_UPDATE_PRODUCT_ID_ERROR_COMPONENT_CODE_VALUES: set[ApiV1HostsUpdateProductIdErrorComponentCode] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_hosts_update_product_id_error_component_code(
    value: str,
) -> ApiV1HostsUpdateProductIdErrorComponentCode:
    if value in API_V1_HOSTS_UPDATE_PRODUCT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_UPDATE_PRODUCT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
