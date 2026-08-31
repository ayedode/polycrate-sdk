from typing import Literal

ApiV1OrganizationsPartialUpdateCachedOpenIncidentsCountErrorComponentAttr = Literal["cached_open_incidents_count"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_OPEN_INCIDENTS_COUNT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateCachedOpenIncidentsCountErrorComponentAttr
] = {
    "cached_open_incidents_count",
}


def check_api_v1_organizations_partial_update_cached_open_incidents_count_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateCachedOpenIncidentsCountErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_OPEN_INCIDENTS_COUNT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_CACHED_OPEN_INCIDENTS_COUNT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
