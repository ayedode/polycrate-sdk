from typing import Literal

ApiV1ProvidersReconcileCreateActiveErrorComponentAttr = Literal["active"]

API_V1_PROVIDERS_RECONCILE_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersReconcileCreateActiveErrorComponentAttr
] = {
    "active",
}


def check_api_v1_providers_reconcile_create_active_error_component_attr(
    value: str,
) -> ApiV1ProvidersReconcileCreateActiveErrorComponentAttr:
    if value in API_V1_PROVIDERS_RECONCILE_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_RECONCILE_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
