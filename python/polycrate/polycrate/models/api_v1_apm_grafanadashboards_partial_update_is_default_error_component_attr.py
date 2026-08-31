from typing import Literal

ApiV1ApmGrafanadashboardsPartialUpdateIsDefaultErrorComponentAttr = Literal["is_default"]

API_V1_APM_GRAFANADASHBOARDS_PARTIAL_UPDATE_IS_DEFAULT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ApmGrafanadashboardsPartialUpdateIsDefaultErrorComponentAttr
] = {
    "is_default",
}


def check_api_v1_apm_grafanadashboards_partial_update_is_default_error_component_attr(
    value: str,
) -> ApiV1ApmGrafanadashboardsPartialUpdateIsDefaultErrorComponentAttr:
    if value in API_V1_APM_GRAFANADASHBOARDS_PARTIAL_UPDATE_IS_DEFAULT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_APM_GRAFANADASHBOARDS_PARTIAL_UPDATE_IS_DEFAULT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
