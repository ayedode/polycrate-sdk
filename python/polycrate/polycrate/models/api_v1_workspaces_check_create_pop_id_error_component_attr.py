from typing import Literal

ApiV1WorkspacesCheckCreatePopIdErrorComponentAttr = Literal["pop_id"]

API_V1_WORKSPACES_CHECK_CREATE_POP_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesCheckCreatePopIdErrorComponentAttr
] = {
    "pop_id",
}


def check_api_v1_workspaces_check_create_pop_id_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCheckCreatePopIdErrorComponentAttr:
    if value in API_V1_WORKSPACES_CHECK_CREATE_POP_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_POP_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
