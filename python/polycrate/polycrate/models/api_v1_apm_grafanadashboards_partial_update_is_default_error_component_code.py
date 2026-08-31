from typing import Literal

ApiV1ApmGrafanadashboardsPartialUpdateIsDefaultErrorComponentCode = Literal["invalid", "null"]

API_V1_APM_GRAFANADASHBOARDS_PARTIAL_UPDATE_IS_DEFAULT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ApmGrafanadashboardsPartialUpdateIsDefaultErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_apm_grafanadashboards_partial_update_is_default_error_component_code(
    value: str,
) -> ApiV1ApmGrafanadashboardsPartialUpdateIsDefaultErrorComponentCode:
    if value in API_V1_APM_GRAFANADASHBOARDS_PARTIAL_UPDATE_IS_DEFAULT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_APM_GRAFANADASHBOARDS_PARTIAL_UPDATE_IS_DEFAULT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
