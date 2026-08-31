from typing import Literal

ApiV1CredentialsReconcileCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_CREDENTIALS_RECONCILE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsReconcileCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_credentials_reconcile_create_labels_error_component_attr(
    value: str,
) -> ApiV1CredentialsReconcileCreateLabelsErrorComponentAttr:
    if value in API_V1_CREDENTIALS_RECONCILE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_RECONCILE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
