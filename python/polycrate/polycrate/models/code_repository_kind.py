from typing import Literal

CodeRepositoryKind = Literal["forgejo", "generic", "gitea", "gitlab"]

CODE_REPOSITORY_KIND_VALUES: set[CodeRepositoryKind] = {
    "forgejo",
    "generic",
    "gitea",
    "gitlab",
}


def check_code_repository_kind(value: str) -> CodeRepositoryKind:
    if value in CODE_REPOSITORY_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CODE_REPOSITORY_KIND_VALUES!r}")
