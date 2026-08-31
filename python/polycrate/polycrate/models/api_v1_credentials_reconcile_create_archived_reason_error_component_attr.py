from typing import Literal

ApiV1CredentialsReconcileCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_CREDENTIALS_RECONCILE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsReconcileCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_credentials_reconcile_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1CredentialsReconcileCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_CREDENTIALS_RECONCILE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_RECONCILE_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
