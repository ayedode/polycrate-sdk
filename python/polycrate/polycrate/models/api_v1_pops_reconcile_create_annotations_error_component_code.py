from typing import Literal

ApiV1PopsReconcileCreateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1_POPS_RECONCILE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1PopsReconcileCreateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_pops_reconcile_create_annotations_error_component_code(
    value: str,
) -> ApiV1PopsReconcileCreateAnnotationsErrorComponentCode:
    if value in API_V1_POPS_RECONCILE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_RECONCILE_CREATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
