from typing import Literal

ApiV1DeliveryControllersListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1_DELIVERY_CONTROLLERS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DeliveryControllersListWorkspacesErrorComponentAttr
] = {
    "workspaces",
}


def check_api_v1_delivery_controllers_list_workspaces_error_component_attr(
    value: str,
) -> ApiV1DeliveryControllersListWorkspacesErrorComponentAttr:
    if value in API_V1_DELIVERY_CONTROLLERS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DELIVERY_CONTROLLERS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
