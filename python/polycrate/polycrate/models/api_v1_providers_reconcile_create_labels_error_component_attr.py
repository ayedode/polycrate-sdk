from typing import Literal

ApiV1ProvidersReconcileCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_PROVIDERS_RECONCILE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersReconcileCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_providers_reconcile_create_labels_error_component_attr(
    value: str,
) -> ApiV1ProvidersReconcileCreateLabelsErrorComponentAttr:
    if value in API_V1_PROVIDERS_RECONCILE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_RECONCILE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
