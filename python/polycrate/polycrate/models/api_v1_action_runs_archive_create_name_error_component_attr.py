from typing import Literal

ApiV1ActionRunsArchiveCreateNameErrorComponentAttr = Literal["name"]

API_V1_ACTION_RUNS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ActionRunsArchiveCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_action_runs_archive_create_name_error_component_attr(
    value: str,
) -> ApiV1ActionRunsArchiveCreateNameErrorComponentAttr:
    if value in API_V1_ACTION_RUNS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ACTION_RUNS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
