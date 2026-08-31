from typing import Literal

ApiV1ProvidersReconcileCreateKindErrorComponentAttr = Literal["kind"]

API_V1_PROVIDERS_RECONCILE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersReconcileCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_providers_reconcile_create_kind_error_component_attr(
    value: str,
) -> ApiV1ProvidersReconcileCreateKindErrorComponentAttr:
    if value in API_V1_PROVIDERS_RECONCILE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_RECONCILE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
