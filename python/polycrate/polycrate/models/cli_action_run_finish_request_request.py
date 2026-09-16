from __future__ import annotations

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.cli_action_run_finish_request_status_enum import (
    CLIActionRunFinishRequestStatusEnum,
    check_cli_action_run_finish_request_status_enum,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cli_action_run_finish_request_request_metadata_type_0 import (
        CLIActionRunFinishRequestRequestMetadataType0,
    )


T = TypeVar("T", bound="CLIActionRunFinishRequestRequest")


@_attrs_define
class CLIActionRunFinishRequestRequest:
    """
    Attributes:
        exit_code (int): Action exit code (0=success)
        finished_at (str | Unset): ISO 8601 finish timestamp
        stdout (str | Unset): Standard output
        stderr (str | Unset): Standard error
        metadata (CLIActionRunFinishRequestRequestMetadataType0 | None | Unset): Additional metadata
        status (CLIActionRunFinishRequestStatusEnum | Unset): * `cancelled` - cancelled
    """

    exit_code: int
    finished_at: str | Unset = UNSET
    stdout: str | Unset = UNSET
    stderr: str | Unset = UNSET
    metadata: CLIActionRunFinishRequestRequestMetadataType0 | None | Unset = UNSET
    status: CLIActionRunFinishRequestStatusEnum | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.cli_action_run_finish_request_request_metadata_type_0 import (
            CLIActionRunFinishRequestRequestMetadataType0,  # noqa: PLC0415
        )

        exit_code = self.exit_code

        finished_at = self.finished_at

        stdout = self.stdout

        stderr = self.stderr

        metadata: dict[str, Any] | None | Unset
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, CLIActionRunFinishRequestRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "exit_code": exit_code,
            }
        )
        if finished_at is not UNSET:
            field_dict["finished_at"] = finished_at
        if stdout is not UNSET:
            field_dict["stdout"] = stdout
        if stderr is not UNSET:
            field_dict["stderr"] = stderr
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        from ..models.cli_action_run_finish_request_request_metadata_type_0 import (
            CLIActionRunFinishRequestRequestMetadataType0,  # noqa: PLC0415
        )

        files: types.RequestFiles = []

        files.append(("exit_code", (None, str(self.exit_code).encode(), "text/plain")))

        if not isinstance(self.finished_at, Unset):
            files.append(("finished_at", (None, str(self.finished_at).encode(), "text/plain")))

        if not isinstance(self.stdout, Unset):
            files.append(("stdout", (None, str(self.stdout).encode(), "text/plain")))

        if not isinstance(self.stderr, Unset):
            files.append(("stderr", (None, str(self.stderr).encode(), "text/plain")))

        if not isinstance(self.metadata, Unset):
            if isinstance(self.metadata, CLIActionRunFinishRequestRequestMetadataType0):
                files.append(("metadata", (None, json.dumps(self.metadata.to_dict()).encode(), "application/json")))
            else:
                files.append(("metadata", (None, str(self.metadata).encode(), "text/plain")))

        if not isinstance(self.status, Unset):
            files.append(("status", (None, str(self.status).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cli_action_run_finish_request_request_metadata_type_0 import (
            CLIActionRunFinishRequestRequestMetadataType0,  # noqa: PLC0415
        )

        d = dict(src_dict)
        exit_code = d.pop("exit_code")

        finished_at = d.pop("finished_at", UNSET)

        stdout = d.pop("stdout", UNSET)

        stderr = d.pop("stderr", UNSET)

        def _parse_metadata(data: object) -> CLIActionRunFinishRequestRequestMetadataType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = CLIActionRunFinishRequestRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CLIActionRunFinishRequestRequestMetadataType0 | None | Unset, data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        _status = d.pop("status", UNSET)
        status: CLIActionRunFinishRequestStatusEnum | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_cli_action_run_finish_request_status_enum(_status)

        cli_action_run_finish_request_request = cls(
            exit_code=exit_code,
            finished_at=finished_at,
            stdout=stdout,
            stderr=stderr,
            metadata=metadata,
            status=status,
        )

        cli_action_run_finish_request_request.additional_properties = d
        return cli_action_run_finish_request_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
