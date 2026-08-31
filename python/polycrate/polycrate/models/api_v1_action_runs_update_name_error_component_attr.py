from typing import Literal

ApiV1ActionRunsUpdateNameErrorComponentAttr = Literal["name"]

API_V1_ACTION_RUNS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ActionRunsUpdateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_action_runs_update_name_error_component_attr(
    value: str,
) -> ApiV1ActionRunsUpdateNameErrorComponentAttr:
    if value in API_V1_ACTION_RUNS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ACTION_RUNS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
