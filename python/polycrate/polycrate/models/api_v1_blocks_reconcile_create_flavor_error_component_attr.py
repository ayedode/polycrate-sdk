from typing import Literal

ApiV1BlocksReconcileCreateFlavorErrorComponentAttr = Literal["flavor"]

API_V1_BLOCKS_RECONCILE_CREATE_FLAVOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksReconcileCreateFlavorErrorComponentAttr
] = {
    "flavor",
}


def check_api_v1_blocks_reconcile_create_flavor_error_component_attr(
    value: str,
) -> ApiV1BlocksReconcileCreateFlavorErrorComponentAttr:
    if value in API_V1_BLOCKS_RECONCILE_CREATE_FLAVOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RECONCILE_CREATE_FLAVOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
