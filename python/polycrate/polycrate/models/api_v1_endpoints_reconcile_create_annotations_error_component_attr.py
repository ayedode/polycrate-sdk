from typing import Literal

ApiV1EndpointsReconcileCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_ENDPOINTS_RECONCILE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsReconcileCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_endpoints_reconcile_create_annotations_error_component_attr(
    value: str,
) -> ApiV1EndpointsReconcileCreateAnnotationsErrorComponentAttr:
    if value in API_V1_ENDPOINTS_RECONCILE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_RECONCILE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
