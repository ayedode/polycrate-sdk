from typing import Literal

ApiV1LoadbalancersRegionsUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_LOADBALANCERS_REGIONS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_loadbalancers_regions_update_archived_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsUpdateArchivedErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
