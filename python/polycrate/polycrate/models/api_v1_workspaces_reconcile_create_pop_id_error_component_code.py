from typing import Literal

ApiV1WorkspacesReconcileCreatePopIdErrorComponentCode = Literal["does_not_exist", "incorrect_type", "null", "required"]

API_V1_WORKSPACES_RECONCILE_CREATE_POP_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesReconcileCreatePopIdErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "null",
    "required",
}


def check_api_v1_workspaces_reconcile_create_pop_id_error_component_code(
    value: str,
) -> ApiV1WorkspacesReconcileCreatePopIdErrorComponentCode:
    if value in API_V1_WORKSPACES_RECONCILE_CREATE_POP_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RECONCILE_CREATE_POP_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
