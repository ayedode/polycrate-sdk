from typing import Literal

CLIActivitySubmissionRequestKindEnum = Literal["ssh-session", "workspace-sync"]

CLI_ACTIVITY_SUBMISSION_REQUEST_KIND_ENUM_VALUES: set[CLIActivitySubmissionRequestKindEnum] = {
    "ssh-session",
    "workspace-sync",
}


def check_cli_activity_submission_request_kind_enum(value: str) -> CLIActivitySubmissionRequestKindEnum:
    if value in CLI_ACTIVITY_SUBMISSION_REQUEST_KIND_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CLI_ACTIVITY_SUBMISSION_REQUEST_KIND_ENUM_VALUES!r}")
