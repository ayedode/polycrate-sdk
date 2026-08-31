from __future__ import annotations

import json
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.cli_activity_submission_request_kind_enum import (
    CLIActivitySubmissionRequestKindEnum,
    check_cli_activity_submission_request_kind_enum,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cli_activity_submission_request_request_metadata import CLIActivitySubmissionRequestRequestMetadata


T = TypeVar("T", bound="CLIActivitySubmissionRequestRequest")


@_attrs_define
class CLIActivitySubmissionRequestRequest:
    """
    Attributes:
        kind (CLIActivitySubmissionRequestKindEnum): * `ssh-session` - ssh-session
            * `workspace-sync` - workspace-sync
        name (str): Slug-format identifier (required)
        organization (str): Organization name
        workspace (str): Workspace name
        display_name (str | Unset): Optional human-readable label
        block (str | Unset): Block name (ssh-session)
        hostname (str | Unset): Target host (ssh-session)
        ssh_user (str | Unset): SSH user (ssh-session)
        metadata (CLIActivitySubmissionRequestRequestMetadata | Unset): Additional metadata
    """

    kind: CLIActivitySubmissionRequestKindEnum
    name: str
    organization: str
    workspace: str
    display_name: str | Unset = UNSET
    block: str | Unset = UNSET
    hostname: str | Unset = UNSET
    ssh_user: str | Unset = UNSET
    metadata: CLIActivitySubmissionRequestRequestMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        kind: str = self.kind

        name = self.name

        organization = self.organization

        workspace = self.workspace

        display_name = self.display_name

        block = self.block

        hostname = self.hostname

        ssh_user = self.ssh_user

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "kind": kind,
                "name": name,
                "organization": organization,
                "workspace": workspace,
            }
        )
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if block is not UNSET:
            field_dict["block"] = block
        if hostname is not UNSET:
            field_dict["hostname"] = hostname
        if ssh_user is not UNSET:
            field_dict["ssh_user"] = ssh_user
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("kind", (None, str(self.kind).encode(), "text/plain")))

        files.append(("name", (None, str(self.name).encode(), "text/plain")))

        files.append(("organization", (None, str(self.organization).encode(), "text/plain")))

        files.append(("workspace", (None, str(self.workspace).encode(), "text/plain")))

        if not isinstance(self.display_name, Unset):
            files.append(("display_name", (None, str(self.display_name).encode(), "text/plain")))

        if not isinstance(self.block, Unset):
            files.append(("block", (None, str(self.block).encode(), "text/plain")))

        if not isinstance(self.hostname, Unset):
            files.append(("hostname", (None, str(self.hostname).encode(), "text/plain")))

        if not isinstance(self.ssh_user, Unset):
            files.append(("ssh_user", (None, str(self.ssh_user).encode(), "text/plain")))

        if not isinstance(self.metadata, Unset):
            files.append(("metadata", (None, json.dumps(self.metadata.to_dict()).encode(), "application/json")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cli_activity_submission_request_request_metadata import (
            CLIActivitySubmissionRequestRequestMetadata,
        )

        d = dict(src_dict)
        kind = check_cli_activity_submission_request_kind_enum(d.pop("kind"))

        name = d.pop("name")

        organization = d.pop("organization")

        workspace = d.pop("workspace")

        display_name = d.pop("display_name", UNSET)

        block = d.pop("block", UNSET)

        hostname = d.pop("hostname", UNSET)

        ssh_user = d.pop("ssh_user", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: CLIActivitySubmissionRequestRequestMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = CLIActivitySubmissionRequestRequestMetadata.from_dict(_metadata)

        cli_activity_submission_request_request = cls(
            kind=kind,
            name=name,
            organization=organization,
            workspace=workspace,
            display_name=display_name,
            block=block,
            hostname=hostname,
            ssh_user=ssh_user,
            metadata=metadata,
        )

        cli_activity_submission_request_request.additional_properties = d
        return cli_activity_submission_request_request

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
