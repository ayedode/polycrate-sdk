from typing import Literal

ApiV1PopsReconcileCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_POPS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PopsReconcileCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_pops_reconcile_create_provider_error_component_code(
    value: str,
) -> ApiV1PopsReconcileCreateProviderErrorComponentCode:
    if value in API_V1_POPS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_RECONCILE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
