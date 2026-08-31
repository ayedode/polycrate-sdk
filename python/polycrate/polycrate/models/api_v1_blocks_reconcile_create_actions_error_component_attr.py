from typing import Literal

ApiV1BlocksReconcileCreateActionsErrorComponentAttr = Literal["actions"]

API_V1_BLOCKS_RECONCILE_CREATE_ACTIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksReconcileCreateActionsErrorComponentAttr
] = {
    "actions",
}


def check_api_v1_blocks_reconcile_create_actions_error_component_attr(
    value: str,
) -> ApiV1BlocksReconcileCreateActionsErrorComponentAttr:
    if value in API_V1_BLOCKS_RECONCILE_CREATE_ACTIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RECONCILE_CREATE_ACTIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
