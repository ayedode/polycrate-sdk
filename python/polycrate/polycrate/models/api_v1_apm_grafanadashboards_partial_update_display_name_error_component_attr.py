from typing import Literal

ApiV1ApmGrafanadashboardsPartialUpdateDisplayNameErrorComponentAttr = Literal["display_name"]

API_V1_APM_GRAFANADASHBOARDS_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ApmGrafanadashboardsPartialUpdateDisplayNameErrorComponentAttr
] = {
    "display_name",
}


def check_api_v1_apm_grafanadashboards_partial_update_display_name_error_component_attr(
    value: str,
) -> ApiV1ApmGrafanadashboardsPartialUpdateDisplayNameErrorComponentAttr:
    if value in API_V1_APM_GRAFANADASHBOARDS_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_APM_GRAFANADASHBOARDS_PARTIAL_UPDATE_DISPLAY_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
