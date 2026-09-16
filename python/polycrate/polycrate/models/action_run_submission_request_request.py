from __future__ import annotations

import datetime
import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.action_run_submission_request_request_block_config_type_0 import (
        ActionRunSubmissionRequestRequestBlockConfigType0,
    )
    from ..models.action_run_submission_request_request_metadata import ActionRunSubmissionRequestRequestMetadata


T = TypeVar("T", bound="ActionRunSubmissionRequestRequest")


@_attrs_define
class ActionRunSubmissionRequestRequest:
    """
    Attributes:
        organization (str): Organization name
        workspace (str): Workspace name
        block (str): Block name
        action (str): Action name
        exit_code (int): Action exit code
        started_at (datetime.datetime): Action start time
        finished_at (datetime.datetime): Action end time
        name (str | Unset): Optional custom name
        stdout (str | Unset): Standard output
        stderr (str | Unset): Standard error
        metadata (ActionRunSubmissionRequestRequestMetadata | Unset): Additional metadata
        block_config (ActionRunSubmissionRequestRequestBlockConfigType0 | None | Unset): Block configuration snapshot
        block_version (None | str | Unset): Block version
    """

    organization: str
    workspace: str
    block: str
    action: str
    exit_code: int
    started_at: datetime.datetime
    finished_at: datetime.datetime
    name: str | Unset = UNSET
    stdout: str | Unset = UNSET
    stderr: str | Unset = UNSET
    metadata: ActionRunSubmissionRequestRequestMetadata | Unset = UNSET
    block_config: ActionRunSubmissionRequestRequestBlockConfigType0 | None | Unset = UNSET
    block_version: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.action_run_submission_request_request_block_config_type_0 import (
            ActionRunSubmissionRequestRequestBlockConfigType0,  # noqa: PLC0415
        )

        organization = self.organization

        workspace = self.workspace

        block = self.block

        action = self.action

        exit_code = self.exit_code

        started_at = self.started_at.isoformat()

        finished_at = self.finished_at.isoformat()

        name = self.name

        stdout = self.stdout

        stderr = self.stderr

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        block_config: dict[str, Any] | None | Unset
        if isinstance(self.block_config, Unset):
            block_config = UNSET
        elif isinstance(self.block_config, ActionRunSubmissionRequestRequestBlockConfigType0):
            block_config = self.block_config.to_dict()
        else:
            block_config = self.block_config

        block_version: None | str | Unset
        if isinstance(self.block_version, Unset):
            block_version = UNSET
        else:
            block_version = self.block_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organization": organization,
                "workspace": workspace,
                "block": block,
                "action": action,
                "exit_code": exit_code,
                "started_at": started_at,
                "finished_at": finished_at,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if stdout is not UNSET:
            field_dict["stdout"] = stdout
        if stderr is not UNSET:
            field_dict["stderr"] = stderr
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if block_config is not UNSET:
            field_dict["block_config"] = block_config
        if block_version is not UNSET:
            field_dict["block_version"] = block_version

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        from ..models.action_run_submission_request_request_block_config_type_0 import (
            ActionRunSubmissionRequestRequestBlockConfigType0,  # noqa: PLC0415
        )

        files: types.RequestFiles = []

        files.append(("organization", (None, str(self.organization).encode(), "text/plain")))

        files.append(("workspace", (None, str(self.workspace).encode(), "text/plain")))

        files.append(("block", (None, str(self.block).encode(), "text/plain")))

        files.append(("action", (None, str(self.action).encode(), "text/plain")))

        files.append(("exit_code", (None, str(self.exit_code).encode(), "text/plain")))

        files.append(("started_at", (None, self.started_at.isoformat().encode(), "text/plain")))

        files.append(("finished_at", (None, self.finished_at.isoformat().encode(), "text/plain")))

        if not isinstance(self.name, Unset):
            files.append(("name", (None, str(self.name).encode(), "text/plain")))

        if not isinstance(self.stdout, Unset):
            files.append(("stdout", (None, str(self.stdout).encode(), "text/plain")))

        if not isinstance(self.stderr, Unset):
            files.append(("stderr", (None, str(self.stderr).encode(), "text/plain")))

        if not isinstance(self.metadata, Unset):
            files.append(("metadata", (None, json.dumps(self.metadata.to_dict()).encode(), "application/json")))

        if not isinstance(self.block_config, Unset):
            if isinstance(self.block_config, ActionRunSubmissionRequestRequestBlockConfigType0):
                files.append(
                    ("block_config", (None, json.dumps(self.block_config.to_dict()).encode(), "application/json"))
                )
            else:
                files.append(("block_config", (None, str(self.block_config).encode(), "text/plain")))

        if not isinstance(self.block_version, Unset):
            if isinstance(self.block_version, str):
                files.append(("block_version", (None, str(self.block_version).encode(), "text/plain")))
            else:
                files.append(("block_version", (None, str(self.block_version).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.action_run_submission_request_request_block_config_type_0 import (
            ActionRunSubmissionRequestRequestBlockConfigType0,  # noqa: PLC0415
        )
        from ..models.action_run_submission_request_request_metadata import (
            ActionRunSubmissionRequestRequestMetadata,  # noqa: PLC0415
        )

        d = dict(src_dict)
        organization = d.pop("organization")

        workspace = d.pop("workspace")

        block = d.pop("block")

        action = d.pop("action")

        exit_code = d.pop("exit_code")

        started_at = datetime.datetime.fromisoformat(d.pop("started_at"))

        finished_at = datetime.datetime.fromisoformat(d.pop("finished_at"))

        name = d.pop("name", UNSET)

        stdout = d.pop("stdout", UNSET)

        stderr = d.pop("stderr", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: ActionRunSubmissionRequestRequestMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ActionRunSubmissionRequestRequestMetadata.from_dict(_metadata)

        def _parse_block_config(data: object) -> ActionRunSubmissionRequestRequestBlockConfigType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                block_config_type_0 = ActionRunSubmissionRequestRequestBlockConfigType0.from_dict(data)

                return block_config_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ActionRunSubmissionRequestRequestBlockConfigType0 | None | Unset, data)

        block_config = _parse_block_config(d.pop("block_config", UNSET))

        def _parse_block_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        block_version = _parse_block_version(d.pop("block_version", UNSET))

        action_run_submission_request_request = cls(
            organization=organization,
            workspace=workspace,
            block=block,
            action=action,
            exit_code=exit_code,
            started_at=started_at,
            finished_at=finished_at,
            name=name,
            stdout=stdout,
            stderr=stderr,
            metadata=metadata,
            block_config=block_config,
            block_version=block_version,
        )

        action_run_submission_request_request.additional_properties = d
        return action_run_submission_request_request

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
