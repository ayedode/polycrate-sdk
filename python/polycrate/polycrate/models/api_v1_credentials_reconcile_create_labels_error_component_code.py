from typing import Literal

ApiV1CredentialsReconcileCreateLabelsErrorComponentCode = Literal["invalid"]

API_V1_CREDENTIALS_RECONCILE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CredentialsReconcileCreateLabelsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_credentials_reconcile_create_labels_error_component_code(
    value: str,
) -> ApiV1CredentialsReconcileCreateLabelsErrorComponentCode:
    if value in API_V1_CREDENTIALS_RECONCILE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_RECONCILE_CREATE_LABELS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
