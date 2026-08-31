from typing import Literal

ApiV1LoadbalancersRegionsUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_LOADBALANCERS_REGIONS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsUpdateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_loadbalancers_regions_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
