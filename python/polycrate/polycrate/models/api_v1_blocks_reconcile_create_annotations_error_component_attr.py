from typing import Literal

ApiV1BlocksReconcileCreateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1_BLOCKS_RECONCILE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksReconcileCreateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1_blocks_reconcile_create_annotations_error_component_attr(
    value: str,
) -> ApiV1BlocksReconcileCreateAnnotationsErrorComponentAttr:
    if value in API_V1_BLOCKS_RECONCILE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RECONCILE_CREATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
