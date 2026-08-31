from typing import Literal

ApiV1BlocksReconcileCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_BLOCKS_RECONCILE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksReconcileCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_blocks_reconcile_create_annotations_error_component_code(
    value: str,
) -> ApiV1BlocksReconcileCreateAnnotationsErrorComponentCode:
    if value in API_V1_BLOCKS_RECONCILE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RECONCILE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
