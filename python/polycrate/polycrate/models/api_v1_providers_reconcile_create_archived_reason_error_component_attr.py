from typing import Literal

ApiV1ProvidersReconcileCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_PROVIDERS_RECONCILE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersReconcileCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_providers_reconcile_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1ProvidersReconcileCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_PROVIDERS_RECONCILE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_RECONCILE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
