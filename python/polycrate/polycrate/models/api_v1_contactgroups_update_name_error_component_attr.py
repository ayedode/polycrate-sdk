from typing import Literal

ApiV1ContactgroupsUpdateNameErrorComponentAttr = Literal["name"]

API_V1_CONTACTGROUPS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ContactgroupsUpdateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_contactgroups_update_name_error_component_attr(
    value: str,
) -> ApiV1ContactgroupsUpdateNameErrorComponentAttr:
    if value in API_V1_CONTACTGROUPS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
