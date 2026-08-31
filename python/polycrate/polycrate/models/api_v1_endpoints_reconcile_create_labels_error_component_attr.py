from typing import Literal

ApiV1EndpointsReconcileCreateLabelsErrorComponentAttr = Literal["labels"]

API_V1_ENDPOINTS_RECONCILE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsReconcileCreateLabelsErrorComponentAttr
] = {
    "labels",
}


def check_api_v1_endpoints_reconcile_create_labels_error_component_attr(
    value: str,
) -> ApiV1EndpointsReconcileCreateLabelsErrorComponentAttr:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_LABELS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
