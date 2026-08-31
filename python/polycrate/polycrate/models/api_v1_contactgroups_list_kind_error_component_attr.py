from typing import Literal

ApiV1ContactgroupsListKindErrorComponentAttr = Literal["kind"]

API_V1_CONTACTGROUPS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ContactgroupsListKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_contactgroups_list_kind_error_component_attr(
    value: str,
) -> ApiV1ContactgroupsListKindErrorComponentAttr:
    if value in API_V1_CONTACTGROUPS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
