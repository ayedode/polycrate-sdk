from typing import Literal

ApiV1ProvidersReconcileCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_PROVIDERS_RECONCILE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersReconcileCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_providers_reconcile_create_archived_error_component_attr(
    value: str,
) -> ApiV1ProvidersReconcileCreateArchivedErrorComponentAttr:
    if value in API_V1_PROVIDERS_RECONCILE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_RECONCILE_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
