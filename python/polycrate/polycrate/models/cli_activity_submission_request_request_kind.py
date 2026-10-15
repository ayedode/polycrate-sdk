from typing import Literal

CLIActivitySubmissionRequestRequestKind = Literal["ssh-session", "workspace-sync"]

CLI_ACTIVITY_SUBMISSION_REQUEST_REQUEST_KIND_VALUES: set[CLIActivitySubmissionRequestRequestKind] = {
    "ssh-session",
    "workspace-sync",
}


def check_cli_activity_submission_request_request_kind(value: str) -> CLIActivitySubmissionRequestRequestKind:
    if value in CLI_ACTIVITY_SUBMISSION_REQUEST_REQUEST_KIND_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CLI_ACTIVITY_SUBMISSION_REQUEST_REQUEST_KIND_VALUES!r}"
    )
