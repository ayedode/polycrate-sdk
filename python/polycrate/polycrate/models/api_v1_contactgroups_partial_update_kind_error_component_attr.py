from typing import Literal

ApiV1ContactgroupsPartialUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_CONTACTGROUPS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactgroupsPartialUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_contactgroups_partial_update_kind_error_component_attr(
    value: str,
) -> ApiV1ContactgroupsPartialUpdateKindErrorComponentAttr:
    if value in API_V1_CONTACTGROUPS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
