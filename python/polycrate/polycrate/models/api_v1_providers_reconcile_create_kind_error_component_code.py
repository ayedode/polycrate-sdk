from typing import Literal

ApiV1ProvidersReconcileCreateKindErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_PROVIDERS_RECONCILE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProvidersReconcileCreateKindErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_providers_reconcile_create_kind_error_component_code(
    value: str,
) -> ApiV1ProvidersReconcileCreateKindErrorComponentCode:
    if value in API_V1_PROVIDERS_RECONCILE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_RECONCILE_CREATE_KIND_ERROR_COMPONENT_CODE_VALUES!r}"
    )
