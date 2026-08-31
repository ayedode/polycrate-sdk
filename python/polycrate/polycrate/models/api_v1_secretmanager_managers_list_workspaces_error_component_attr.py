from typing import Literal

ApiV1SecretmanagerManagersListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1_SECRETMANAGER_MANAGERS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersListWorkspacesErrorComponentAttr
] = {
    "workspaces",
}


def check_api_v1_secretmanager_managers_list_workspaces_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersListWorkspacesErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
