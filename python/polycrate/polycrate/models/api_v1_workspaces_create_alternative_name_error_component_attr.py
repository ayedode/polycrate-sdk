from typing import Literal

ApiV1WorkspacesCreateAlternativeNameErrorComponentAttr = Literal["alternative_name"]

API_V1_WORKSPACES_CREATE_ALTERNATIVE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesCreateAlternativeNameErrorComponentAttr
] = {
    "alternative_name",
}


def check_api_v1_workspaces_create_alternative_name_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCreateAlternativeNameErrorComponentAttr:
    if value in API_V1_WORKSPACES_CREATE_ALTERNATIVE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CREATE_ALTERNATIVE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
