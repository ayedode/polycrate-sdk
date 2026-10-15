from typing import Literal

CodeRepositoryRequestKind = Literal["forgejo", "generic", "gitea", "gitlab"]

CODE_REPOSITORY_REQUEST_KIND_VALUES: set[CodeRepositoryRequestKind] = {
    "forgejo",
    "generic",
    "gitea",
    "gitlab",
}


def check_code_repository_request_kind(value: str) -> CodeRepositoryRequestKind:
    if value in CODE_REPOSITORY_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CODE_REPOSITORY_REQUEST_KIND_VALUES!r}")
