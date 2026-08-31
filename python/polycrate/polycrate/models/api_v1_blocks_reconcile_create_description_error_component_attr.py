from typing import Literal

ApiV1BlocksReconcileCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_BLOCKS_RECONCILE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksReconcileCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_blocks_reconcile_create_description_error_component_attr(
    value: str,
) -> ApiV1BlocksReconcileCreateDescriptionErrorComponentAttr:
    if value in API_V1_BLOCKS_RECONCILE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RECONCILE_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
