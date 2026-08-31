from typing import Literal

ApiV1ContactgroupsPartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1_CONTACTGROUPS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactgroupsPartialUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_contactgroups_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1ContactgroupsPartialUpdateNameErrorComponentAttr:
    if value in API_V1_CONTACTGROUPS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
