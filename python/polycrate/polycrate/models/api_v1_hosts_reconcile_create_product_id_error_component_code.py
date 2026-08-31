from typing import Literal

ApiV1HostsReconcileCreateProductIdErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_HOSTS_RECONCILE_CREATE_PRODUCT_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1HostsReconcileCreateProductIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_hosts_reconcile_create_product_id_error_component_code(
    value: str,
) -> ApiV1HostsReconcileCreateProductIdErrorComponentCode:
    if value in API_V1_HOSTS_RECONCILE_CREATE_PRODUCT_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_HOSTS_RECONCILE_CREATE_PRODUCT_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
