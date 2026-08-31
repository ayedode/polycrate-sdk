from typing import Literal

ApiV1ProvidersReconcileCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_PROVIDERS_RECONCILE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersReconcileCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_providers_reconcile_create_annotations_error_component_attr(
    value: str,
) -> ApiV1ProvidersReconcileCreateAnnotationsErrorComponentAttr:
    if value in API_V1_PROVIDERS_RECONCILE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_RECONCILE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
