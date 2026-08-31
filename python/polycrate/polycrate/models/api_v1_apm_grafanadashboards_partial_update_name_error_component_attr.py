from typing import Literal

ApiV1ApmGrafanadashboardsPartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1_APM_GRAFANADASHBOARDS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ApmGrafanadashboardsPartialUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_apm_grafanadashboards_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1ApmGrafanadashboardsPartialUpdateNameErrorComponentAttr:
    if value in API_V1_APM_GRAFANADASHBOARDS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_APM_GRAFANADASHBOARDS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
